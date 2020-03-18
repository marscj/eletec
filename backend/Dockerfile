FROM python:latest
ENV PYTHONUNBUFFERED 1
ENV REDIS_HOST "redis"
RUN mkdir /backend
WORKDIR /backend
COPY . /backend
RUN pip install --upgrade pip && pip install -r requirements.txt
# EXPOSE 8000
# CMD ["gunicorn", "--chdir", "backend", "--bind", ":8000", "backend.wsgi:application"]