#!/bin/bash

set -e

# Wait for PostgreSQL service to accept connections
until nc -z -v -w30 db 5432
do
  echo "Waiting for database connection..."
  # Wait for 5 seconds before checking again
  sleep 5
done
echo "Database is now available"

# Выполнение миграций и создание администратора
python3 manage.py compilemessages --ignore=.venv
python3 manage.py migrate --noinput
python3 manage.py initadmin

# Добавление или обновление записи в таблице "sites"
python3 manage.py shell <<EOF
from django.contrib.sites.models import Site

site, created = Site.objects.get_or_create(id=1, defaults={'domain': 'localhost', 'name': 'localhost'})
EOF

# Добавление социального приложения Google
python3 manage.py shell <<EOF
from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site

google_app, created = SocialApp.objects.get_or_create(provider='google', defaults={'name': 'гугл авторизация', 'client_id': '$GOOGLE_CLIENT_ID', 'secret': '$GOOGLE_CLIENT_SECRET'})
google_app.sites.add(Site.objects.get(id=1))
EOF

# Запуск сервера
python3 manage.py runserver 0.0.0.0:8000
exec "$@"
