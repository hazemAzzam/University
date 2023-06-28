import os

# remove cache
os.system("python rm_cache.py")

# makemigrations
os.system("python manage.py makemigrations")

# migrate
os.system("python manage.py migrate")