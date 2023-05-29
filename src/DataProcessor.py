class DataProcessor:
    def process_data(self, data: dict) -> list:
        """
        Process the given data.
        """
        if "slip" in data:
            return [data["slip"]]
        if "message" in data:
            raise Exception("An exception occurred.", str(data))
        raise Exception("Received an unsupported data structure.")
