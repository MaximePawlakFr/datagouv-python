# datagouv-python

# Run

```
poetry run start
```

# Build
```
poetry version
poetry version -s
```
poetry version [patch, minor, major]

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
