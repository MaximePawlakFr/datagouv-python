import requests
from tqdm import tqdm
import pathlib


def download(url: str, directory_name: str = None, file_name: str = None):
    resp = requests.get(url, stream=True)
    total = int(resp.headers.get("content-length", 0))
    # Can also replace 'file' with a io.BytesIO object

    if directory_name is None:
        directory_name = "."

    if file_name is None:
        file_name = url.split("/")[-1]

    file_path = pathlib.PurePath(directory_name, file_name)
    with open(file_path, "wb") as file, tqdm(
        desc=file_name,
        total=total,
        unit="iB",
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in resp.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)
