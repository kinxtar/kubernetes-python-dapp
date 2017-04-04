# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1Capabilities(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, add=None, drop=None):
        """
        V1Capabilities - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'add': 'list[str]',
            'drop': 'list[str]'
        }

        self.attribute_map = {
            'add': 'add',
            'drop': 'drop'
        }

        self._add = add
        self._drop = drop

    @property
    def add(self):
        """
        Gets the add of this V1Capabilities.
        Added capabilities

        :return: The add of this V1Capabilities.
        :rtype: list[str]
        """
        return self._add

    @add.setter
    def add(self, add):
        """
        Sets the add of this V1Capabilities.
        Added capabilities

        :param add: The add of this V1Capabilities.
        :type: list[str]
        """

        self._add = add

    @property
    def drop(self):
        """
        Gets the drop of this V1Capabilities.
        Removed capabilities

        :return: The drop of this V1Capabilities.
        :rtype: list[str]
        """
        return self._drop

    @drop.setter
    def drop(self, drop):
        """
        Sets the drop of this V1Capabilities.
        Removed capabilities

        :param drop: The drop of this V1Capabilities.
        :type: list[str]
        """

        self._drop = drop

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
