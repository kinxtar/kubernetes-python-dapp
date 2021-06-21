# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.18
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1alpha1PolicyRulesWithSubjects(object):
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
        'non_resource_rules': 'list[V1alpha1NonResourcePolicyRule]',
        'resource_rules': 'list[V1alpha1ResourcePolicyRule]',
        'subjects': 'list[FlowcontrolV1alpha1Subject]'
    }

    attribute_map = {
        'non_resource_rules': 'nonResourceRules',
        'resource_rules': 'resourceRules',
        'subjects': 'subjects'
    }

    def __init__(self, non_resource_rules=None, resource_rules=None, subjects=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1PolicyRulesWithSubjects - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._non_resource_rules = None
        self._resource_rules = None
        self._subjects = None
        self.discriminator = None

        if non_resource_rules is not None:
            self.non_resource_rules = non_resource_rules
        if resource_rules is not None:
            self.resource_rules = resource_rules
        self.subjects = subjects

    @property
    def non_resource_rules(self):
        """Gets the non_resource_rules of this V1alpha1PolicyRulesWithSubjects.  # noqa: E501

        `nonResourceRules` is a list of NonResourcePolicyRules that identify matching requests according to their verb and the target non-resource URL.  # noqa: E501

        :return: The non_resource_rules of this V1alpha1PolicyRulesWithSubjects.  # noqa: E501
        :rtype: list[V1alpha1NonResourcePolicyRule]
        """
        return self._non_resource_rules

    @non_resource_rules.setter
    def non_resource_rules(self, non_resource_rules):
        """Sets the non_resource_rules of this V1alpha1PolicyRulesWithSubjects.

        `nonResourceRules` is a list of NonResourcePolicyRules that identify matching requests according to their verb and the target non-resource URL.  # noqa: E501

        :param non_resource_rules: The non_resource_rules of this V1alpha1PolicyRulesWithSubjects.  # noqa: E501
        :type: list[V1alpha1NonResourcePolicyRule]
        """

        self._non_resource_rules = non_resource_rules

    @property
    def resource_rules(self):
        """Gets the resource_rules of this V1alpha1PolicyRulesWithSubjects.  # noqa: E501

        `resourceRules` is a slice of ResourcePolicyRules that identify matching requests according to their verb and the target resource. At least one of `resourceRules` and `nonResourceRules` has to be non-empty.  # noqa: E501

        :return: The resource_rules of this V1alpha1PolicyRulesWithSubjects.  # noqa: E501
        :rtype: list[V1alpha1ResourcePolicyRule]
        """
        return self._resource_rules

    @resource_rules.setter
    def resource_rules(self, resource_rules):
        """Sets the resource_rules of this V1alpha1PolicyRulesWithSubjects.

        `resourceRules` is a slice of ResourcePolicyRules that identify matching requests according to their verb and the target resource. At least one of `resourceRules` and `nonResourceRules` has to be non-empty.  # noqa: E501

        :param resource_rules: The resource_rules of this V1alpha1PolicyRulesWithSubjects.  # noqa: E501
        :type: list[V1alpha1ResourcePolicyRule]
        """

        self._resource_rules = resource_rules

    @property
    def subjects(self):
        """Gets the subjects of this V1alpha1PolicyRulesWithSubjects.  # noqa: E501

        subjects is the list of normal user, serviceaccount, or group that this rule cares about. There must be at least one member in this slice. A slice that includes both the system:authenticated and system:unauthenticated user groups matches every request. Required.  # noqa: E501

        :return: The subjects of this V1alpha1PolicyRulesWithSubjects.  # noqa: E501
        :rtype: list[FlowcontrolV1alpha1Subject]
        """
        return self._subjects

    @subjects.setter
    def subjects(self, subjects):
        """Sets the subjects of this V1alpha1PolicyRulesWithSubjects.

        subjects is the list of normal user, serviceaccount, or group that this rule cares about. There must be at least one member in this slice. A slice that includes both the system:authenticated and system:unauthenticated user groups matches every request. Required.  # noqa: E501

        :param subjects: The subjects of this V1alpha1PolicyRulesWithSubjects.  # noqa: E501
        :type: list[FlowcontrolV1alpha1Subject]
        """
        if self.local_vars_configuration.client_side_validation and subjects is None:  # noqa: E501
            raise ValueError("Invalid value for `subjects`, must not be `None`")  # noqa: E501

        self._subjects = subjects

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
        if not isinstance(other, V1alpha1PolicyRulesWithSubjects):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1PolicyRulesWithSubjects):
            return True

        return self.to_dict() != other.to_dict()
