import abc
import json
import xml.etree.ElementTree as et

import yaml

import serializers


class Serializer(metaclass=abc.ABCMeta):
    """
    Base Serializer Class
    """

    def __init__(self):
        pass

    def start_object(self, object_name, object_id):
        pass

    def add_property(self, name, value):
        pass

    def to_str(self):
        pass


class JsonSerializer(Serializer):
    """
    A class which serialize an object to JSON format
    """

    def __init__(self):
        self._current_object = None

    def start_object(self, object_name, object_id):
        self._current_object = {
            'id': object_id
        }

    def add_property(self, name, value):
        self._current_object[name] = value

    def to_str(self):
        return json.dumps(self._current_object)


class XmlSerializer(Serializer):
    """
    A class which serialize an object to XML format
    """

    def __init__(self):
        self._element = None

    def start_object(self, object_name, object_id):
        self._element = et.Element(object_name,
                                   attrib={'id': object_id})

    def add_property(self, name, value):
        prop = et.SubElement(self._element, name)
        prop.text = value

    def to_str(self):
        return et.tostring(self._element, encoding='unicode')


class YamlSerializer(serializers.JsonSerializer):
    """
    A class which serialize an object to YAML format
    - inherits from `JsonSerializer`
    - overrides `to_str` method
    """

    def to_str(self):
        return yaml.dump(self._current_object)


class ObjectSerializer:
    """
    A generic class to handle a serializable objects and serializers
    """

    def serialize(self, serializable: object, format):
        serializer = factory.get_serializer(format)
        serializable.serialize(serializer)
        return serializer.to_str()


class SerializerFactory:
    """
    A factory class for Serializers
    - register and returns a serializer instance
    """

    def __init__(self):
        self._creators = {}

    def register_format(self, format, creator):
        # TODO: update creator
        self._creators[format] = creator

    def get_serializer(self, format):
        creator = self._creators.get(format)
        if not creator:
            raise ValueError(format)
        return creator()


factory = SerializerFactory()
factory.register_format('JSON', JsonSerializer)
factory.register_format('XML', XmlSerializer)
factory.register_format('YAML', YamlSerializer)


if __name__ == "__main__":
    from book import Book
    book = Book('1', 'Water of Love', 'Dire Straits')
    serializer = serializers.ObjectSerializer()

    print(serializer.serialize(book, 'JSON'))
    print(serializer.serialize(book, 'XML'))
    print(serializer.serialize(book, 'YAML'))

    # JSON:
    #   {"id": "1", "title": "Water of Love", "artist": "Dire Straits"}
    # XML:
    #   <song id="1"><title>Water of Love</title><artist>Dire Straits</artist></song>
    # YAML:
    #   {artist: Dire Straits, id: '1', title: Water of Love}
