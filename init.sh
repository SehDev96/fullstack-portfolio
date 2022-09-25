#!/usr/bin/env bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER developer WITH PASSWORD 'developer' CREATEDB;
    CREATE DATABASE postgres_database;
    GRANT ALL PRIVILEGES ON DATABASE postgres_database TO developer;
EOSQL
