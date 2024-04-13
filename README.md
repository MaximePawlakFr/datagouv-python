# datagouv-python

# Build

```
python -m build

python -m twine upload --config-file .pypirc -r testpypi dist/*
python -m twine upload --config-file .pypirc -r pypi dist/*
```