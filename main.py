import os

import typer

from database import BaseDatabase
from database.PostgreSqlDatabase import PostgreSqlDatabase
from libs.ParserFactory import JsonParserFactory, ExcelParserFactory
from settings import FileExtensionsEnum

app = typer.Typer()


def create_parser(db: BaseDatabase, input_file: str):
    file_extension = os.path.splitext(input_file)[1]
    parser = None
    if file_extension == FileExtensionsEnum.JSON.value:
        parser = JsonParserFactory.create(db, input_file)
    elif file_extension == FileExtensionsEnum.XLSX.value:
        parser = ExcelParserFactory.create(db, input_file)
    if parser is None:
        print('wrong file extension')
        exit(1)
    return parser


@app.command()
def loader(mode: str, input_file: str):
    db = PostgreSqlDatabase()
    parser = create_parser(db, input_file)
    parser.parse()


if __name__ == "__main__":
    app()
