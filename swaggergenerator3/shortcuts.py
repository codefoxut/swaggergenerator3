"""Swagger json generator method.

Source:: https://github.com/venmo/swaggergenerator
         https://github.com/goibibo/swaggergenerator3

**Install swaggergenerator3 before using it.
    $ pip install -e git+https://github.com/goibibo/swaggergenerator3@master?egg=swaggergenerator3

"""
import json
import os
from ast import literal_eval
from pprint import pprint
import requests
import yaml

from . import Generator, get_yaml


class SwaggerDocsGen:

    def __init__(self, folder_path=None):
        # Create a Generator.
        self.generator = Generator()
        # create a tmp folder
        self.folder_path = folder_path
        if folder_path and not os.path.exists(folder_path):
            os.mkdir(folder_path)
            print(f"Directory '{folder_path}' created")

    def swagger_yml(self, url, params, method, file_name, headers=None):
        """Generate swagger YML.

        Args:
            url:
            params:
            method:
            file_name:
            headers:

        Returns:

        """
        self.add_endpoint_to_generator(url, params, method, headers=headers)
        self.generate_files(file_name)

    def generate_files(self, file_name, gen_json=True):

        yml_data = get_yaml(self.generator.generate_paths())
        if self.folder_path:
            file_path = os.path.join(self.folder_path, f"{file_name}.yaml")

            with open(file_path, 'w') as f:
                f.write(yml_data)

            if gen_json:
                file_path2 = os.path.join(self.folder_path, f"{file_name}.json")

                with open(file_path, 'r') as f, open(file_path2, 'w') as f_2:
                    data_yml = yaml.safe_load(f)
                    json.dump(data_yml, f_2, indent=2)
        else:
            pprint(yml_data, depth=2, width=80)

        return yml_data

    def add_endpoint_to_generator(self, url, method, params, headers=None, description='',
                                  summary=''):
        # access the url for this source.
        if method == 'GET':
            response = requests.request(method, url, params=params, headers=headers)
        else:
            response = requests.request(method, url, data=params, headers=headers)
        # print("response", response.json())
        self.generator.provide_example(response.request, response, description=description,
                                       summary=summary)

    def generate_docs(self, api_docs_list, filename=None):
        """Generate docs by iterating over the api_doc_list and store the generated doc in
        filename.

        Args:
            api_docs_list (list): a list of apis attributes.
                ** url **: url name
                ** method **: API method.
                ** params **: API params.
                ** headers **: API headers.
                ** description ** : api docstring
            filename (str): filename to store the api documentations. [no extension needed.]

        Returns:

        """
        print("Welcome to swagger documentation generation!!")
        for api_doc in api_docs_list:
            self.add_endpoint_to_generator(
                api_doc['url'], api_doc['method'], api_doc.get('params'),
                api_doc.get('headers'), api_doc.get('description'), api_doc.get('summary'))

        self.generate_files(filename)


def generate_docs_manaul():
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

        swag_gen.add_endpoint_to_generator(url, method, params, headers=headers)

        raw = input('Please enter 0 to continue or press any key between 1-9. - ')
        if raw:
            counter = literal_eval(raw)
        else:
            counter = 0

        if counter != 0:
            file_name = input('Please enter file_name to save generated data. - ')

            gen_doc = swag_gen.generate_files(file_name)
            pprint(gen_doc)
