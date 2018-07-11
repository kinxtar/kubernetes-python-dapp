# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.11.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1NodeConfigSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'config_map': 'V1ConfigMapNodeConfigSource'
    }

    attribute_map = {
        'config_map': 'configMap'
    }

    def __init__(self, config_map=None):
        """
        V1NodeConfigSource - a model defined in Swagger
        """

        self._config_map = None
        self.discriminator = None

        if config_map is not None:
          self.config_map = config_map

    @property
    def config_map(self):
        """
        Gets the config_map of this V1NodeConfigSource.
        ConfigMap is a reference to a Node's ConfigMap

        :return: The config_map of this V1NodeConfigSource.
        :rtype: V1ConfigMapNodeConfigSource
        """
        return self._config_map

    @config_map.setter
    def config_map(self, config_map):
        """
        Sets the config_map of this V1NodeConfigSource.
        ConfigMap is a reference to a Node's ConfigMap

        :param config_map: The config_map of this V1NodeConfigSource.
        :type: V1ConfigMapNodeConfigSource
        """

        self._config_map = config_map

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
        if not isinstance(other, V1NodeConfigSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
