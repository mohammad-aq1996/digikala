FROM python:3.9.6-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

CMD python digikala/manage.py makemigrations --noinput && \
    python digikala/manage.py migrate  --noinput && \
    python digikala/manage.py runserver 0.0.0.0:8000