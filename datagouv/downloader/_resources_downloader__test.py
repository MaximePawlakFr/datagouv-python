import pytest

from datagouv import ResourcesDownloader
from datagouv.downloader._resources_downloader import RESOURCE_TYPES

resource_1 = {"id": "r_1_id", "url": "r_1_url", "type": "main"}
resource_2 = {"id": "r_2_id", "url": "r_2_url", "type": "main"}
resource_3 = {"id": "r_3_id", "url": "r_3_url", "type": "documentation"}
resource_4 = {"id": "r_4_id", "url": "r_4_url", "type": "other"}

dataset_1_id = "id_d_1"
dataset_1 = {
    "id": "dataset_1_id",
    "resources": [resource_1, resource_2, resource_3, resource_4],
}


class MockDatasetsService(object):
    def get(self, dataset_id):
        return dataset_1


class MockDatagouvClient(object):
    def __init__(self) -> None:
        self.datasets = MockDatasetsService()
        return


def test_default():
    d = ResourcesDownloader(dataset_1_id, DatagouvClient=MockDatagouvClient)
    # Test dataset
    assert d is not None
    assert d.dataset_id == dataset_1_id

    # By default, all files types
    assert d.resource_types == RESOURCE_TYPES

    # Test resources
    assert len(d.resources) == 4

    # Test resource
    resource = d.resources[0]
    assert resource.get("id") == "r_1_id"
    assert resource.get("url") == "r_1_url"


def test_no_dataset_id():
    with pytest.raises(TypeError) as error:
        ResourcesDownloader(DatagouvClient=MockDatagouvClient)
    print(error)
    assert (
        str(error.value)
        == "__init__() missing 1 required positional argument: 'dataset_id'"
    )


def test_only_main_files():
    d = ResourcesDownloader(dataset_1_id, ["main"], DatagouvClient=MockDatagouvClient)

    # Test files types
    assert d.resource_types == ["main"]
    assert len(d.resources) == 4
    assert len(d.urls) == 2


def test_main_and_doc_files():
    d = ResourcesDownloader(
        dataset_1_id, ["main", "documentation"], DatagouvClient=MockDatagouvClient
    )
    # Test files types
    assert d.resource_types == ["main", "documentation"]
    assert len(d.resources) == 4
    assert len(d.urls) == 3
