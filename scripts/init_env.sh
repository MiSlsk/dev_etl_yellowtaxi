#!/bin/bash

SCRATCH_SPACE=./.scratch_space
INPUT_FILE=yellow_tripdata_2022-01.parquet
INPUT_FILE_PATH=$SCRATCH_SPACE/$INPUT_FILE
PARTITIONED_PATH=$SCRATCH_SPACE/partitions

mkdir $SCRATCH_SPACE
mkdir $PARTITIONED_PATH

curl https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-01.parquet --output $INPUT_FILE_PATH
