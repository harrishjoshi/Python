#!/bin/bash

# 1. Start PostgreSQL in Docker

# Check if the blog_postgres container is already running
if [ "$(docker ps -q -f name=blog_postgres)" ]; then
    echo "PostgreSQL container (blog_postgres) is already running..."
else
    echo "Starting PostgreSQL in Docker..."
    docker run -d \
      --name blog_postgres \
      -e POSTGRES_USER=blog_user \
      -e POSTGRES_PASSWORD=secret \
      -e POSTGRES_DB=blog_db \
      -p 5432:5432 \
      postgres:17-alpine

    # Wait for PostgreSQL to be ready (max 10 seconds)
    echo "Waiting for PostgreSQL to start..."
    for i in {1..10}; do
        if docker exec blog_postgres pg_isready -U blog_user &> /dev/null; then
            echo "PostgreSQL is ready!"
            break
        fi
        sleep 1
    done
fi

# 2. Export blog database URL and persist it in ~/.bashrc
export BLOG_DATABASE_URL="postgresql://blog_user:secret@127.0.0.1:5432/blog_db"

if ! grep -q "export BLOG_DATABASE_URL=" ~/.bashrc; then
    echo 'export BLOG_DATABASE_URL="postgresql://blog_user:secret@127.0.0.1:5432/blog_db"' >> ~/.bashrc
    source ~/.bashrc
    echo "BLOG_DATABASE_URL added to ~/.bashrc"
fi

echo "Current BLOG_DATABASE_URL: $BLOG_DATABASE_URL"

# 3. Run Alembic migrations to create/update database schema
echo "Applying database migrations..."
if ! alembic upgrade head; then
    echo "Alembic migration failed!"
    exit 1
fi

# 4. Start the FastAPI app with uvicorn
echo "Starting FastAPI application..."
exec uvicorn apps.main:app --reload --host 0.0.0.0 --port 8000