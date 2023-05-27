import fastavro

class FileWriter:
    def __init__(self, file_path):
        self.file_path = file_path

    def write_to_file(self, data):
        with open(self.file_path, 'wb') as file:
            fastavro.writer(file, data)