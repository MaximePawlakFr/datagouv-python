import DatasetsService

class DatagouvClient(object):
    def __init__(self, api_key=None):
        self.options = {
          "api_key": api_key,
          "api_base_url": "https://www.data.gouv.fr/api",
          "api_version": "1"
        }

        self.datasets = DatasetsService(self.options)