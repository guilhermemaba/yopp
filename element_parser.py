# -*- coding: utf8 -*-
# vim: ts=4 sts=4 sw=4 et:

import yaml


class ElementParser(yaml.YAMLObject):

    def __init__(self, data):
        self.data = data

    @classmethod
    def loader(cls, loader, node):
        value = loader.construct_scalar(node)
        return cls(value)

    @classmethod
    def representer(cls, dumper, data):
        return dumper.represent_scalar(cls.yaml_tag, u' ', + data)

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self.data)

    @classmethod
    def action(cls, value):
        return value


class ModelElementParser(ElementParser):
    yaml_tag = u'!gimme_model'

    @classmethod
    def action(cls, value):
        # TODO example for implement custom action
        return u'Model-{}'.format(value)


class FormElementParser(ElementParser):
    yaml_tag = u'!gimme_form'

    @classmethod
    def action(cls, value):
        # TODO example for implement custom action
        return u'Form-{}'.format(value)


def register_element(element):
    yaml.add_representer(element, element.representer)
    yaml.add_constructor(element.yaml_tag, element.loader)

register_element(ModelElementParser)
register_element(FormElementParser)
