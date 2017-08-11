# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1beta1NonResourceAttributes(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, path=None, verb=None):
        """
        V1beta1NonResourceAttributes - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'path': 'str',
            'verb': 'str'
        }

        self.attribute_map = {
            'path': 'path',
            'verb': 'verb'
        }

        self._path = path
        self._verb = verb

    @property
    def path(self):
        """
        Gets the path of this V1beta1NonResourceAttributes.
        Path is the URL path of the request

        :return: The path of this V1beta1NonResourceAttributes.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this V1beta1NonResourceAttributes.
        Path is the URL path of the request

        :param path: The path of this V1beta1NonResourceAttributes.
        :type: str
        """

        self._path = path

    @property
    def verb(self):
        """
        Gets the verb of this V1beta1NonResourceAttributes.
        Verb is the standard HTTP verb

        :return: The verb of this V1beta1NonResourceAttributes.
        :rtype: str
        """
        return self._verb

    @verb.setter
    def verb(self, verb):
        """
        Sets the verb of this V1beta1NonResourceAttributes.
        Verb is the standard HTTP verb

        :param verb: The verb of this V1beta1NonResourceAttributes.
        :type: str
        """

        self._verb = verb

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1beta1NonResourceAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
