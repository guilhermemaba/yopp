# -*- coding: utf8 -*-
# vim: ts=4 sts=4 sw=4 et:

import mimetypes
import yaml
import os
from collections import MutableMapping
from constants import YAML_MIME_TYPES
from element_parser import ElementParser

__all__ = ['YAMLParserException', 'YAMLDoesNotExistException', 'YAMLNotDefinedException', 'YAMLParser']


class YAMLParserException(Exception):
    pass


class YAMLDoesNotExistException(YAMLParserException):
    pass


class YAMLNotDefinedException(YAMLParserException):
    pass


class YAMLParser(MutableMapping):

    def __init__(self, yaml_path, *args, **kwargs):
        self.store = dict()
        self.yaml_path = yaml_path
        self._load_data()
        self.update(*args, **kwargs)

    def __getitem__(self, key):
        return self.store[key]

    def __setitem__(self, key, value):
        if isinstance(value, ElementParser):
            # call function action
            self.store[key] = value.action(value.data)
        else:
            self.store[key] = value

    def __delitem__(self, key):
        del self.store[key]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

    def _get_data_yaml(self):
        if not self.yaml_path:
            raise YAMLNotDefinedException('yaml_path is not defined!')
        if not os.path.isfile(self.yaml_path):
            raise YAMLDoesNotExistException('file {} does not exists!'.format(self.yaml_path))
        mime_type = _get_mime_type(self.yaml_path)
        if _is_mime_type_yaml(mime_type):
            arquive = open(self.yaml_path, 'rb')
            return arquive.read()
        return {}

    def _parse_yaml(self):
        return yaml.load(self._get_data_yaml())

    def _load_data(self):
        '''
        Load file yaml and set data in object
        '''
        data = self._parse_yaml()
        if isinstance(data, dict):
            self.update(data)
        else:
            data = {index: data_dict for index, data_dict in enumerate(data)}
            self.update(data)


def _is_mime_type_yaml(mime_type):
    if mime_type:
        return mime_type.lower() in YAML_MIME_TYPES


def _get_mime_type(arquive):
    return mimetypes.guess_type(arquive)[0]


for mimetype in YAML_MIME_TYPES:
    mimetypes.add_type(mimetype, ".yaml")
