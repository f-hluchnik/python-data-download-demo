import unittest

from src.DataProcessor import DataProcessor


class DataProcessorTests(unittest.TestCase):
    def setUp(self):
        self.processor = DataProcessor()

    def test_process_data_with_slip(self):
        """Test when 'slip' key is present in the data"""
        data = {"slip": "advice slip"}
        result = self.processor.process_data(data)
        self.assertEqual(result, ["advice slip"])

    def test_process_data_with_message(self):
        """Test when 'message' key is present in the data"""
        data = {"message": "error message"}
        with self.assertRaises(Exception) as exception_context:
            self.processor.process_data(data)
        self.assertEqual(
            str(exception_context.exception),
            "('An exception occurred.', \"{'message': 'error message'}\")",
        )

    def test_process_data_unsupported_structure(self):
        """Test when the data has an unsupported structure"""
        data = {"unsupported": "Some data"}
        with self.assertRaises(Exception) as exception_context:
            self.processor.process_data(data)
        self.assertEqual(
            str(exception_context.exception), "Received an unsupported data structure."
        )
