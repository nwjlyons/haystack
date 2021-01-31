
# Haystack

Exploring [Hotwire](https://hotwire.dev/) in [Django](https://www.djangoproject.com).

Setup

- `docker-compose build`
- `docker-compose run web ./manage.py migrate`
- `docker-compose run web ./manage.py createsuperuser`
- `docker-compose up`

New terminal

- `cd haystack/assets`
- `NODE_ENV=production npm run deploy`
