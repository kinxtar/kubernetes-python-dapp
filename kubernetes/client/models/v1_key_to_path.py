# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1KeyToPath(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, key=None, mode=None, path=None):
        """
        V1KeyToPath - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'key': 'str',
            'mode': 'int',
            'path': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'mode': 'mode',
            'path': 'path'
        }

        self._key = key
        self._mode = mode
        self._path = path

    @property
    def key(self):
        """
        Gets the key of this V1KeyToPath.
        The key to project.

        :return: The key of this V1KeyToPath.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this V1KeyToPath.
        The key to project.

        :param key: The key of this V1KeyToPath.
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")

        self._key = key

    @property
    def mode(self):
        """
        Gets the mode of this V1KeyToPath.
        Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.

        :return: The mode of this V1KeyToPath.
        :rtype: int
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """
        Sets the mode of this V1KeyToPath.
        Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.

        :param mode: The mode of this V1KeyToPath.
        :type: int
        """

        self._mode = mode

    @property
    def path(self):
        """
        Gets the path of this V1KeyToPath.
        The relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.

        :return: The path of this V1KeyToPath.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this V1KeyToPath.
        The relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.

        :param path: The path of this V1KeyToPath.
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")

        self._path = path

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
        if not isinstance(other, V1KeyToPath):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
