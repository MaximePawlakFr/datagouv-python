import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="datagouv-python",
    version="0.0.1",
    author="Maxime Pawlak",
    author_email="maxime.pawlak@amatek.fr",
    description="A python client for data.gouv.fr",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MaximePawlakFr/datagouv-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        "Operating System :: OS Independent",
    ],
)