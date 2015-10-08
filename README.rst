===============================
yopp (YAML Object Python Parser)
===============================

.. image:: https://img.shields.io/travis/guilhermemaba/yopp.svg
        :target: https://travis-ci.org/guilhermemaba/yopp

.. image:: https://img.shields.io/pypi/v/yopp.svg
        :target: https://pypi.python.org/pypi/yopp


Transforms YAML file to python objects using a custom parser
Thanks for the code pyraml-parser: https://github.com/an2deg/pyraml-parser

* Free software: ISC license
* Documentation: https://yopp.readthedocs.org.

Quickstart
----------

Install YOPP::

    pip install yopp

Then use it in a project::

    from yopp.yaml_parser import YAMLParser
    
    yaml_parser = YAMLParser('schema.yaml')

It's possible create yours ElementParser e yaml_tag with custom action::

    from yopp.element_parser import ElementParser, register


    class ModelElementParser(ElementParser):
        yaml_tag = u'!gimme_model'

        @classmethod
        def action(cls, value):
            # TODO example for implement custom action
            return u'Model-{}'.format(value)
    
    
    register_element(ModelElementParser)


Features
--------

* TODO
