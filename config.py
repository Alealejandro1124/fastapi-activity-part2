# config.py
import os

DB_USER = os.getenv("DB_USER", "your_mysql_user")
DB_PASS = os.getenv("DB_PASS", "your_mysql_password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "tododb")

SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
)
