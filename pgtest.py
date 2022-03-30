import os
import sys
import psycopg2

conn = psycopg2.connect("host='%s' port=%d dbname='%s' user='%s' password='%s' connect_timeout=1" %
        (
            os.getenv('POSTGRES_HOST', 'postgres'),
            os.getenv('POSTGRES_PORT', 5432),
            os.getenv('POSTGRES_DB', 'postgres'),
            os.getenv('POSTGRES_USER', 'postgres'),
            os.getenv('POSTGRES_PASSWORD', 'postgres')
        )
    )
print('connected')
conn.close()
sys.exit(0)
