
# Connecting to Postgres DB

## Locally hosted postgres db in Docker

// --- --- --- --- DEFAULT PORT
docker run -it --rm --network bridge postgres psql -h 172.17.0.4 -U postgres

## Connecting to postgres db hosted by render.com

// --- --- --- ---
PGPASSWORD=<PGPASSWORD_HERE> psql -h <HOSTNAME_HERE> -U <DB_USER> <DB_NAME
// --- --- --- ---
ie: PGPASSWORD=<PGPASSWORD_HERE> psql -h <RENDER_INSTANCE_URL> -U <RENDER_INSTANCE_USER_NAME> <RENDER_INSTANCE_DB_NAME>

or

// --- --- --- ---
```.sh
source .env
PGPASSWORD=$PG_PASSWORD psql -h $PG_HOST -U $PG_USER $PG_DB
```

