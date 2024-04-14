# datagouv-python

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

```python
# Get a dataset
dataset = client.datasets.get(my_dataset_id)
```

```python
# dataset example
{
    'acronym': None,
    'archived': None,
    'badges': [],
    'contact_point': None,
    'created_at': '2023-12-01T10:27:38.839000+00:00',
    'deleted': None,
    'description': "### Présentation\n\nDonnées climatologiques de toutes les stations de métropole et d'outre-mer depuis leur ouverture, pour tous les paramètres disponibles. Ces données ont subi un contrôle climatologique.\n\n### Informations techniques\n\n- Les données quotidiennes sont proposées en téléchargement, par département, et par lots de période au format csv compressé\n- L'ensemble des paramètres est fourni pour l'ensemble des stations météorologiques\n- Les heures sont exprimées en UTC pour la métropole et en FU pour l'outre-mer\n- La mise à jour des fichiers est annuelle pour les historiques avant 1950, mensuelles pour les fichiers de 1950 jusqu'à l'année -2 et quotidiennes pour les deux dernières années",
    'extras': {},
    'frequency': 'daily',
    'frequency_date': '2023-12-02T23:27:25+00:00',
    'harvest': None,
    'id': '6569b51ae64326786e4e8e1a',
    'internal': {
        'created_at_internal': '2023-12-01T10:27:38.839000+00:00',
        'last_modified_internal': '2024-04-14T10:52:41.962000+00:00'
    },
    'last_modified': '2024-04-14T10:52:41.962000+00:00',
    'last_update': '2024-04-14T10:43:29+00:00',
    'license': 'lov2',
    'metrics': {
        'discussions': 10,
        'followers': 1,
        'reuses': 6,
        'views': 2722
    },
    'organization': {
        'acronym': None,
        'badges': [{'kind': 'public-service'}, {'kind': 'certified'}],
        'class': 'Organization',
        'id': '534fff8ba3a7292c64a77ed4',
        'logo': 'https://static.data.gouv.fr/avatars/81/6374003e904fad9ddac7436315fd15-original.png',
        'logo_thumbnail': 'https://static.data.gouv.fr/avatars/81/6374003e904fad9ddac7436315fd15-100.png',
        'name': 'Météo-France',
        'page': 'https://www.data.gouv.fr/fr/organizations/meteo-france/',
        'slug': 'meteo-france',
        'uri': 'https://www.data.gouv.fr/api/1/organizations/meteo-france/'
    },
    'owner': None,
    'page': 'https://www.data.gouv.fr/fr/datasets/donnees-climatologiques-de-base-quotidiennes/',
    'private': False,
    'quality': {
        'all_resources_available': True,
        'dataset_description_quality': True,
        'has_open_format': True,
        'has_resources': True,
        'license': True,
        'resources_documentation': True,
        'score': 1.0,
        'spatial': True,
        'temporal_coverage': True,
        'update_frequency': True,
        'update_fulfilled_in_time': True
    },
    'resources': [{
        'checksum': None,
        'created_at': '2023-12-12T14:16:56.276000+00:00',
        'description': 'Données quotidiennes RR-T-Vent pour le département 01, sur la période 1852-1949',
        'extras': {'analysis:checksum': '25caa34f0345a5dba5750dde5104e27cba8cec90',
        'analysis:content-length': 16964768,
        'analysis:last-modified-at': '2024-03-26T05:54:37+00:00',
        'analysis:last-modified-detection': 'last-modified-header',
        'analysis:mime-type': 'text/plain',
        'analysis:parsing:finished_at': '2024-04-04T14:31:23.414758+00:00',
        'analysis:parsing:started_at': '2024-04-04T14:31:03.522056+00:00',
        'check:available': True,
        'check:date': '2024-01-09T16:03:12.743530+00:00',
        'check:headers:content-length': 762912,
        'check:headers:content-type': 'application/octet-stream',
        'check:status': 200,
        'check:timeout': False},
        'filesize': 762912,
        'filetype': 'remote',
        'format': 'csv.gz',
        'harvest': None,
        'id': 'c1265c02-3a8e-4a28-961e-26b2fd704fe8',
        'internal': {
            'created_at_internal': '2023-12-12T14:16:56.276000+00:00',
            'last_modified_internal': '2024-01-09T13:53:59.098000+00:00'
        },
        'last_modified': '2024-03-26T05:54:37+00:00',
        'latest': 'https://www.data.gouv.fr/fr/datasets/r/c1265c02-3a8e-4a28-961e-26b2fd704fe8',
        'metrics': {
            'views': 1475
            },
        'mime': None,
        'preview_url': None,
        'schema': {
            'name': None,
            'url': None,
            'version': None
            },
        'title': 'QUOT_departement_01_periode_1852-1949_RR-T-Vent',
        'type': 'main',
        'url': 'https://object.files.data.gouv.fr/meteofrance/data/synchro_ftp/BASE/QUOT/Q_01_1852-1949_RR-T-Vent.csv.gz'
    },
     ...
    ]
}
```


# Run

```
poetry run start
poetry run black datagouv/
poetry run flake8
```

# Build
```
poetry version
poetry version -s

poetry version [patch, minor, major]
```

```
poetry build
```

<!-- 
```
python -m build

python -m twine upload --config-file .pypirc -r testpypi dist/*
python -m twine upload --config-file .pypirc -r pypi dist/*
``` -->

# Publish
```
poetry config repositories.test-pypi https://test.pypi.org/legacy/
poetry config pypi-token.test-pypi MY_TOKEN
```
```
poetry publish -r test-pypi 
```

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