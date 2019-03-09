import pytest
import requests

from swaggergenerator3 import Generator, get_yaml


def test_no_params(httpbin):
    generator = Generator()
    response = requests.get(httpbin.url + '/get')
    generator.provide_example(response.request, response)

    response = requests.post(httpbin.url + '/post')
    generator.provide_example(response.request, response)

    expected = {
        '/post': {
            'post': {
                'responses': {
                    '200': {
                        'description': 'TODO',
                        'schema': {
                            'additionalProperties': False,
                            'type': 'object',
                            'properties': {
                                'files': {
                                    'additionalProperties': False,
                                    'type': 'object',
                                    'properties': {}},
                                'origin': {
                                    'type': 'string'},
                                'form': {
                                    'additionalProperties': False,
                                    'type': 'object',
                                    'properties': {}},
                                'url': {
                                    'type': 'string'},
                                'args': {
                                    'additionalProperties': False,
                                    'type': 'object',
                                    'properties': {}},
                                'headers': {
                                    'additionalProperties': False,
                                    'type': 'object',
                                    'properties': {
                                        'Content-Length': {'type': 'string'},
                                        'Accept-Encoding': {'type': 'string'},
                                        'Connection': {'type': 'string'},
                                        'Accept': {'type': 'string'},
                                        'User-Agent': {'type': 'string'},
                                        'Host': {'type': 'string'}}
                                },
                                'json': {'type': 'null'},
                                'data': {'type': 'string'}}
                        }
                    }
                },
                'parameters': [], 'description': 'TODO'}},
        '/get': {
            'get': {
                'responses': {
                    '200': {
                        'description': 'TODO',
                        'schema': {
                            'additionalProperties': False, 'type': 'object',
                            'properties': {
                                'origin': {'type': 'string'},
                                'headers': {
                                    'additionalProperties': False,
                                    'type': 'object',
                                    'properties': {
                                        # 'Content-Length': {'type': 'string'},
                                        'Accept-Encoding': {'type': 'string'},
                                        'Connection': {'type': 'string'},
                                        'Accept': {'type': 'string'},
                                        'User-Agent': {'type': 'string'},
                                        'Host': {'type': 'string'}}},
                                'args': {
                                    'additionalProperties': False,
                                    'type': 'object',
                                    'properties': {}},
                                'url': {'type': 'string'}}}}},
                'parameters': [], 'description': 'TODO'}}}
    assert generator.generate_paths() == expected


def test_get_params(httpbin):
    generator = Generator()
    response = requests.get(httpbin.url + '/get', params={'query_key': 'query_val'})
    generator.provide_example(response.request, response)

    expected = {
        '/get': {
            'get': {
                'responses': {
                    '200': {
                        'description': 'TODO',
                        'schema': {
                            'additionalProperties': False,
                            'type': 'object',
                            'properties': {
                                'origin': {'type': 'string'},
                                'headers': {
                                    'additionalProperties': False,
                                    'type': 'object',
                                    'properties': {
                                        # 'Content-Length': {'type': 'string'},
                                        'Accept-Encoding': {'type': 'string'},
                                        'Connection': {'type': 'string'},
                                        'Accept': {'type': 'string'},
                                        'User-Agent': {'type': 'string'},
                                        'Host': {'type': 'string'}}},
                                'args': {
                                    'additionalProperties': False,
                                    'type': 'object',
                                    'properties': {
                                        'query_key': {
                                            'type': 'string'}}},
                                'url': {'type': 'string'}}}}
                },
                'parameters': [
                    {'required': True, 'type': 'string', 'name': 'query_key',
                     'in': 'query'}], 'description': 'TODO'}}
    }
    assert generator.generate_paths() == expected


def test_post_body(httpbin):
    generator = Generator()
    response = requests.post(httpbin.url + '/post', json={'body_key': {'body_subkey': 'body_val'}})
    generator.provide_example(response.request, response)

    expected = {
        '/post': {
            'post': {
                'responses': {
                    '200': {
                        'description': 'TODO',
                        'schema': {
                            'additionalProperties': False,
                            'type': 'object',
                            'properties': {
                                'files': {
                                    'additionalProperties': False,
                                    'type': 'object',
                                    'properties': {}},
                                'origin': {'type': 'string'},
                                'form': {
                                    'additionalProperties': False,
                                    'type': 'object',
                                    'properties': {}},
                                'url': {'type': 'string'},
                                'args': {
                                    'additionalProperties': False,
                                    'type': 'object',
                                    'properties': {}},
                                'headers': {
                                    'additionalProperties': False,
                                    'type': 'object',
                                    'properties': {
                                        'Content-Length': {'type': 'string'},
                                        'Accept-Encoding': {'type': 'string'},
                                        'Connection': {'type': 'string'},
                                        'Accept': {'type': 'string'},
                                        'User-Agent': {'type': 'string'},
                                        'Host': {'type': 'string'},
                                        'Content-Type': {'type': 'string'}}},
                                'json': {
                                    'additionalProperties': False,
                                    'type': 'object',
                                    'properties': {
                                        'body_key': {
                                            'additionalProperties': False,
                                            'type': 'object',
                                            'properties': {
                                                'body_subkey': {
                                                    'type': 'string'}}}}
                                },
                                'data': {'type': 'string'}}}}},
                'parameters': [{'schema': {'additionalProperties': False,
                                           'type': 'object', 'properties': {
                        'body_key': {'additionalProperties': False,
                                     'type': 'object', 'properties': {
                                'body_subkey': {'type': 'string'}}}}},
                                'name': 'body_data', 'in': 'body'}],
                'description': 'TODO'}}}
    assert generator.generate_paths() == expected


def test_naive_path_params(httpbin):
    generator = Generator()
    response = requests.get(httpbin.url + '/cache/1')
    generator.provide_example(response.request, response)

    response = requests.get(httpbin.url + '/cache/2')
    generator.provide_example(response.request, response)

    expected = {
        '/cache/{param1}': {
            'get': {
                'responses': {
                    '200': {
                        'description': 'TODO',
                        'schema': {
                            'additionalProperties': False,
                            'type': 'object',
                            'properties': {'origin': {
                                'type': 'string'},
                                'headers': {
                                    'additionalProperties': False,
                                    'type': 'object',
                                    'properties': {
                                        # 'Content-Length': {'type': 'string'},
                                        'Accept-Encoding': {'type': 'string'},
                                        'Connection': {'type': 'string'},
                                        'Accept': {'type': 'string'},
                                        'User-Agent': {'type': 'string'},
                                        'Host': {'type': 'string'}}},
                                'args': {
                                    'additionalProperties': False,
                                    'type': 'object',
                                    'properties': {}},
                                'url': {'type': 'string'}}}
                    }
                },
                'parameters': [{'required': True, 'type': 'string',
                                'name': 'param1', 'in': 'path'}],
                'description': 'TODO'}}}
    assert generator.generate_paths() == expected


def test_component_length_mismatch(httpbin):
    generator = Generator()
    response = requests.get(httpbin.url + '/get')
    generator.provide_example(response.request, response)

    response = requests.get(httpbin.url + '/cache/2')
    generator.provide_example(response.request, response)

    expected = {
        '/get': {
            'get': {
                'responses': {
                    '200': {
                        'description': 'TODO',
                        'schema': {
                            'additionalProperties': False,
                                   'type': 'object',
                                   'properties': {
                                       'origin': {'type': 'string'},
                                       'headers': {
                                           'additionalProperties': False,
                                           'type': 'object',
                                           'properties': {
                                               # 'Content-Length': {'type': 'string'},
                                               'Accept-Encoding': {'type': 'string'},
                                               'Connection': {'type': 'string'},
                                               'Accept': {'type': 'string'},
                                               'User-Agent': {'type': 'string'},
                                               'Host': {'type': 'string'}}},
                                       'args': {
                                           'additionalProperties': False,
                                           'type': 'object',
                                           'properties': {}},
                                       'url': {
                                           'type': 'string'}}}}
                },
                'parameters': [],
                'description': 'TODO'}
        },
        '/cache/{param1}': {
            'get': {
                'responses': {
                    '200': {
                        'description': 'TODO',
                        'schema': {
                            'additionalProperties': False,
                            'type': 'object',
                            'properties': {
                                'origin': {'type': 'string'},
                                'headers': {
                                    'additionalProperties': False,
                                    'type': 'object',
                                    'properties': {
                                        # 'Content-Length': {'type': 'string'},
                                        'Accept-Encoding': {'type': 'string'},
                                        'Connection': {'type': 'string'},
                                        'Accept': {'type': 'string'},
                                        'User-Agent': {'type': 'string'},
                                        'Host': {'type': 'string'}}
                                },
                                'args': {
                                    'additionalProperties': False,
                                    'type': 'object',
                                    'properties': {}},
                                'url': {'type': 'string'}}}
                    }
                },
                'parameters': [{
                    'required': True, 'type': 'string', 'name': 'param1', 'in': 'path'
                }],
                'description': 'TODO'}}}
    assert generator.generate_paths() == expected


def test_non_naive_path_params(httpbin):
    generator = Generator()
    response = requests.get(httpbin.url + '/basic-auth/1/pass', auth=('1', 'pass'))
    generator.provide_example(response.request, response)

    response = requests.get(httpbin.url + '/basic-auth/user/pass', auth=('user', 'pass'))
    generator.provide_example(response.request, response)

    expected = {
        '/basic-auth/{param1}/pass': {
            'get': {
                'responses': {
                    '200': {
                        'description': 'TODO',
                        'schema': {
                            'additionalProperties': False,
                            'type': 'object',
                            'properties': {
                                'authenticated': {'type': 'boolean'},
                                'user': {'type': 'string'}}}}},
                'parameters': [
                    {'required': True, 'type': 'string',
                     'name': 'param1', 'in': 'path'}],
                'description': 'TODO'}}}
    assert generator.generate_paths() == expected


def test_custom_path_params(httpbin):
    class CustomGenerator(Generator):
        def is_param(self, e, path):
            return e in {'user1', 'user2'} or super(CustomGenerator, self).is_param(e, path)

    generator = CustomGenerator()
    response = requests.get(httpbin.url + '/basic-auth/user1/pass', auth=('user1', 'pass'))
    generator.provide_example(response.request, response)

    response = requests.get(httpbin.url + '/basic-auth/user2/pass', auth=('user2', 'pass'))
    generator.provide_example(response.request, response)

    expected = {
        '/basic-auth/{param1}/pass': {
            'get': {
                'responses': {
                    '200': {
                        'description': 'TODO',
                        'schema': {
                            'additionalProperties': False,
                            'type': 'object',
                            'properties': {
                                'authenticated': {'type': 'boolean'},
                                'user': {'type': 'string'}}}}},
                'parameters': [
                    {'required': True, 'type': 'string',
                     'name': 'param1', 'in': 'path'}],
                'description': 'TODO'}}}
    assert generator.generate_paths() == expected


def test_base_path(httpbin):
    generator = Generator(base_path='/cache')
    response = requests.get(httpbin.url + '/cache/1')
    generator.provide_example(response.request, response)

    response = requests.get(httpbin.url + '/cache/2')
    generator.provide_example(response.request, response)

    expected = {
        '/{param1}': {
            'get': {
                'responses': {
                    '200': {
                        'description': 'TODO',
                        'schema': {
                            'additionalProperties': False, 'type': 'object',
                            'properties': {
                                'origin': {'type': 'string'},
                                'headers': {
                                    'additionalProperties': False, 'type': 'object',
                                    'properties': {
                                        # 'Content-Length': {'type': 'string'},
                                        'Accept-Encoding': {'type': 'string'},
                                        'Connection': {'type': 'string'},
                                        'Accept': {'type': 'string'},
                                        'User-Agent': {'type': 'string'},
                                        'Host': {'type': 'string'}}
                                },
                                'args': {
                                    'additionalProperties': False, 'type': 'object',
                                    'properties': {}}, 'url': {'type': 'string'}
                            }}}
                },
                'parameters': [
                    {
                        'required': True, 'type': 'string', 'name': 'param1',
                        'in': 'path'}],
                'description': 'TODO'}}}
    assert generator.generate_paths() == expected


def test_param_blacklist(httpbin):
    generator = Generator(query_key_blacklist={'token'})
    response = requests.get(httpbin.url + '/get', params={'token': '123'})
    generator.provide_example(response.request, response)

    expected = {
        '/get': {
            'get': {
                'responses': {
                    '200': {
                        'description': 'TODO',
                        'schema': {'additionalProperties': False,
                                   'type': 'object',
                                   'properties': {'origin': {
                                       'type': 'string'},
                                       'headers': {
                                           'additionalProperties': False,
                                           'type': 'object',
                                           'properties': {
                                               # 'Content-Length': {'type': 'string'},
                                               'Accept-Encoding': {'type': 'string'},
                                               'Connection': {'type': 'string'},
                                               'Accept': {'type': 'string'},
                                               'User-Agent': {'type': 'string'},
                                               'Host': {'type': 'string'}}},
                                       'args': {
                                           'additionalProperties': False,
                                           'type': 'object',
                                           'properties': {'token': {'type': 'string'}}
                                       },
                                       'url': {'type': 'string'}}}}
                },
                'parameters': [], 'description': 'TODO'}}}
    assert generator.generate_paths() == expected


def test_definition_matching(httpbin):
    existing_schema = {
        'definitions': {
            'Person': {
                'type': 'object',
                'properties': {
                    'name': {
                        'type': 'string',
                    },
                    'id': {
                        'type': 'integer',
                    }
                }
            }
        }
    }

    generator = Generator(existing_schema=existing_schema)
    response = requests.post(httpbin.url + '/post',
                             json=[{'name': 'foo', 'id': 1}, {'name': 'bar', 'id': 2}])
    generator.provide_example(response.request, response)

    expected = {
        '/post': {
            'post': {
                'responses': {
                    '200': {
                        'description': 'TODO',
                        'schema': {'$ref': '#/definitions/Person'}}
                },
                'parameters': [
                    {
                        'schema': {
                            'items': {
                                '$ref': '#/definitions/Person'
                            },
                            'type': 'array'},
                        'name': 'body_data', 'in': 'body'}], 'description': 'TODO'}}}
    assert generator.generate_paths() == expected


def test_subdefinition_matching(httpbin):
    existing_schema = {
        'definitions': {
            'Person': {
                'type': 'object',
                'additionalProperties': False,
                'properties': {
                    'name': {
                        '$ref': '#/definitions/Name',
                    }
                },
            },
            'Name': {
                'type': 'object',
                'additionalProperties': False,
                'properties': {
                    'first': {
                        type: 'string',
                    },
                    'last': {
                        type: 'string',
                    },
                }
            }
        }
    }

    generator = Generator(existing_schema=existing_schema)
    response = requests.post(httpbin.url + '/post', json={'name': {'first': 'foo', 'last': 'bar'}})
    generator.provide_example(response.request, response)

    expected = {
        '/post': {
            'post': {
                'responses': {
                    '200': {
                        'description': 'TODO',
                        'schema': {'additionalProperties': False,
                                   'type': 'object',
                                   'properties': {
                                       'files': {
                                           'additionalProperties': False,
                                           'type': 'object',
                                           'properties': {}},
                                       'origin': {'type': 'string'},
                                       'form': {
                                           'additionalProperties': False,
                                           'type': 'object',
                                           'properties': {}},
                                       'url': {'type': 'string'},
                                       'args': {
                                           'additionalProperties': False,
                                           'type': 'object',
                                           'properties': {}},
                                       'headers': {
                                           'additionalProperties': False,
                                           'type': 'object',
                                           'properties': {
                                               'Content-Length': {'type': 'string'},
                                               'Accept-Encoding': {'type': 'string'},
                                               'Connection': {'type': 'string'},
                                               'Accept': {'type': 'string'},
                                               'User-Agent': {'type': 'string'},
                                               'Host': {'type': 'string'},
                                               'Content-Type': {'type': 'string'}}},
                                       'json': {
                                           '$ref': '#/definitions/Person'},
                                       'data': {
                                           'type': 'string'}}}}},
                'parameters': [{'schema': {'$ref': '#/definitions/Person'},
                                'name': 'body_data', 'in': 'body'}],
                'description': 'TODO'}}}
    assert generator.generate_paths() == expected


def test_empty_array_with_valid_examples(httpbin):
    generator = Generator()
    response = requests.post(httpbin.url + '/post', json=[])
    generator.provide_example(response.request, response)

    response = requests.post(httpbin.url + '/post', json=[1, 2, 3])
    generator.provide_example(response.request, response)

    expected = {
        '/post': {
            'post': {
                'responses': {
                    '200': {
                        'description': 'TODO',
                        'schema': {
                            'additionalProperties': False,
                            'type': 'object',
                            'properties': {
                                'files': {
                                    'additionalProperties': False,
                                    'type': 'object',
                                    'properties': {}
                                },
                                'origin': {'type': 'string'},
                                'form': {
                                    'additionalProperties': False,
                                    'type': 'object',
                                    'properties': {}},
                                'url': {'type': 'string'},
                                'args': {
                                    'additionalProperties': False,
                                    'type': 'object',
                                    'properties': {}},
                                'headers': {
                                    'additionalProperties': False,
                                    'type': 'object',
                                    'properties': {
                                        'Content-Length': {'type': 'string'},
                                        'Accept-Encoding': {'type': 'string'},
                                        'Connection': {'type': 'string'},
                                        'Accept': {'type': 'string'},
                                        'User-Agent': {'type': 'string'},
                                        'Host': {'type': 'string'},
                                        'Content-Type': {'type': 'string'}}},
                                'json': {
                                    'items': {'type': 'number'},
                                    'type': 'array'
                                },
                                'data': {'type': 'string'}}}}
                },
                'parameters': [
                    {'schema': {'items': {'type': 'number'}, 'type': 'array'},
                     'name': 'body_data', 'in': 'body'}],
                'description': 'TODO'}}}
    assert generator.generate_paths() == expected


def test_empty_array_alone_ignored(httpbin):
    generator = Generator()
    response = requests.post(httpbin.url + '/post', json=[])
    generator.provide_example(response.request, response)

    expected = {'/post': {'post': {'responses': {}, 'parameters': [], 'description': 'TODO'}}}
    assert generator.generate_paths() == expected


def test_known_paths_ignored(httpbin):
    existing_schema = {
        'paths': {
            '/get': {
                'get': {}
            }
        }
    }
    generator = Generator(existing_schema=existing_schema)
    response = requests.get(httpbin.url + '/get')
    generator.provide_example(response.request, response)

    expected = {}
    assert generator.generate_paths() == expected


def test_example_str(httpbin):
    generator = Generator()
    response = requests.get(httpbin.url + '/get')
    generator.provide_example(response.request, response)
    assert str(generator.path_to_examples['/get'][0]) == "'get /get -> 200'"


def test_get_yaml(httpbin):
    generator = Generator()
    response = requests.post(httpbin.url + '/post', json=[])
    generator.provide_example(response.request, response)

    expected = {'/post': {'post': {'responses': {}, 'parameters': [], 'description': 'TODO'}}}
    schemas = generator.generate_paths()
    assert schemas == expected

    expected_yaml = """  /post:
    post:
      description: TODO
      parameters: []
      responses: {}
  """

    assert get_yaml(schemas) == expected_yaml


def test_provided_default(httpbin):
    generator = Generator(
        default={'description': 'unexpected error', 'schema': {'$ref': '#/definitions/Error'}})
    response = requests.post(httpbin.url + '/get', json=[])
    generator.provide_example(response.request, response)

    expected = {'/get': {'post': {'responses': {
        'default': {'description': 'unexpected error',
                    'schema': {'$ref': '#/definitions/Error'}}},
        'description': 'TODO'}}}
    assert generator.generate_paths() == expected


def test_optional_field_nonempty_example(httpbin):
    generator = Generator()
    response = requests.post(httpbin.url + '/post', json={'parent': {'other': True}})
    generator.provide_example(response.request, response)

    response = requests.post(httpbin.url + '/post',
                             json={'parent': {'optional': True, 'other': True}})
    generator.provide_example(response.request, response)

    expected = {
        '/post': {
            'post': {
                'responses': {
                    '200': {
                        'description': 'TODO',
                        'schema': {
                            'additionalProperties': False,
                            'type': 'object',
                            'properties': {'files': {
                                'additionalProperties': False,
                                'type': 'object',
                                'properties': {}},
                                'origin': {
                                    'type': 'string'},
                                'form': {
                                    'additionalProperties': False,
                                    'type': 'object',
                                    'properties': {}},
                                'url': {
                                    'type': 'string'},
                                'args': {
                                    'additionalProperties': False,
                                    'type': 'object',
                                    'properties': {}},
                                'headers': {
                                    'additionalProperties': False,
                                    'type': 'object',
                                    'properties': {
                                        'Content-Length': {'type': 'string'},
                                        'Accept-Encoding': {'type': 'string'},
                                        'Connection': {'type': 'string'},
                                        'Accept': {'type': 'string'},
                                        'User-Agent': {'type': 'string'},
                                        'Host': {'type': 'string'},
                                        'Content-Type': {'type': 'string'}}},
                                'json': {
                                    'additionalProperties': False,
                                    'type': 'object',
                                    'properties': {
                                        'parent': {
                                            'additionalProperties': False,
                                            'type': 'object',
                                            'properties': {
                                                'other': {'type': 'boolean'},
                                                'optional': {'type': 'boolean'}}
                                        }
                                    }
                                },
                                'data': {
                                    'type': 'string'}}}}},
                'parameters': [
                    {
                        'schema': {
                            'additionalProperties': False,
                            'type': 'object',
                            'properties': {
                                'parent': {
                                    'additionalProperties': False,
                                    'type': 'object',
                                    'properties': {
                                        'other': {'type': 'boolean'},
                                        'optional': {'type': 'boolean'}}}}
                        },
                        'name': 'body_data', 'in': 'body'}],
                'description': 'TODO'}}}
    assert generator.generate_paths() == expected


if __name__ == '__main__':
    pytest.main()
