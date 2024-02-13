import csv

class CSV:
    def __init__(self, filename):
        self.filename = filename
        self._cached_data = None

    def get_array(self):
        if self._cached_data is None:
            self._cached_data = self.parse_csv()
        return self._cached_data

    def parse_csv(self):
        with open(self.filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            return [row for row in reader]

    def save_rows_to_csv(self, data):
        with open(self.filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
        self._cached_data = None  # Invalidate cache after saving

    def invalidate_cache(self):
        self._cached_data = None
