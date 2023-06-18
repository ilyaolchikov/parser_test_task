import os

from dotenv import load_dotenv

load_dotenv()


class BaseDatabase:
    connection = None
    engine = None

    def __init__(self):
        self.ENGINE_URL = f"{os.getenv('DB_ENGINE')}://{os.getenv('POSTGRES_USER')}:" \
                          f"{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('DB_SERVER')}:{os.getenv('DB_PORT')}/{os.getenv('POSTGRES_DB')}"

    def init_database_structure(self):
        pass
