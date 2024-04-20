# datagouv-python

[![PyPI version](https://badge.fury.io/py/datagouv-python.svg)](https://badge.fury.io/py/datagouv-python)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MaximePawlakFr/datagouv-python)

Unofficial python client for `data.gouv.fr`.

Official documentation is here: https://guides.data.gouv.fr/guide-data.gouv.fr/api/reference.

Current API version supported = "1".

# Getting Started

```python
from datagouv import DatagouvClient

client = DatagouvClient(MY_API_KEY)

# Get a dataset
dataset = client.datasets.get(my_dataset_id)
dataset_resources = dataset.get('resources')

# Upload a new resource from a file
client.datasets.post_resource_file(my_dataset_id, filename)

# Update a resource file 
client.datasets.put_resource_file(my_dataset_id, filename, resource_id)

# Update a resource
client.datasets.put_resource(my_dataset_id, resource)

```

## Download all resources
```python
from datagouv import ResourcesDownloader

# Get a dataset: https://meteo.data.gouv.fr/datasets/656dab84db1bdf627a40eaae
dataset_id = "656dab84db1bdf627a40eaae"

# Instanciate ResourcesDownloader
downloader = ResourcesDownloader(dataset_id)

# Download to current directory
downloader.download()
```

---

# Development

```
poetry run start
poetry run black datagouv/
poetry run flake8
```

## Build and Publish

### Steps

```bash
poetry version [patch, minor, major]
poetry install
# todo: Update CHANGELOG
git commit -m "vX.X.X"
git tag vX.X.X
poetry build
poetry publish
git push --tags
git push
```

### Commands
```bash
poetry add pytest --group dev

poetry version
poetry version -s

poetry version [patch, minor, major]
```

```bash
poetry build
```


<!-- 
```
python -m build

python -m twine upload --config-file .pypirc -r testpypi dist/*
python -m twine upload --config-file .pypirc -r pypi dist/*
``` -->

#### Config 
```bash
# test-pypi
poetry config repositories.test-pypi https://test.pypi.org/legacy/
poetry config pypi-token.test-pypi MY_TOKEN

poetry publish -r test-pypi 

# pypi
poetry config pypi-token.pypi MY_TOKEN
poetry publish
```

# Resources
* https://pypi.org/project/datagouv-python/

# Roadmap

* [ ] Handle /datasets routes
* [ ] Handle other routes
    * /site
    * /reuses
    * /discussions
    * /organizations
    * /spatial
    * /users
    * /me
    * /workers
    * /tags
    * /topics
    * /posts
    * /transfer
    * /notifications
    * /avatars
    * /harvest

