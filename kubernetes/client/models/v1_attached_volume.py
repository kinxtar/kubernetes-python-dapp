# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.12.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1AttachedVolume(object):
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
        'device_path': 'str',
        'name': 'str'
    }

    attribute_map = {
        'device_path': 'devicePath',
        'name': 'name'
    }

    def __init__(self, device_path=None, name=None):
        """
        V1AttachedVolume - a model defined in Swagger
        """

        self._device_path = None
        self._name = None
        self.discriminator = None

        self.device_path = device_path
        self.name = name

    @property
    def device_path(self):
        """
        Gets the device_path of this V1AttachedVolume.
        DevicePath represents the device path where the volume should be available

        :return: The device_path of this V1AttachedVolume.
        :rtype: str
        """
        return self._device_path

    @device_path.setter
    def device_path(self, device_path):
        """
        Sets the device_path of this V1AttachedVolume.
        DevicePath represents the device path where the volume should be available

        :param device_path: The device_path of this V1AttachedVolume.
        :type: str
        """
        if device_path is None:
            raise ValueError("Invalid value for `device_path`, must not be `None`")

        self._device_path = device_path

    @property
    def name(self):
        """
        Gets the name of this V1AttachedVolume.
        Name of the attached volume

        :return: The name of this V1AttachedVolume.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1AttachedVolume.
        Name of the attached volume

        :param name: The name of this V1AttachedVolume.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

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
        if not isinstance(other, V1AttachedVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
