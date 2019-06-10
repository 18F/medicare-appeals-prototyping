import os
import psycopg2
import timeit
from invoke import task


DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()
start_time = timeit.default_timer()
def elapsed():
    return round(timeit.default_timer() - start_time, 2)

@task
def commit(c):
    conn.commit()
    c.run('echo "Committing database changes"')


@task
def close(c):
    cur.close()
    conn.close()
    c.run(f'echo "Total Time elapsed: {elapsed()}seconds"')
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
    c.run(f'echo "Created tmp_claims - {elapsed()}seconds"')


@task()
def createmappings(c):
    sql = open('./sql/field_mapping.sql', 'r')
    cur.execute(sql.read())
    sql.close()
    c.run(f'echo "Created field mappings - {elapsed()}seconds"')


@task()
def createappeals(c):
    sql = open('./sql/tmp_appeals.sql', 'r')
    cur.execute(sql.read())
    sql.close()
    c.run(f'echo "Created tmp_appeals {elapsed()}seconds"')

@task()
def createprocedures(c):
    sql = open('./sql/tmp_procedure_codes.sql', 'r')
    cur.execute(sql.read())
    sql.close()
    c.run(f'echo "Created tmp_procedure_codes.sql {elapsed()}seconds"')


@task()
def createclaimstoappeals(c):
    sql = open('./sql/tmp_claims_to_appeals.sql', 'r')
    cur.execute(sql.read())
    sql.close()
    c.run(f'echo "Created tmp_claims_to_appeals {elapsed()}seconds"')


@task()
def sanitize(c):
    sql = open('./sql/sanitize.sql', 'r')
    cur.execute(sql.read())
    sql.close()
    c.run(f'echo "Sanitized data - {elapsed()}seconds"')


@task()
def migratedata(c):
    sql = open('./sql/migrate.sql', 'r')
    cur.execute(sql.read())
    sql.close()
    c.run(f'echo "Migrated sample data into model - {elapsed()}seconds"')


@task
def cleanup(c):
    sql = open('./sql/cleanup.sql', 'r')
    cur.execute(sql.read())
    sql.close()
    c.run(f'echo "Database temp files cleaned - {elapsed()}seconds"')


@task(
    pre=[
        dbsetup,
        createclaims,
        createappeals,
        createprocedures,
        createmappings,
        sanitize,
        createclaimstoappeals,
        migratedata,
        cleanup
    ],
    post=[
        commit,
        close
    ]
)
def createdata(c):
    c.run(f'echo "Data created!"')
