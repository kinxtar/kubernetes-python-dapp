# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1SecretKeySelector(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, key=None, name=None, optional=None):
        """
        V1SecretKeySelector - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'key': 'str',
            'name': 'str',
            'optional': 'bool'
        }

        self.attribute_map = {
            'key': 'key',
            'name': 'name',
            'optional': 'optional'
        }

        self._key = key
        self._name = name
        self._optional = optional

    @property
    def key(self):
        """
        Gets the key of this V1SecretKeySelector.
        The key of the secret to select from.  Must be a valid secret key.

        :return: The key of this V1SecretKeySelector.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this V1SecretKeySelector.
        The key of the secret to select from.  Must be a valid secret key.

        :param key: The key of this V1SecretKeySelector.
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")

        self._key = key

    @property
    def name(self):
        """
        Gets the name of this V1SecretKeySelector.
        Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names

        :return: The name of this V1SecretKeySelector.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1SecretKeySelector.
        Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names

        :param name: The name of this V1SecretKeySelector.
        :type: str
        """

        self._name = name

    @property
    def optional(self):
        """
        Gets the optional of this V1SecretKeySelector.
        Specify whether the Secret or it's key must be defined

        :return: The optional of this V1SecretKeySelector.
        :rtype: bool
        """
        return self._optional

    @optional.setter
    def optional(self, optional):
        """
        Sets the optional of this V1SecretKeySelector.
        Specify whether the Secret or it's key must be defined

        :param optional: The optional of this V1SecretKeySelector.
        :type: bool
        """

        self._optional = optional

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
        if not isinstance(other, V1SecretKeySelector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
