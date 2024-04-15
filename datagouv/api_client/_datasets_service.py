from datagouv.api_client._data_requestor import DataRequestor


class DatasetsService(object):
    def __init__(self, options):
        self.options = options
        self.requestor = DataRequestor(self.options)

    def search(self, query, options):
        url = f"/datasets?q={query}"

        return self.requestor.get(url)

    def get(self, dataset_id):
        url = f"/datasets/{dataset_id}"

        return self.requestor.get(url)

    def post_resource_file(self, dataset_id, filename):
        url = f"/datasets/{dataset_id}/upload"

        return self.requestor.post_file(url, filename)

    def put_resource_file(self, dataset_id, filename, resource_id):
        url = f"/datasets/{dataset_id}/resources/{resource_id}/upload"

        return self.requestor.post_file(url, filename)

    def put_resource(self, dataset_id, resource):
        resource_id = resource.get("id")
        url = f"/datasets/{dataset_id}/resources/{resource_id}"

        return self.requestor.put(url, resource)

    """
        only in api v2
        def get_resources(self, dataset_id, options={}):
        page = options.get('page', None)
        page_size = options.get('page_size', None)

        url = f"/datasets/{dataset_id}/resources?"#page={page}&page_size={page_size}"
        url = url + f"page={page}" if page else url
        url = url + f"&page_size={page_size}" if page_size else url
        print(url)
        return self.requestor.get(url)
    """
