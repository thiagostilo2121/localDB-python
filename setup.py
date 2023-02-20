from setuptools import setup

readme = open("./README.md", "r")


setup(
    name='localDB',
    packages=['local-db', 'os'],  # this must be the same as the name above
    version='0.1.1',
    description='localDB is a Python package that allows you to generate a local database in the file system. With localDB, users can create, update, delete, and search a local database on their system. This package can be useful for applications that require a simple and efficient local data storage solution. Additionally, being a local database solution, it does not require an internet connection or depend on external services.',
    long_description=readme.read(),
    long_description_content_type='text/markdown',
    author='Thiago Stilo',
    author_email='stilothiagovalentin@gmail.com',
    # use the URL to the github repo
    url='https://github.com/thiagostilo2121/localDB-python',
    download_url='https://github.com/thiagostilo2121/localDB-python/tarball/0.1.1',
    keywords=['testing', 'logging', 'example'],
    classifiers=[ ],
    license='MIT',
    include_package_data=True
)