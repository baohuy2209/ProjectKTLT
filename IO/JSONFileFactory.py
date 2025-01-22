import json


class JSONFileFactory:
    def read_file(self, filename, mode_file):
        with open(filename, mode_file) as file:
            data = json.load(file)
        return data
    def write_file(self, filename, mode_file, data):
        current_data = self.read_file(filename, "r")
        current_data.append(data)
        with open(filename, mode_file, encoding="utf-8") as file:
            json.dump(current_data, file, ensure_ascii=False, indent=4)
