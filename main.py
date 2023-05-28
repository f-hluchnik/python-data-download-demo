from dotenv import load_dotenv
from src.APIClient import APIClient
from src.DataProcessor import DataProcessor
from src.FileWriter import FileWriter
import logging

def main():
    load_dotenv()
    
    api_url = "https://www.example.com"
    file_path = "output"

    api_client = APIClient(api_url)
    data = api_client.fetch_data()

    data_processor = DataProcessor()
    processed_data = data_processor.process_data(data)

    file_writer = FileWriter(file_path)
    file_writer.write_to_file(processed_data)

    logging.info("Download and saving was successful.")

if __name__ == '__main__':
    main()