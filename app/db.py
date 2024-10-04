import psycopg2
from .config import Config


def get_db_connection():
    try:
        connection = psycopg2.connect(
            dbname=Config.DB_NAME,          
            user=Config.DB_USER,          
            password=Config.DB_PASSWORD,  
            host=Config.DB_HOST,      
            port='5432'            
        )
        return connection
    except Exception as e:
        print(f"Erreur lors de la connexion à la base de données : {e}")
