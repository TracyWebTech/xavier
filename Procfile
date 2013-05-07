web: python manage.py syncdb --noinput; python manage.py migrate --noinput; python manage.py collectstatic --noinput; gunicorn_django -b 0.0.0.0:$PORT -w 3 -k gevent
