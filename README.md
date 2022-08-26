## dev_etl_yellowtaxi
### testing tools &amp; dev environment



Project root ./dev_etl_yellowtaxi

### Start the PostgreSQL database and create tables by running docker compose at the project root:

```
docker-compose up -d
```

Host = localhost
Database = yellowtaxi
User = yellowtaxiUser
Password = pass1

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

### Partition downloaded dataset:

```
bash ./scripts/partition.sh
```
      
### ....

### ....
