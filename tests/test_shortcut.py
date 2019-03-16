

import pytest
import requests
import os

from swaggergenerator3.shortcuts import SwaggerDocsGen


def test_shortcut():
    api_docs = [
        {
            'method': "GET",
            'url': "https://httpbin.org/get",
            'params': dict(a=1, b=5, c=6),
            'headers': None,
            'description': 'description will be here.'
         },
        {
            'method': "GET",
            'url': "https://httpbin.org/get",
            'params': dict(d=6, c=30),
            'headers': None,
            'description': 'description will be here.'
        },
        {
            'method': "POST",
            'url': "https://httpbin.org/anything",
            'params': dict(d=6),
            'headers': None,
            'description': 'description will be there.'
        },
        {
            'method': "GET",
            'url': "https://httpbin.org/anything/there",
            'params': dict(e=6),
            'headers': None,
            'description': 'description will be where.'
        },
        {
            'method': "GET",
            'url': "https://httpbin.org/anything/here",
            'params': dict(e=6),
            'headers': None,
            'description': 'description will be where.'
        }

    ]
    file_path = os.path.dirname(__file__)
    SwaggerDocsGen(file_path).generate_docs(api_docs, 'sample')
