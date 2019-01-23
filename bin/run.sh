#/bin/bash

set -e

# Only run migrations on the zeroth index when in a cloud.gov environment
if [[ -v CF_INSTANCE_INDEX && $CF_INSTANCE_INDEX == 0 ]]
then
  python manage.py migrate --settings=medicare_appeals.settings.production --noinput
else
  echo "Migrations did not run."
  if [[ -v CF_INSTANCE_INDEX ]]
  then
    echo "CF Instance Index is ${CF_INSTANCE_INDEX}."
  fi
fi

if [[ -f VERSION ]]
then
  VERSION=$(cat VERSION)
else
  VERSION="Manual Deployment"
fi

python manage.py collectstatic --settings=medicare_appeals.settings.production --noinput
gunicorn -t 120 -k gevent -w 2 medicare_appeals.wsgi:application
