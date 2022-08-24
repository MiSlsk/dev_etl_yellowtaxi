# dev_etl_yellowtaxi
testing tools &amp; dev environment


Project root ./dev_etl_yellowtaxi

1. Start the PostgreSQL database and create tables by running docker compose at the project root:
      docker-compose up -d

Host = localhost
Database = yellowtaxi
User = yellowtaxiUser
Password = pass1

2. Create Environment variables and download the dataset to localhost:
      bash ./scripts/init_env.sh
      
3. Create Python project virtual environment and load dependencies:
  ....

4. Partition downloaded dataset:
      bash ./scripts/partition.sh
      
5. ....

6. ....
