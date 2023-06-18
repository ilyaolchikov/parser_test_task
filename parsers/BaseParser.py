from abc import ABC, abstractmethod

from database import BaseDatabase


class BaseParser(ABC):

    @abstractmethod
    def __init__(self, db: BaseDatabase, file_path: str):
        self.file_path = file_path
        self.db = db

    @abstractmethod
    def parse(self):
        pass
