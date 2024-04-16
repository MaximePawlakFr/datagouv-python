from datagouv import ResourcesDownloader
import pytest

dataset_1_id = "id_d_1"
dataset_1 = {"id": "dataset_1_id", "resources": [{"id": "r_1_id", "url": "r_1_url"}]}


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

    # Test resrouce
    resource = d.resources[0]
    assert resource.get("id") == "r_1_id"
    assert resource.get("url") == "r_1_url"


def test_no_dataset_id():
    with pytest.raises(TypeError) as error:
        ResourcesDownloader(DatagouvClient=MockDatagouvClient)
    print(error)
    assert str(error.value) == "__init__() missing 1 required positional argument: 'dataset_id'"
