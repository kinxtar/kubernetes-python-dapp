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


class V1alpha1ValidatingAdmissionPolicyStatus(object):
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
        'conditions': 'list[V1Condition]',
        'observed_generation': 'int',
        'type_checking': 'V1alpha1TypeChecking'
    }

    attribute_map = {
        'conditions': 'conditions',
        'observed_generation': 'observedGeneration',
        'type_checking': 'typeChecking'
    }

    def __init__(self, conditions=None, observed_generation=None, type_checking=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1ValidatingAdmissionPolicyStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._conditions = None
        self._observed_generation = None
        self._type_checking = None
        self.discriminator = None

        if conditions is not None:
            self.conditions = conditions
        if observed_generation is not None:
            self.observed_generation = observed_generation
        if type_checking is not None:
            self.type_checking = type_checking

    @property
    def conditions(self):
        """Gets the conditions of this V1alpha1ValidatingAdmissionPolicyStatus.  # noqa: E501

        The conditions represent the latest available observations of a policy's current state.  # noqa: E501

        :return: The conditions of this V1alpha1ValidatingAdmissionPolicyStatus.  # noqa: E501
        :rtype: list[V1Condition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this V1alpha1ValidatingAdmissionPolicyStatus.

        The conditions represent the latest available observations of a policy's current state.  # noqa: E501

        :param conditions: The conditions of this V1alpha1ValidatingAdmissionPolicyStatus.  # noqa: E501
        :type: list[V1Condition]
        """

        self._conditions = conditions

    @property
    def observed_generation(self):
        """Gets the observed_generation of this V1alpha1ValidatingAdmissionPolicyStatus.  # noqa: E501

        The generation observed by the controller.  # noqa: E501

        :return: The observed_generation of this V1alpha1ValidatingAdmissionPolicyStatus.  # noqa: E501
        :rtype: int
        """
        return self._observed_generation

    @observed_generation.setter
    def observed_generation(self, observed_generation):
        """Sets the observed_generation of this V1alpha1ValidatingAdmissionPolicyStatus.

        The generation observed by the controller.  # noqa: E501

        :param observed_generation: The observed_generation of this V1alpha1ValidatingAdmissionPolicyStatus.  # noqa: E501
        :type: int
        """

        self._observed_generation = observed_generation

    @property
    def type_checking(self):
        """Gets the type_checking of this V1alpha1ValidatingAdmissionPolicyStatus.  # noqa: E501


        :return: The type_checking of this V1alpha1ValidatingAdmissionPolicyStatus.  # noqa: E501
        :rtype: V1alpha1TypeChecking
        """
        return self._type_checking

    @type_checking.setter
    def type_checking(self, type_checking):
        """Sets the type_checking of this V1alpha1ValidatingAdmissionPolicyStatus.


        :param type_checking: The type_checking of this V1alpha1ValidatingAdmissionPolicyStatus.  # noqa: E501
        :type: V1alpha1TypeChecking
        """

        self._type_checking = type_checking

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
        if not isinstance(other, V1alpha1ValidatingAdmissionPolicyStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1ValidatingAdmissionPolicyStatus):
            return True

        return self.to_dict() != other.to_dict()
