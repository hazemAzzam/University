# gunicorn_config.py

bind = '0.0.0.0:8000'  # Replace with your desired host and port
workers = 4  # Adjust the number of workers as needed
module = 'university.asgi:application'  # Replace 'your_project_name' with your actual project name

