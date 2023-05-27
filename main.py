from APIClient import APIClient
from DataProcessor import DataProcessor
from FileWriter import FileWriter

def main():
    api_url = "www.example.com"
    file_path = "output"

    api_client = APIClient(api_url)
    data = api_client.fetch_data()

    data_processor = DataProcessor()
    processed_data = data_processor.process_data(data)

    file_writer = FileWriter(file_path)
    file_writer.write_to_file(processed_data)

    print("Download and saving was successful.")

if __name__ == 'main':
    main()