release: python manage.py migrate --noinput
web: gunicorn haystack.wsgi:application --log-file -
