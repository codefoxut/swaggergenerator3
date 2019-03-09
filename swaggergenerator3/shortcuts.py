"""Swagger json generator method.

Source:: https://github.com/venmo/swaggergenerator
         https://github.com/goibibo/swaggergenerator3

**Install swaggergenerator3 before using it.
    $ pip install -e git+https://github.com/goibibo/swaggergenerator3@master?egg=swaggergenerator3

"""
import json
import os
from ast import literal_eval
from os.path import dirname   # pylint: disable=C0412

import requests
import yaml
try:
    from swaggergenerator3 import Generator, get_yaml
except ImportError:
    pass

PROJECT_PATH = dirname(dirname(dirname(os.path.abspath(__file__))))

FILE_LOCATION = os.path.join(PROJECT_PATH, "voyager_proj/docs/_tmp")


class SwaggerDocsGen:

    def __init__(self):
        # Create a Generator.
        self.generator = Generator()
        if not os.path.exists(FILE_LOCATION):
            os.mkdir(FILE_LOCATION)
            print(f"Directory '{FILE_LOCATION}' created")

    def swagger_yml(self, url, params, method, file_name, headers=None):
        """Generate swagger YML.

        Args:
            url:
            params:
            method:
            file_name:

        Returns:

        """
        self.add_endpoint_to_generator(url, params, method, headers=headers)
        self.generate_files(file_name)

    def generate_files(self, file_name, gen_json=True):

        yml_data = get_yaml(self.generator.generate_paths())
        file_path = os.path.join(FILE_LOCATION, f"{file_name}.yaml")

        with open(file_path, 'w') as f:
            f.write(yml_data)

        if gen_json:
            file_path2 = os.path.join(FILE_LOCATION, f"{file_name}.json")

            with open(file_path, 'r') as f, open(file_path2, 'w') as f_2:
                data_yml = yaml.safe_load(f)
                json.dump(data_yml, f_2, indent=2)

        return yml_data

    def add_endpoint_to_generator(self, url, params, method, headers=None):
        # access the url for this source.
        if method == 'GET':
            response = requests.request(method, url, params=params, headers=headers)
        else:
            response = requests.request(method, url, data=params, headers=headers)
        print("response", response.json())
        self.generator.provide_example(response.request, response)


def generate_docs():
    """
    This Function should be used to create apidoc for different API endpoints.

    Returns:

    """
    counter = 0
    print("Welcome to Swagger.json creation.")
    swag_gen = SwaggerDocsGen()
    while counter == 0:
        method = input('Plese enter the method of API (GET/POST). - ') or 'GET'
        url = input('Please enter URL. - ')
        raw = input('Please Enter  data to send with URL. - ')
        if raw:
            params = literal_eval(raw)
        else:
            params = None
        raw = input('Please enter header data. - ')
        if raw:
            headers = literal_eval(raw)
        else:
            headers = {}

        swag_gen.add_endpoint_to_generator(url, params, method, headers=headers)

        raw = input('Please enter 0 to continue or press any key between 1-9. - ')
        if raw:
            counter = literal_eval(raw)
        else:
            counter = 0

        if counter != 0:
            file_name = input('Please enter file_name to save generated data. - ')

            swag_gen.generate_files(file_name)
