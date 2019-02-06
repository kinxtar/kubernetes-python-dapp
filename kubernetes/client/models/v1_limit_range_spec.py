# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.13.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1LimitRangeSpec(object):
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
        'limits': 'list[V1LimitRangeItem]'
    }

    attribute_map = {
        'limits': 'limits'
    }

    def __init__(self, limits=None):
        """
        V1LimitRangeSpec - a model defined in Swagger
        """

        self._limits = None
        self.discriminator = None

        self.limits = limits

    @property
    def limits(self):
        """
        Gets the limits of this V1LimitRangeSpec.
        Limits is the list of LimitRangeItem objects that are enforced.

        :return: The limits of this V1LimitRangeSpec.
        :rtype: list[V1LimitRangeItem]
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """
        Sets the limits of this V1LimitRangeSpec.
        Limits is the list of LimitRangeItem objects that are enforced.

        :param limits: The limits of this V1LimitRangeSpec.
        :type: list[V1LimitRangeItem]
        """
        if limits is None:
            raise ValueError("Invalid value for `limits`, must not be `None`")

        self._limits = limits

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
        if not isinstance(other, V1LimitRangeSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
