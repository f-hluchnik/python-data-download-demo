import os

from fastavro import parse_schema, writer


class FileWriter:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        schema = {
            "doc": "A piece of advice.",
            "name": "Advice",
            "namespace": "advices",
            "type": "record",
            "fields": [
                {"name": "id", "type": "int"},
                {"name": "advice", "type": "string"},
            ],
        }
        self.parsed_schema = parse_schema(schema)

    def write_to_file(self, data: list) -> None:
        """Write provided data to file. If the file already exists, data are appended to it."""

        if os.path.exists(self.file_path):
            mode = "a+b"
            schema = None
        else:
            mode = "wb"
            schema = self.parsed_schema

        with open(self.file_path, mode) as file:
            writer(file, schema, data)
