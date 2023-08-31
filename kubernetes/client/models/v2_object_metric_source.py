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


class V2ObjectMetricSource(object):
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
        'described_object': 'V2CrossVersionObjectReference',
        'metric': 'V2MetricIdentifier',
        'target': 'V2MetricTarget'
    }

    attribute_map = {
        'described_object': 'describedObject',
        'metric': 'metric',
        'target': 'target'
    }

    def __init__(self, described_object=None, metric=None, target=None, local_vars_configuration=None):  # noqa: E501
        """V2ObjectMetricSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._described_object = None
        self._metric = None
        self._target = None
        self.discriminator = None

        self.described_object = described_object
        self.metric = metric
        self.target = target

    @property
    def described_object(self):
        """Gets the described_object of this V2ObjectMetricSource.  # noqa: E501


        :return: The described_object of this V2ObjectMetricSource.  # noqa: E501
        :rtype: V2CrossVersionObjectReference
        """
        return self._described_object

    @described_object.setter
    def described_object(self, described_object):
        """Sets the described_object of this V2ObjectMetricSource.


        :param described_object: The described_object of this V2ObjectMetricSource.  # noqa: E501
        :type: V2CrossVersionObjectReference
        """
        if self.local_vars_configuration.client_side_validation and described_object is None:  # noqa: E501
            raise ValueError("Invalid value for `described_object`, must not be `None`")  # noqa: E501

        self._described_object = described_object

    @property
    def metric(self):
        """Gets the metric of this V2ObjectMetricSource.  # noqa: E501


        :return: The metric of this V2ObjectMetricSource.  # noqa: E501
        :rtype: V2MetricIdentifier
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this V2ObjectMetricSource.


        :param metric: The metric of this V2ObjectMetricSource.  # noqa: E501
        :type: V2MetricIdentifier
        """
        if self.local_vars_configuration.client_side_validation and metric is None:  # noqa: E501
            raise ValueError("Invalid value for `metric`, must not be `None`")  # noqa: E501

        self._metric = metric

    @property
    def target(self):
        """Gets the target of this V2ObjectMetricSource.  # noqa: E501


        :return: The target of this V2ObjectMetricSource.  # noqa: E501
        :rtype: V2MetricTarget
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this V2ObjectMetricSource.


        :param target: The target of this V2ObjectMetricSource.  # noqa: E501
        :type: V2MetricTarget
        """
        if self.local_vars_configuration.client_side_validation and target is None:  # noqa: E501
            raise ValueError("Invalid value for `target`, must not be `None`")  # noqa: E501

        self._target = target

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
        if not isinstance(other, V2ObjectMetricSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V2ObjectMetricSource):
            return True

        return self.to_dict() != other.to_dict()
