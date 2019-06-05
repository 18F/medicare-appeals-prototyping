import os
import psycopg2
from invoke import task


DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()


@task
def commit(c):
    conn.commit()
    c.run('echo "Committing database changes"')


@task
def close(c):
    cur.close()
    conn.close()
    c.run('echo "Closing database connection"')


@task
def dbsetup(c):
    sql = open('./sql/db_setup.sql', 'r')
    cur.execute(sql.read())
    sql.close()
    c.run(f'echo "Database setup"')


@task()
def createclaims(c):
    sql = open('./sql/tmp_claims.sql', 'r')
    cur.execute(sql.read())
    sql.close()
    c.run(f'echo "Created tmp_claims"')


@task()
def createmappings(c):
    sql = open('./sql/field_mapping.sql', 'r')
    cur.execute(sql.read())
    sql.close()
    c.run(f'echo "Created field mappings"')


@task()
def createappeals(c):
    sql = open('./sql/tmp_appeals.sql', 'r')
    cur.execute(sql.read())
    sql.close()
    c.run(f'echo "Created tmp_appeals"')


@task()
def createclaimstoappeals(c):
    sql = open('./sql/tmp_claims_to_appeals.sql', 'r')
    cur.execute(sql.read())
    sql.close()
    c.run(f'echo "Created tmp_claims_to_appeals"')


@task()
def sanitize(c):
    sql = open('./sql/sanitize.sql', 'r')
    cur.execute(sql.read())
    sql.close()
    c.run(f'echo "Sanitized data"')


@task(
    pre=[
        dbsetup,
        createclaims,
        createmappings,
        sanitize,
        createappeals,
        createclaimstoappeals,
    ],
    post=[
        commit,
        close
    ]
)
def createdata(c):
    c.run(f'echo "Data created!"')
