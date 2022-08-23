import pandas

inputPath = './.scratch_space/yellow_tripdata_2022-01.parquet'
outputPath = './.scratch_space/partitions'

# Display all columns and rows
pandas.set_option('display.max_columns', None)
# Display full column value
pandas.set_option('display.max_colwidth', None)

tripDataDf = pandas.read_parquet(path=inputPath)
tripDataDf["tpep_dropoff_date"] = tripDataDf["tpep_dropoff_datetime"].dt.date
tripDataDf.to_parquet(path=outputPath, partition_cols=["tpep_dropoff_date"])
