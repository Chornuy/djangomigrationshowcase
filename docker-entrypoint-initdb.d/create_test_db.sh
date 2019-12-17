#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER djangoproject WITH ENCRYPTED PASSWORD 'qw123321';
    CREATE DATABASE djangoproject;
    GRANT ALL PRIVILEGES ON DATABASE djangoproject TO djangoproject;
EOSQL
