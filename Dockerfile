FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    gnupg2 \
    ca-certificates \
    lsb-release \
    && rm -rf /var/lib/apt/lists/*

RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" \
    > /etc/apt/sources.list.d/pgdg.list && \
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
    apt-get update && apt-get install -y --no-install-recommends \
    postgresql-15 \
    postgresql-client-15 \
    postgresql-contrib-15 \
    redis-server \
    supervisor \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /var/lib/postgresql/data && \
    chown -R postgres:postgres /var/lib/postgresql/data && \
    su - postgres -c "/usr/lib/postgresql/15/bin/initdb -D /var/lib/postgresql/data" && \
    su - postgres -c "/usr/lib/postgresql/15/bin/pg_ctl \
        -D /var/lib/postgresql/data \
        -l /tmp/postgres.log \
        -o \"-c listen_addresses='localhost'\" \
        -w start" && \
    su - postgres -c "psql -c \"CREATE USER yokwejuste WITH PASSWORD 'password';\"" && \
    su - postgres -c "createdb visuleo -O yokwejuste" && \
    su - postgres -c "/usr/lib/postgresql/15/bin/pg_ctl -D /var/lib/postgresql/data stop"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8080

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
