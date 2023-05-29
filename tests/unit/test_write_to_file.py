import os
import tempfile
import unittest

from fastavro import reader, writer

from src.FileWriter import FileWriter


class FileWriterTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.file_path = os.path.join(self.temp_dir.name, "test.avro")
        self.writer = FileWriter(self.file_path)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_write_to_file_new_file(self):
        """Test writing to a new file"""
        data = [
            {"id": 1, "advice": "First advice"},
            {"id": 2, "advice": "Second advice"},
        ]

        self.writer.write_to_file(data)

        # Verify file existence
        self.assertTrue(os.path.exists(self.file_path))

        # Verify file content
        with open(self.file_path, "rb") as file:
            records = list(reader(file))
            self.assertEqual(records, data)

    def test_write_to_file_existing_file(self):
        """Test writing to an existing file"""
        initial_data = [{"id": 1, "advice": "Initial advice"}]
        data_to_append = [{"id": 2, "advice": "Appended advice"}]
        expected_data = initial_data + data_to_append

        # Create an existing file with initial data
        with open(self.file_path, "wb") as file:
            writer(file, FileWriter.schema, initial_data)

        # Append data to the existing file
        self.writer.write_to_file(data_to_append)

        # Verify file content
        with open(self.file_path, "rb") as file:
            records = list(reader(file))
            self.assertEqual(records, expected_data)
