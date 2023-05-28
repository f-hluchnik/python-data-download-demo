import logging

from src.APIClient import APIClient
from src.DataProcessor import DataProcessor
from src.FileWriter import FileWriter


def main():
    """Fetches data from API, processes it and writes the processed data to a file."""
    api_url = "https://api.adviceslip.com/advice"
    file_path = "output/advices.avro"

    api_client = APIClient(api_url)
    try:
        data = api_client.fetch_data()
    except Exception as exception:
        logging.error("An error occurred during the API request: %s", str(exception))
        raise

    data_processor = DataProcessor()
    try:
        processed_data = data_processor.process_data(data)
    except Exception as exception:
        logging.error("An error occurred while processing the data: %s", str(exception))
        raise

    file_writer = FileWriter(file_path)
    file_writer.write_to_file(processed_data)


if __name__ == "__main__":
    main()
