#!/bin/bash
set -e

psql -U postgres -h ${DBHOST} -d postgres -c "CREATE EXTENSION IF NOT EXISTS hstore;"

exec "$@"
