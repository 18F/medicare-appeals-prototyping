import dj_database_url
from .base import *

DEBUG = True

DATABASES = {
    "default":
    dj_database_url.config(
        default=
        "postgres://medicare:password@localhost:5432/medicare_appeals_test",
        conn_max_age=600,
    )
}
