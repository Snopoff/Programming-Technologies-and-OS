from flask import Flask, jsonify
from flask_restful import Api
from sqlalchemy import create_engine
import time
import os

username = os.environ['MYSQL_USER']
password = os.environ['MYSQL_PASSWORD']
host = os.environ['MYSQL_HOST']
db = os.environ['MYSQL_DATABASE']

app = Flask(__name__)
api = Api(app)

time.sleep(30)
connection_str = 'mysql+mysqlconnector://{}:{}@{}:3306/{}'.format(
    username, password, host, db)
engine = create_engine(connection_str)
connection = engine.connect()


@app.route('/')
def home():
    response = connection.execute(
        'SELECT * FROM sample_table2;').fetchall()
    return str(response)


@app.route('/health')
def health():
    resp = jsonify(success=True)
    return resp


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10786)
