from __future__ import annotations
import re
from datagouv import DatagouvClient
import datagouv.downloader._utils as _utils


RESOURCE_TYPES = ["main", "documentation", "update", "api", "code", "other"]


class ResourcesDownloader(object):
    def __init__(
        self,
        dataset_id: str,
        resource_types: str | list[str] = "all",
        url_regex: str = None,
        DatagouvClient=DatagouvClient,
    ) -> None:
        """
        resource_types: ["main", "documentation", "update", "api", "code", "other"]
        """
        self.dataset_id: str = dataset_id

        self.dataset: list = None
        self.resources: list = []
        self.urls: list = []

        if resource_types == "all":
            self.resource_types: list = RESOURCE_TYPES
        elif isinstance(resource_types, list):
            self.resource_types = resource_types

        self.url_regex = url_regex

        self.client = DatagouvClient()

        self.prepare()

    def prepare(self) -> None:
        """
        Fetch dataset, set resources and urls.
        """
        self.dataset = self.client.datasets.get(self.dataset_id)
        self.resources = self.dataset.get("resources")
        self.urls = []

        for resource in self.resources:
            # Add url if type is allowed
            type = resource.get("type")
            url = resource.get("url")
            if type in self.resource_types and (
                self.url_regex is None or re.search(self.url_regex, url) is not None
            ):
                self.urls.append(url)

        return None

    def download(self, directory_path: str = None) -> list:
        """
        Download resources into `directory_path`
        """
        for url in self.urls:
            _utils.download(url, directory_path)

        return self.urls
