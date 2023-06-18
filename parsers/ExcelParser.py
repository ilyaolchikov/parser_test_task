import pandas as pd
from sqlalchemy.exc import DataError, IntegrityError

from database import BaseDatabase
from parsers.BaseParser import BaseParser


class ExcelParser(BaseParser):
    def __init__(self, db: BaseDatabase, file_path: str):
        super(ExcelParser, self).__init__(db, file_path)
        try:
            self.data = pd.read_excel(file_path, engine='openpyxl')
        except (FileNotFoundError, Exception) as e:
            print(f"Could not read file {self.file_path}. {e}")
            exit(1)

    def parse(self):
        for index, row in self.data.iterrows():
            self.db.save_works_row((DataError, IntegrityError), dict(row))
