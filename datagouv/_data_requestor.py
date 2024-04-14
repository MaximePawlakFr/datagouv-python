import requests

class DataRequestor(object):
    def __init__(self, options):
        self.options = options
        self.base_url = f"{self.options.get('api_base_url')}/{self.options.get('api_version')}"
        self.headers = {
            'X-API-KEY': self.options.get('api_key')
        }

    def get(self, url):
        absolute_url = f"{self.base_url}{url}"

        response = requests.get(absolute_url)
        return response.json()
    
    def post_file(self, url, filename):
        absolute_url = f"{self.base_url}{url}"
        
        response = requests.post(absolute_url, files={
            'file': open(filename, 'rb'),
            }, headers=self.headers)

        return  response.json()
    
    def put(self, url, json):
        absolute_url = f"{self.base_url}{url}"
        
        response = requests.put(absolute_url, json=json, headers=self.headers)

        return response.json()
    