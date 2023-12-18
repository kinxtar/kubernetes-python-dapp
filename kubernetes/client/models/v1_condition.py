# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.29
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1Condition(object):
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
        'last_transition_time': 'datetime',
        'message': 'str',
        'observed_generation': 'int',
        'reason': 'str',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'last_transition_time': 'lastTransitionTime',
        'message': 'message',
        'observed_generation': 'observedGeneration',
        'reason': 'reason',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, last_transition_time=None, message=None, observed_generation=None, reason=None, status=None, type=None, local_vars_configuration=None):  # noqa: E501
        """V1Condition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._last_transition_time = None
        self._message = None
        self._observed_generation = None
        self._reason = None
        self._status = None
        self._type = None
        self.discriminator = None

        self.last_transition_time = last_transition_time
        self.message = message
        if observed_generation is not None:
            self.observed_generation = observed_generation
        self.reason = reason
        self.status = status
        self.type = type

    @property
    def last_transition_time(self):
        """Gets the last_transition_time of this V1Condition.  # noqa: E501

        lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.  # noqa: E501

        :return: The last_transition_time of this V1Condition.  # noqa: E501
        :rtype: datetime
        """
        return self._last_transition_time

    @last_transition_time.setter
    def last_transition_time(self, last_transition_time):
        """Sets the last_transition_time of this V1Condition.

        lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.  # noqa: E501

        :param last_transition_time: The last_transition_time of this V1Condition.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and last_transition_time is None:  # noqa: E501
            raise ValueError("Invalid value for `last_transition_time`, must not be `None`")  # noqa: E501

        self._last_transition_time = last_transition_time

    @property
    def message(self):
        """Gets the message of this V1Condition.  # noqa: E501

        message is a human readable message indicating details about the transition. This may be an empty string.  # noqa: E501

        :return: The message of this V1Condition.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this V1Condition.

        message is a human readable message indicating details about the transition. This may be an empty string.  # noqa: E501

        :param message: The message of this V1Condition.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def observed_generation(self):
        """Gets the observed_generation of this V1Condition.  # noqa: E501

        observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance.  # noqa: E501

        :return: The observed_generation of this V1Condition.  # noqa: E501
        :rtype: int
        """
        return self._observed_generation

    @observed_generation.setter
    def observed_generation(self, observed_generation):
        """Sets the observed_generation of this V1Condition.

        observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance.  # noqa: E501

        :param observed_generation: The observed_generation of this V1Condition.  # noqa: E501
        :type: int
        """

        self._observed_generation = observed_generation

    @property
    def reason(self):
        """Gets the reason of this V1Condition.  # noqa: E501

        reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty.  # noqa: E501

        :return: The reason of this V1Condition.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this V1Condition.

        reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty.  # noqa: E501

        :param reason: The reason of this V1Condition.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and reason is None:  # noqa: E501
            raise ValueError("Invalid value for `reason`, must not be `None`")  # noqa: E501

        self._reason = reason

    @property
    def status(self):
        """Gets the status of this V1Condition.  # noqa: E501

        status of the condition, one of True, False, Unknown.  # noqa: E501

        :return: The status of this V1Condition.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this V1Condition.

        status of the condition, one of True, False, Unknown.  # noqa: E501

        :param status: The status of this V1Condition.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def type(self):
        """Gets the type of this V1Condition.  # noqa: E501

        type of condition in CamelCase or in foo.example.com/CamelCase.  # noqa: E501

        :return: The type of this V1Condition.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1Condition.

        type of condition in CamelCase or in foo.example.com/CamelCase.  # noqa: E501

        :param type: The type of this V1Condition.  # noqa: E501
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
        if not isinstance(other, V1Condition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1Condition):
            return True

        return self.to_dict() != other.to_dict()
