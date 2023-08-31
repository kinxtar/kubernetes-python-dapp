# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.28
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1LimitRangeItem(object):
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
        'default': 'dict(str, str)',
        'default_request': 'dict(str, str)',
        'max': 'dict(str, str)',
        'max_limit_request_ratio': 'dict(str, str)',
        'min': 'dict(str, str)',
        'type': 'str'
    }

    attribute_map = {
        'default': 'default',
        'default_request': 'defaultRequest',
        'max': 'max',
        'max_limit_request_ratio': 'maxLimitRequestRatio',
        'min': 'min',
        'type': 'type'
    }

    def __init__(self, default=None, default_request=None, max=None, max_limit_request_ratio=None, min=None, type=None, local_vars_configuration=None):  # noqa: E501
        """V1LimitRangeItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._default = None
        self._default_request = None
        self._max = None
        self._max_limit_request_ratio = None
        self._min = None
        self._type = None
        self.discriminator = None

        if default is not None:
            self.default = default
        if default_request is not None:
            self.default_request = default_request
        if max is not None:
            self.max = max
        if max_limit_request_ratio is not None:
            self.max_limit_request_ratio = max_limit_request_ratio
        if min is not None:
            self.min = min
        self.type = type

    @property
    def default(self):
        """Gets the default of this V1LimitRangeItem.  # noqa: E501

        Default resource requirement limit value by resource name if resource limit is omitted.  # noqa: E501

        :return: The default of this V1LimitRangeItem.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this V1LimitRangeItem.

        Default resource requirement limit value by resource name if resource limit is omitted.  # noqa: E501

        :param default: The default of this V1LimitRangeItem.  # noqa: E501
        :type: dict(str, str)
        """

        self._default = default

    @property
    def default_request(self):
        """Gets the default_request of this V1LimitRangeItem.  # noqa: E501

        DefaultRequest is the default resource requirement request value by resource name if resource request is omitted.  # noqa: E501

        :return: The default_request of this V1LimitRangeItem.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._default_request

    @default_request.setter
    def default_request(self, default_request):
        """Sets the default_request of this V1LimitRangeItem.

        DefaultRequest is the default resource requirement request value by resource name if resource request is omitted.  # noqa: E501

        :param default_request: The default_request of this V1LimitRangeItem.  # noqa: E501
        :type: dict(str, str)
        """

        self._default_request = default_request

    @property
    def max(self):
        """Gets the max of this V1LimitRangeItem.  # noqa: E501

        Max usage constraints on this kind by resource name.  # noqa: E501

        :return: The max of this V1LimitRangeItem.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this V1LimitRangeItem.

        Max usage constraints on this kind by resource name.  # noqa: E501

        :param max: The max of this V1LimitRangeItem.  # noqa: E501
        :type: dict(str, str)
        """

        self._max = max

    @property
    def max_limit_request_ratio(self):
        """Gets the max_limit_request_ratio of this V1LimitRangeItem.  # noqa: E501

        MaxLimitRequestRatio if specified, the named resource must have a request and limit that are both non-zero where limit divided by request is less than or equal to the enumerated value; this represents the max burst for the named resource.  # noqa: E501

        :return: The max_limit_request_ratio of this V1LimitRangeItem.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._max_limit_request_ratio

    @max_limit_request_ratio.setter
    def max_limit_request_ratio(self, max_limit_request_ratio):
        """Sets the max_limit_request_ratio of this V1LimitRangeItem.

        MaxLimitRequestRatio if specified, the named resource must have a request and limit that are both non-zero where limit divided by request is less than or equal to the enumerated value; this represents the max burst for the named resource.  # noqa: E501

        :param max_limit_request_ratio: The max_limit_request_ratio of this V1LimitRangeItem.  # noqa: E501
        :type: dict(str, str)
        """

        self._max_limit_request_ratio = max_limit_request_ratio

    @property
    def min(self):
        """Gets the min of this V1LimitRangeItem.  # noqa: E501

        Min usage constraints on this kind by resource name.  # noqa: E501

        :return: The min of this V1LimitRangeItem.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this V1LimitRangeItem.

        Min usage constraints on this kind by resource name.  # noqa: E501

        :param min: The min of this V1LimitRangeItem.  # noqa: E501
        :type: dict(str, str)
        """

        self._min = min

    @property
    def type(self):
        """Gets the type of this V1LimitRangeItem.  # noqa: E501

        Type of resource that this limit applies to.  # noqa: E501

        :return: The type of this V1LimitRangeItem.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1LimitRangeItem.

        Type of resource that this limit applies to.  # noqa: E501

        :param type: The type of this V1LimitRangeItem.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, V1LimitRangeItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1LimitRangeItem):
            return True

        return self.to_dict() != other.to_dict()
