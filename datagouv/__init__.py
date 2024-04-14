import importlib.metadata
from datagouv._datagouv_client import DatagouvClient as DatagouvClient # noqa

VERSION:str = importlib.metadata.version("datagouv-python")

