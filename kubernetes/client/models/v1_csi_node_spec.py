# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.27
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1CSINodeSpec(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'drivers': 'list[V1CSINodeDriver]'
    }

    attribute_map = {
        'drivers': 'drivers'
    }

    def __init__(self, drivers=None, local_vars_configuration=None):  # noqa: E501
        """V1CSINodeSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._drivers = None
        self.discriminator = None

        self.drivers = drivers

    @property
    def drivers(self):
        """Gets the drivers of this V1CSINodeSpec.  # noqa: E501

        drivers is a list of information of all CSI Drivers existing on a node. If all drivers in the list are uninstalled, this can become empty.  # noqa: E501

        :return: The drivers of this V1CSINodeSpec.  # noqa: E501
        :rtype: list[V1CSINodeDriver]
        """
        return self._drivers

    @drivers.setter
    def drivers(self, drivers):
        """Sets the drivers of this V1CSINodeSpec.

        drivers is a list of information of all CSI Drivers existing on a node. If all drivers in the list are uninstalled, this can become empty.  # noqa: E501

        :param drivers: The drivers of this V1CSINodeSpec.  # noqa: E501
        :type: list[V1CSINodeDriver]
        """
        if self.local_vars_configuration.client_side_validation and drivers is None:  # noqa: E501
            raise ValueError("Invalid value for `drivers`, must not be `None`")  # noqa: E501

        self._drivers = drivers

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1CSINodeSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1CSINodeSpec):
            return True

        return self.to_dict() != other.to_dict()
