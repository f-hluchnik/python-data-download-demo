import os

from fastavro import writer


class FileWriter:
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

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def write_to_file(self, data: list) -> None:
        """Write provided data to file. If the file already exists, data are appended to it."""

        mode = "a+b" if os.path.exists(self.file_path) else "wb"

        with open(self.file_path, mode) as file:
            writer(file, FileWriter.schema, data)
