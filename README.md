## dev_etl_yellowtaxi
### testing tools &amp; dev environment



Project root: ./dev_etl_yellowtaxi

### Start the PostgreSQL database and create tables by running docker compose at the project root:

```
docker-compose up -d
```

Host = localhost

Database = yellowtaxi

User = yellowtaxiUser

Password = pass1

### Recreate tables without reruning docker compose.
Start bash in a container:
```
docker exec -ti <CONTAINER> bash
```
Copy from Container to Docker Host:
```
docker cp <CONTAINER>:SRC_PATH DEST_PATH
```
Copy from Docker Host to Container:
```
docker cp SRC_PATH <CONTAINER>:DEST_PATH
```
Run the script:
```
docker exec -it <CONTAINER> psql -U <DB_USER> -d <DB_NAME> -f /tmp/file.sql
```

### Create Environment variables and download the dataset to localhost:

```
bash ./scripts/init_env.sh
```
      
### Create Python project virtual environment and load dependencies.

Create virtual environment:

```
python3 -m venv ./.dev_etl_yellowtaxi.venv
```

Activate virtual environment:

```
source ./.dev_etl_yellowtaxi.venv/bin/activate
```

Recreate virtual environment dependencies:

```
python3 -m pip install -r requirements.txt
```


Deactivate virtual environment:
```
deactivate
```

### Partition downloaded dataset:
```
bash ./scripts/partition.sh
```
      
### Load partitioned data into the database and get some data quality observations
```
python3 ./scripts/etl.py
```

### ....
