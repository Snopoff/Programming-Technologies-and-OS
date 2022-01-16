FROM ubuntu

RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get install -y pip && \
    pip install pandas && \
    pip install sqlalchemy && \
    pip install pymysql && \
    pip install cryptography && \
    pip install mysql-connector-python 

WORKDIR /app

COPY ./script.py /app/script.py

CMD ["python3", "serv2/script.py"]