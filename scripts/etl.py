import glob

import pandas
from sqlalchemy import create_engine, text

# filePath = './.scratch_space/partitions/tpep_dropoff_date=**/*.parquet'
filePath = './.scratch_space/partitions/tpep_dropoff_date=2022-01-1*/*.parquet'
host = 'localhost'
database = 'yellowtaxi'
user = 'yellowtaxiUser'
password = 'pass1'

print(filePath)
files = glob.glob(filePath) 
print(files)
inputDf = pandas.concat([pandas.read_parquet(path=filePath) for filePath in files])

# rename to conform to database column naming convention
processedDf = inputDf.rename(columns={
    "VendorID": "vendor_id",
    "RatecodeID": "rate_code_id",
    "payment_type": "payment_type_id",
    "PULocationID": "pu_location_id",
    "DOLocationID": "do_location_id",
}
)

vendor_Df = pandas.DataFrame({'id':processedDf['vendor_id'].dropna().unique()})
rate_code_Df = pandas.DataFrame({'id':processedDf['rate_code_id'].dropna().unique()})
payment_type_Df = pandas.DataFrame({'id':processedDf['payment_type_id'].dropna().unique()})

# batch data analysis
total_records = len(processedDf)
empty_vendor_ids = processedDf['vendor_id'].isna().sum()
empty_rate_code_id = processedDf['rate_code_id'].isna().sum()
empty_payment_type_id = processedDf['payment_type_id'].isna().sum()

engine = create_engine(f'postgresql://{user}:{password}@{host}/{database}')
with engine.connect() as connection:
    with connection.begin():
    
        # register batch
        result = connection.execute(text(
            f"INSERT INTO batches(files, loaded) VALUES (ARRAY {files},current_timestamp) RETURNING id")).fetchall()
        batchId = result[0]["id"]
        processedDf["batch_id"] = batchId
        
        # load data Dimension # no append_skipdupes
        vendor_Df.to_sql(
            name="vendors",
            con=connection,
            if_exists='append',
            index=False,
            chunksize=100000
        )
        
        # load data Dimension # no append_skipdupes
        rate_code_Df.to_sql(
            name="rate_codes",
            con=connection,
            if_exists='append',
            index=False,
            chunksize=100000
        )
        
        # load data Dimension # no append_skipdupes
        payment_type_Df.to_sql(
            name="payment_types",
            con=connection,
            if_exists='append',
            index=False,
            chunksize=100000
        )
        
        # load data Facts
        processedDf.to_sql(
            name="fact_yellow_taxi_trips",
            con=connection,
            if_exists='append',
            index=False,
            chunksize=100000
        )
        
        # write Analytics
        connection.execute(text(
            f"""
            INSERT INTO batch_analytics(
                batch_id, total_records, empty_vendor_ids, empty_rate_code_id, empty_payment_type_id)
             VALUES (
                {batchId}, {total_records}, {empty_vendor_ids}, {empty_rate_code_id}, {empty_payment_type_id})
             """
        ))
