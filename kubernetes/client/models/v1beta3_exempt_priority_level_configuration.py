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


class V1beta3ExemptPriorityLevelConfiguration(object):
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
        'lendable_percent': 'int',
        'nominal_concurrency_shares': 'int'
    }

    attribute_map = {
        'lendable_percent': 'lendablePercent',
        'nominal_concurrency_shares': 'nominalConcurrencyShares'
    }

    def __init__(self, lendable_percent=None, nominal_concurrency_shares=None, local_vars_configuration=None):  # noqa: E501
        """V1beta3ExemptPriorityLevelConfiguration - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._lendable_percent = None
        self._nominal_concurrency_shares = None
        self.discriminator = None

        if lendable_percent is not None:
            self.lendable_percent = lendable_percent
        if nominal_concurrency_shares is not None:
            self.nominal_concurrency_shares = nominal_concurrency_shares

    @property
    def lendable_percent(self):
        """Gets the lendable_percent of this V1beta3ExemptPriorityLevelConfiguration.  # noqa: E501

        `lendablePercent` prescribes the fraction of the level's NominalCL that can be borrowed by other priority levels.  This value of this field must be between 0 and 100, inclusive, and it defaults to 0. The number of seats that other levels can borrow from this level, known as this level's LendableConcurrencyLimit (LendableCL), is defined as follows.  LendableCL(i) = round( NominalCL(i) * lendablePercent(i)/100.0 )  # noqa: E501

        :return: The lendable_percent of this V1beta3ExemptPriorityLevelConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._lendable_percent

    @lendable_percent.setter
    def lendable_percent(self, lendable_percent):
        """Sets the lendable_percent of this V1beta3ExemptPriorityLevelConfiguration.

        `lendablePercent` prescribes the fraction of the level's NominalCL that can be borrowed by other priority levels.  This value of this field must be between 0 and 100, inclusive, and it defaults to 0. The number of seats that other levels can borrow from this level, known as this level's LendableConcurrencyLimit (LendableCL), is defined as follows.  LendableCL(i) = round( NominalCL(i) * lendablePercent(i)/100.0 )  # noqa: E501

        :param lendable_percent: The lendable_percent of this V1beta3ExemptPriorityLevelConfiguration.  # noqa: E501
        :type: int
        """

        self._lendable_percent = lendable_percent

    @property
    def nominal_concurrency_shares(self):
        """Gets the nominal_concurrency_shares of this V1beta3ExemptPriorityLevelConfiguration.  # noqa: E501

        `nominalConcurrencyShares` (NCS) contributes to the computation of the NominalConcurrencyLimit (NominalCL) of this level. This is the number of execution seats nominally reserved for this priority level. This DOES NOT limit the dispatching from this priority level but affects the other priority levels through the borrowing mechanism. The server's concurrency limit (ServerCL) is divided among all the priority levels in proportion to their NCS values:  NominalCL(i)  = ceil( ServerCL * NCS(i) / sum_ncs ) sum_ncs = sum[priority level k] NCS(k)  Bigger numbers mean a larger nominal concurrency limit, at the expense of every other priority level. This field has a default value of zero.  # noqa: E501

        :return: The nominal_concurrency_shares of this V1beta3ExemptPriorityLevelConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._nominal_concurrency_shares

    @nominal_concurrency_shares.setter
    def nominal_concurrency_shares(self, nominal_concurrency_shares):
        """Sets the nominal_concurrency_shares of this V1beta3ExemptPriorityLevelConfiguration.

        `nominalConcurrencyShares` (NCS) contributes to the computation of the NominalConcurrencyLimit (NominalCL) of this level. This is the number of execution seats nominally reserved for this priority level. This DOES NOT limit the dispatching from this priority level but affects the other priority levels through the borrowing mechanism. The server's concurrency limit (ServerCL) is divided among all the priority levels in proportion to their NCS values:  NominalCL(i)  = ceil( ServerCL * NCS(i) / sum_ncs ) sum_ncs = sum[priority level k] NCS(k)  Bigger numbers mean a larger nominal concurrency limit, at the expense of every other priority level. This field has a default value of zero.  # noqa: E501

        :param nominal_concurrency_shares: The nominal_concurrency_shares of this V1beta3ExemptPriorityLevelConfiguration.  # noqa: E501
        :type: int
        """

        self._nominal_concurrency_shares = nominal_concurrency_shares

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
        if not isinstance(other, V1beta3ExemptPriorityLevelConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta3ExemptPriorityLevelConfiguration):
            return True

        return self.to_dict() != other.to_dict()
