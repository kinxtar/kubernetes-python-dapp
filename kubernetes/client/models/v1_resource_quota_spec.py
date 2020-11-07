# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.17
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1ResourceQuotaSpec(object):
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
        'hard': 'dict(str, str)',
        'scope_selector': 'V1ScopeSelector',
        'scopes': 'list[str]'
    }

    attribute_map = {
        'hard': 'hard',
        'scope_selector': 'scopeSelector',
        'scopes': 'scopes'
    }

    def __init__(self, hard=None, scope_selector=None, scopes=None, local_vars_configuration=None):  # noqa: E501
        """V1ResourceQuotaSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._hard = None
        self._scope_selector = None
        self._scopes = None
        self.discriminator = None

        if hard is not None:
            self.hard = hard
        if scope_selector is not None:
            self.scope_selector = scope_selector
        if scopes is not None:
            self.scopes = scopes

    @property
    def hard(self):
        """Gets the hard of this V1ResourceQuotaSpec.  # noqa: E501

        hard is the set of desired hard limits for each named resource. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/  # noqa: E501

        :return: The hard of this V1ResourceQuotaSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._hard

    @hard.setter
    def hard(self, hard):
        """Sets the hard of this V1ResourceQuotaSpec.

        hard is the set of desired hard limits for each named resource. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/  # noqa: E501

        :param hard: The hard of this V1ResourceQuotaSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._hard = hard

    @property
    def scope_selector(self):
        """Gets the scope_selector of this V1ResourceQuotaSpec.  # noqa: E501


        :return: The scope_selector of this V1ResourceQuotaSpec.  # noqa: E501
        :rtype: V1ScopeSelector
        """
        return self._scope_selector

    @scope_selector.setter
    def scope_selector(self, scope_selector):
        """Sets the scope_selector of this V1ResourceQuotaSpec.


        :param scope_selector: The scope_selector of this V1ResourceQuotaSpec.  # noqa: E501
        :type: V1ScopeSelector
        """

        self._scope_selector = scope_selector

    @property
    def scopes(self):
        """Gets the scopes of this V1ResourceQuotaSpec.  # noqa: E501

        A collection of filters that must match each object tracked by a quota. If not specified, the quota matches all objects.  # noqa: E501

        :return: The scopes of this V1ResourceQuotaSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this V1ResourceQuotaSpec.

        A collection of filters that must match each object tracked by a quota. If not specified, the quota matches all objects.  # noqa: E501

        :param scopes: The scopes of this V1ResourceQuotaSpec.  # noqa: E501
        :type: list[str]
        """

        self._scopes = scopes

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
        if not isinstance(other, V1ResourceQuotaSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ResourceQuotaSpec):
            return True

        return self.to_dict() != other.to_dict()
