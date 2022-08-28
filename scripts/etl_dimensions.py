import glob

import pandas
from sqlalchemy import create_engine, text

filePath = './.scratch_space/partitions/tpep_dropoff_date=**/*.parquet'
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

engine = create_engine(f'postgresql://{user}:{password}@{host}/{database}')
with engine.connect() as connection:
    with connection.begin():
        
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
