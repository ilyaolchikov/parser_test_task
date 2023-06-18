from dotenv import load_dotenv
from sqlalchemy import MetaData, Table, Column, Integer, String, Date, Float, UniqueConstraint
from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy_utils import database_exists, create_database

from database.BaseDatabase import BaseDatabase
from libs.Singleton import Singleton

load_dotenv()


class PostgreSqlDatabase(BaseDatabase, Singleton):

    def __init__(self):
        super(PostgreSqlDatabase, self).__init__()
        self.engine = create_engine(self.ENGINE_URL)
        if not database_exists(self.ENGINE_URL):
            create_database(self.ENGINE_URL)
        self.connection = self.engine.connect()
        self.init_database_structure()

    def init_database_structure(self):
        self.create_table_works()

    def create_table_works(self):
        meta = MetaData()

        self.works_table = Table(
            'works', meta,
            Column('ID', Integer, primary_key=True, autoincrement=True),
            Column('WBS', String(80), nullable=False, unique=True),
            Column('NAME', String(512), nullable=False),
            Column('START_DATE', Date(), nullable=False),
            Column('END_DATE', Date(), nullable=False),
            Column('EFFORT', Float, nullable=False, default=0),
            UniqueConstraint('WBS')
        )
        meta.create_all(self.engine)

    def save_works_row(self, expected_exceptions: tuple, data: dict):
        new_row = insert(self.works_table).values(list(data.values()))
        updated_row = new_row.on_conflict_do_update(
            constraint='works_WBS_key',
            set_={key: data[key] for key in data if key != 'WBS'}
        )
        try:
            self.connection.execute(updated_row)
        except expected_exceptions:
            print(f'Error at the line: {data}. Skipping...')
        self.connection.commit()
