import requests
from decouple import config, UndefinedValueError
from print_json import PrintJson

class IPStackRequest(PrintJson):
    """Class for Getting Latitude and Longitude"""
    def __init__(self, ip):
        self.response = {
            "status":200,
            "latitude":0,
            "longitude":0,
            "message":"OK"
        }
        try:
            self.api_key = config('API_KEY')
        except UndefinedValueError:
            self.response["status"] = 400
            self.response["message"] = "API_KEY is not defined in the .env file."

        self.base_url = config('BASE_URL')
        self.ip = ip

        self.get_latitude_longitude()
        super().__init__(self.response)

    def get_latitude_longitude(self):
        url = f"{self.base_url}/{self.ip}?access_key={self.api_key}"
        try:
            resp = requests.get(url)
            if resp.status_code == 200:
                data = resp.json()
                if "latitude" in data and "longitude" in data:
                    self.response["latitude"] = data["latitude"]
                    self.response["longitude"] = data["longitude"]
                else:
                    self.response["message"] = "Not Found latitude and longitude"
                    self.response["status"] = 400
            else:
                self.response["status"] = resp.status_code
        except requests.exceptions.HTTPError as ex:
            self.response["status"] = 500
            self.response["message"] = str(ex)
        except requests.exceptions.RequestException as ex:
            self.response["status"] = 500
            self.response["message"] = str(ex)   
        except Exception as ex:
            self.response["status"] = 500
            self.response["message"] = str(ex)