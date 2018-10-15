# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.12.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1ScopedResourceSelectorRequirement(object):
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
        'operator': 'str',
        'scope_name': 'str',
        'values': 'list[str]'
    }

    attribute_map = {
        'operator': 'operator',
        'scope_name': 'scopeName',
        'values': 'values'
    }

    def __init__(self, operator=None, scope_name=None, values=None):
        """
        V1ScopedResourceSelectorRequirement - a model defined in Swagger
        """

        self._operator = None
        self._scope_name = None
        self._values = None
        self.discriminator = None

        self.operator = operator
        self.scope_name = scope_name
        if values is not None:
          self.values = values

    @property
    def operator(self):
        """
        Gets the operator of this V1ScopedResourceSelectorRequirement.
        Represents a scope's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist.

        :return: The operator of this V1ScopedResourceSelectorRequirement.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """
        Sets the operator of this V1ScopedResourceSelectorRequirement.
        Represents a scope's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist.

        :param operator: The operator of this V1ScopedResourceSelectorRequirement.
        :type: str
        """
        if operator is None:
            raise ValueError("Invalid value for `operator`, must not be `None`")

        self._operator = operator

    @property
    def scope_name(self):
        """
        Gets the scope_name of this V1ScopedResourceSelectorRequirement.
        The name of the scope that the selector applies to.

        :return: The scope_name of this V1ScopedResourceSelectorRequirement.
        :rtype: str
        """
        return self._scope_name

    @scope_name.setter
    def scope_name(self, scope_name):
        """
        Sets the scope_name of this V1ScopedResourceSelectorRequirement.
        The name of the scope that the selector applies to.

        :param scope_name: The scope_name of this V1ScopedResourceSelectorRequirement.
        :type: str
        """
        if scope_name is None:
            raise ValueError("Invalid value for `scope_name`, must not be `None`")

        self._scope_name = scope_name

    @property
    def values(self):
        """
        Gets the values of this V1ScopedResourceSelectorRequirement.
        An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

        :return: The values of this V1ScopedResourceSelectorRequirement.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this V1ScopedResourceSelectorRequirement.
        An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

        :param values: The values of this V1ScopedResourceSelectorRequirement.
        :type: list[str]
        """

        self._values = values

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
        if not isinstance(other, V1ScopedResourceSelectorRequirement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
