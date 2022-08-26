CREATE TABLE IF NOT EXISTS vendors
(
	    id   BIGSERIAL PRIMARY KEY,
	    name VARCHAR(45)
);

CREATE TABLE IF NOT EXISTS rate_codes
(
	    id   BIGSERIAL PRIMARY KEY,
	    name VARCHAR(45)
);

CREATE TABLE IF NOT EXISTS payment_types
(
	    id   BIGSERIAL PRIMARY KEY,
	    name VARCHAR(45)
);

CREATE TABLE IF NOT EXISTS batches
(
	    id     BIGSERIAL PRIMARY KEY,
	    files  VARCHAR(255) ARRAY,
	    loaded TIMESTAMP
);

CREATE TABLE IF NOT EXISTS fact_yellow_taxi_trips
(
	    id                    BIGSERIAL PRIMARY KEY,
	    vendor_id             BIGINT REFERENCES vendors (id),
	    tpep_pickup_datetime  timestamp,
	    tpep_dropoff_datetime timestamp,
	    passenger_count       DECIMAL,
	    trip_distance         DECIMAL,
	    rate_code_id          BIGINT REFERENCES rate_codes (id),
	    store_and_fwd_flag    text,
	    pu_location_id        BIGINT,
	    do_location_id        BIGINT,
	    payment_type_id       BIGINT REFERENCES payment_types (id),
	    fare_amount           DECIMAL,
	    extra                 DECIMAL,
	    mta_tax               DECIMAL,
	    tip_amount            DECIMAL,
	    tolls_amount          DECIMAL,
	    improvement_surcharge DECIMAL,
	    total_amount          DECIMAL,
	    congestion_surcharge  DECIMAL,
	    airport_fee           DECIMAL,
	    batch_id              BIGINT REFERENCES batches (id)
);

CREATE TABLE IF NOT EXISTS batch_analytics
(
	    id                    BIGSERIAL PRIMARY KEY,
	    batch_id              BIGINT REFERENCES batches (id),
	    total_records         BIGINT,
	    empty_vendor_ids      BIGINT,
	    empty_rate_code_id    BIGINT,
	    empty_payment_type_id BIGINT
);

