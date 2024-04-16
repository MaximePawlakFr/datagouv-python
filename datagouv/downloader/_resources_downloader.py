from datagouv import DatagouvClient
import datagouv.downloader._utils as _utils


class ResourcesDownloader(object):
    def __init__(self, dataset_id, DatagouvClient=DatagouvClient):
        self.dataset_id = dataset_id

        self.dataset = None
        self.resources = []
        self.urls = []

        self.client = DatagouvClient()

        self.prepare()

    def prepare(self):
        """
        Fetch dataset, set resources and urls.
        """
        self.dataset = self.client.datasets.get(self.dataset_id)
        self.resources = self.dataset.get("resources")
        self.urls = [resource.get("url") for resource in self.resources]
        return None

    def download(self, directory_path: str = None):
        """
        Download resources into `directory_path`
        """
        for url in self.urls:
            _utils.download(url, directory_path)

        return self.urls
