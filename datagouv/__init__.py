import importlib.metadata
from datagouv.api_client._datagouv_client import DatagouvClient as DatagouvClient  # noqa
from datagouv.downloader._resources_downloader import ResourcesDownloader as ResourcesDownloader  # noqa

VERSION: str = importlib.metadata.version("datagouv-python")
