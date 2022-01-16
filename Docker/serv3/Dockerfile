FROM ubuntu

RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get install -y pip && \
    pip install Flask && \
    pip install Flask-Cors && \
    pip install sqlalchemy && \
    pip install pymysql && \
    pip install cryptography && \
    pip install mysql-connector-python && \
    pip install Flask-RESTful

WORKDIR /app

EXPOSE 10786

COPY app.py app.py

CMD ["python3", "app.py"]