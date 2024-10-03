from flask import Flask
from app.config import Config
import psycopg2
from app import routes


app = Flask(__name__)
app.config.from_object(Config)


def get_db_connection():
    conn = psycopg2.connect(
        host=app.config['DB_HOST'],
        database=app.config['DB_NAME'],
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD']
    ) 
    return conn


