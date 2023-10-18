import json
class PrintJson:
    def __init__(self, data):
        self.data = data
    
    def print_json(self):
        formatted_data = json.dumps(self.data, indent=4, sort_keys=True)
        print(formatted_data)