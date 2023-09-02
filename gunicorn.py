# gunicorn.py

bind = '0.0.0.0:8000'
workers = 4
pythonpath = '/www/wwwroot/University'
module = 'university.asgi:application'
