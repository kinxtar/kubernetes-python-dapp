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


class V1beta1MatchResources(object):
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
        'exclude_resource_rules': 'list[V1beta1NamedRuleWithOperations]',
        'match_policy': 'str',
        'namespace_selector': 'V1LabelSelector',
        'object_selector': 'V1LabelSelector',
        'resource_rules': 'list[V1beta1NamedRuleWithOperations]'
    }

    attribute_map = {
        'exclude_resource_rules': 'excludeResourceRules',
        'match_policy': 'matchPolicy',
        'namespace_selector': 'namespaceSelector',
        'object_selector': 'objectSelector',
        'resource_rules': 'resourceRules'
    }

    def __init__(self, exclude_resource_rules=None, match_policy=None, namespace_selector=None, object_selector=None, resource_rules=None, local_vars_configuration=None):  # noqa: E501
        """V1beta1MatchResources - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._exclude_resource_rules = None
        self._match_policy = None
        self._namespace_selector = None
        self._object_selector = None
        self._resource_rules = None
        self.discriminator = None

        if exclude_resource_rules is not None:
            self.exclude_resource_rules = exclude_resource_rules
        if match_policy is not None:
            self.match_policy = match_policy
        if namespace_selector is not None:
            self.namespace_selector = namespace_selector
        if object_selector is not None:
            self.object_selector = object_selector
        if resource_rules is not None:
            self.resource_rules = resource_rules

    @property
    def exclude_resource_rules(self):
        """Gets the exclude_resource_rules of this V1beta1MatchResources.  # noqa: E501

        ExcludeResourceRules describes what operations on what resources/subresources the ValidatingAdmissionPolicy should not care about. The exclude rules take precedence over include rules (if a resource matches both, it is excluded)  # noqa: E501

        :return: The exclude_resource_rules of this V1beta1MatchResources.  # noqa: E501
        :rtype: list[V1beta1NamedRuleWithOperations]
        """
        return self._exclude_resource_rules

    @exclude_resource_rules.setter
    def exclude_resource_rules(self, exclude_resource_rules):
        """Sets the exclude_resource_rules of this V1beta1MatchResources.

        ExcludeResourceRules describes what operations on what resources/subresources the ValidatingAdmissionPolicy should not care about. The exclude rules take precedence over include rules (if a resource matches both, it is excluded)  # noqa: E501

        :param exclude_resource_rules: The exclude_resource_rules of this V1beta1MatchResources.  # noqa: E501
        :type: list[V1beta1NamedRuleWithOperations]
        """

        self._exclude_resource_rules = exclude_resource_rules

    @property
    def match_policy(self):
        """Gets the match_policy of this V1beta1MatchResources.  # noqa: E501

        matchPolicy defines how the \"MatchResources\" list is used to match incoming requests. Allowed values are \"Exact\" or \"Equivalent\".  - Exact: match a request only if it exactly matches a specified rule. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, but \"rules\" only included `apiGroups:[\"apps\"], apiVersions:[\"v1\"], resources: [\"deployments\"]`, a request to apps/v1beta1 or extensions/v1beta1 would not be sent to the ValidatingAdmissionPolicy.  - Equivalent: match a request if modifies a resource listed in rules, even via another API group or version. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, and \"rules\" only included `apiGroups:[\"apps\"], apiVersions:[\"v1\"], resources: [\"deployments\"]`, a request to apps/v1beta1 or extensions/v1beta1 would be converted to apps/v1 and sent to the ValidatingAdmissionPolicy.  Defaults to \"Equivalent\"  # noqa: E501

        :return: The match_policy of this V1beta1MatchResources.  # noqa: E501
        :rtype: str
        """
        return self._match_policy

    @match_policy.setter
    def match_policy(self, match_policy):
        """Sets the match_policy of this V1beta1MatchResources.

        matchPolicy defines how the \"MatchResources\" list is used to match incoming requests. Allowed values are \"Exact\" or \"Equivalent\".  - Exact: match a request only if it exactly matches a specified rule. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, but \"rules\" only included `apiGroups:[\"apps\"], apiVersions:[\"v1\"], resources: [\"deployments\"]`, a request to apps/v1beta1 or extensions/v1beta1 would not be sent to the ValidatingAdmissionPolicy.  - Equivalent: match a request if modifies a resource listed in rules, even via another API group or version. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, and \"rules\" only included `apiGroups:[\"apps\"], apiVersions:[\"v1\"], resources: [\"deployments\"]`, a request to apps/v1beta1 or extensions/v1beta1 would be converted to apps/v1 and sent to the ValidatingAdmissionPolicy.  Defaults to \"Equivalent\"  # noqa: E501

        :param match_policy: The match_policy of this V1beta1MatchResources.  # noqa: E501
        :type: str
        """

        self._match_policy = match_policy

    @property
    def namespace_selector(self):
        """Gets the namespace_selector of this V1beta1MatchResources.  # noqa: E501


        :return: The namespace_selector of this V1beta1MatchResources.  # noqa: E501
        :rtype: V1LabelSelector
        """
        return self._namespace_selector

    @namespace_selector.setter
    def namespace_selector(self, namespace_selector):
        """Sets the namespace_selector of this V1beta1MatchResources.


        :param namespace_selector: The namespace_selector of this V1beta1MatchResources.  # noqa: E501
        :type: V1LabelSelector
        """

        self._namespace_selector = namespace_selector

    @property
    def object_selector(self):
        """Gets the object_selector of this V1beta1MatchResources.  # noqa: E501


        :return: The object_selector of this V1beta1MatchResources.  # noqa: E501
        :rtype: V1LabelSelector
        """
        return self._object_selector

    @object_selector.setter
    def object_selector(self, object_selector):
        """Sets the object_selector of this V1beta1MatchResources.


        :param object_selector: The object_selector of this V1beta1MatchResources.  # noqa: E501
        :type: V1LabelSelector
        """

        self._object_selector = object_selector

    @property
    def resource_rules(self):
        """Gets the resource_rules of this V1beta1MatchResources.  # noqa: E501

        ResourceRules describes what operations on what resources/subresources the ValidatingAdmissionPolicy matches. The policy cares about an operation if it matches _any_ Rule.  # noqa: E501

        :return: The resource_rules of this V1beta1MatchResources.  # noqa: E501
        :rtype: list[V1beta1NamedRuleWithOperations]
        """
        return self._resource_rules

    @resource_rules.setter
    def resource_rules(self, resource_rules):
        """Sets the resource_rules of this V1beta1MatchResources.

        ResourceRules describes what operations on what resources/subresources the ValidatingAdmissionPolicy matches. The policy cares about an operation if it matches _any_ Rule.  # noqa: E501

        :param resource_rules: The resource_rules of this V1beta1MatchResources.  # noqa: E501
        :type: list[V1beta1NamedRuleWithOperations]
        """

        self._resource_rules = resource_rules

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
        if not isinstance(other, V1beta1MatchResources):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta1MatchResources):
            return True

        return self.to_dict() != other.to_dict()
