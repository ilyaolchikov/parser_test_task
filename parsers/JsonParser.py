import json
from json.decoder import JSONDecodeError

from sqlalchemy.exc import IntegrityError, DataError

from database import BaseDatabase
from .BaseParser import BaseParser


class JsonParser(BaseParser):

    def __init__(self, db: BaseDatabase, file_path: str):
        super(JsonParser, self).__init__(db, file_path)
        try:
            with open(self.file_path) as file_content:
                self.data = json.load(file_content)
        except (FileNotFoundError, JSONDecodeError) as e:
            print(f"Could not read file: {self.file_path}. {e}")
            exit(1)

    def parse(self):
        for line in self.data:
            self.db.save_works_row((IntegrityError, DataError), line)
