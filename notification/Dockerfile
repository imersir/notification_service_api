FROM python:3.7

WORKDIR /code
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r /code/requirements.txt --no-cache-dir
COPY . .
CMD ["gunicorn", "notification.wsgi:application", "--bind", "0:8000" ]

# CMD ["python", "manage.py", "runserver", "0:8000"]
# CMD gunicorn notification.wsgi:application --bind 0.0.0.0:8000