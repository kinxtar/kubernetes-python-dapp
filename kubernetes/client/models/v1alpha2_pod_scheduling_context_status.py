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


class V1alpha2PodSchedulingContextStatus(object):
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
        'resource_claims': 'list[V1alpha2ResourceClaimSchedulingStatus]'
    }

    attribute_map = {
        'resource_claims': 'resourceClaims'
    }

    def __init__(self, resource_claims=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha2PodSchedulingContextStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._resource_claims = None
        self.discriminator = None

        if resource_claims is not None:
            self.resource_claims = resource_claims

    @property
    def resource_claims(self):
        """Gets the resource_claims of this V1alpha2PodSchedulingContextStatus.  # noqa: E501

        ResourceClaims describes resource availability for each pod.spec.resourceClaim entry where the corresponding ResourceClaim uses \"WaitForFirstConsumer\" allocation mode.  # noqa: E501

        :return: The resource_claims of this V1alpha2PodSchedulingContextStatus.  # noqa: E501
        :rtype: list[V1alpha2ResourceClaimSchedulingStatus]
        """
        return self._resource_claims

    @resource_claims.setter
    def resource_claims(self, resource_claims):
        """Sets the resource_claims of this V1alpha2PodSchedulingContextStatus.

        ResourceClaims describes resource availability for each pod.spec.resourceClaim entry where the corresponding ResourceClaim uses \"WaitForFirstConsumer\" allocation mode.  # noqa: E501

        :param resource_claims: The resource_claims of this V1alpha2PodSchedulingContextStatus.  # noqa: E501
        :type: list[V1alpha2ResourceClaimSchedulingStatus]
        """

        self._resource_claims = resource_claims

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
        if not isinstance(other, V1alpha2PodSchedulingContextStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha2PodSchedulingContextStatus):
            return True

        return self.to_dict() != other.to_dict()
