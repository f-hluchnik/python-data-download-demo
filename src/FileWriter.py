from fastavro import writer, parse_schema
import os

class FileWriter:
    def __init__(self, file_path):
        self.file_path = file_path
        schema = {
            'doc': 'A piece of advice.',
            'name': 'Advice',
            'namespace': 'advices',
            'type': 'record',
            'fields': [
                {'name': 'id', 'type': 'int'},
                {'name': 'advice', 'type': 'string'}
            ],
        }
        self.parsed_schema = parse_schema(schema)

    def write_to_file(self, data):
        if os.path.exists(self.file_path):
            mode = 'a+b'
            schema = None
        else:
            mode = 'wb'
            schema = self.parsed_schema

        with open(self.file_path, mode) as file:
            writer(file, schema, data)