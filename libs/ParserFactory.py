from parsers.ExcelParser import ExcelParser
from parsers.JsonParser import JsonParser


class ParserFactory:
    @staticmethod
    def create(db, input_file):
        pass


class JsonParserFactory(ParserFactory):
    @staticmethod
    def create(db, input_file):
        return JsonParser(db, input_file)


class ExcelParserFactory(ParserFactory):
    @staticmethod
    def create(db, input_file):
        return ExcelParser(db, input_file)
