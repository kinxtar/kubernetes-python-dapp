# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.5.1-660c2a2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class V1beta1NetworkPolicyPeer(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, namespace_selector=None, pod_selector=None):
        """
        V1beta1NetworkPolicyPeer - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'namespace_selector': 'UnversionedLabelSelector',
            'pod_selector': 'UnversionedLabelSelector'
        }

        self.attribute_map = {
            'namespace_selector': 'namespaceSelector',
            'pod_selector': 'podSelector'
        }

        self._namespace_selector = namespace_selector
        self._pod_selector = pod_selector


    @property
    def namespace_selector(self):
        """
        Gets the namespace_selector of this V1beta1NetworkPolicyPeer.
        Selects Namespaces using cluster scoped-labels.  This matches all pods in all namespaces selected by this label selector. This field follows standard label selector semantics. If omitted, this selector selects no namespaces. If present but empty, this selector selects all namespaces.

        :return: The namespace_selector of this V1beta1NetworkPolicyPeer.
        :rtype: UnversionedLabelSelector
        """
        return self._namespace_selector

    @namespace_selector.setter
    def namespace_selector(self, namespace_selector):
        """
        Sets the namespace_selector of this V1beta1NetworkPolicyPeer.
        Selects Namespaces using cluster scoped-labels.  This matches all pods in all namespaces selected by this label selector. This field follows standard label selector semantics. If omitted, this selector selects no namespaces. If present but empty, this selector selects all namespaces.

        :param namespace_selector: The namespace_selector of this V1beta1NetworkPolicyPeer.
        :type: UnversionedLabelSelector
        """

        self._namespace_selector = namespace_selector

    @property
    def pod_selector(self):
        """
        Gets the pod_selector of this V1beta1NetworkPolicyPeer.
        This is a label selector which selects Pods in this namespace. This field follows standard label selector semantics. If not provided, this selector selects no pods. If present but empty, this selector selects all pods in this namespace.

        :return: The pod_selector of this V1beta1NetworkPolicyPeer.
        :rtype: UnversionedLabelSelector
        """
        return self._pod_selector

    @pod_selector.setter
    def pod_selector(self, pod_selector):
        """
        Sets the pod_selector of this V1beta1NetworkPolicyPeer.
        This is a label selector which selects Pods in this namespace. This field follows standard label selector semantics. If not provided, this selector selects no pods. If present but empty, this selector selects all pods in this namespace.

        :param pod_selector: The pod_selector of this V1beta1NetworkPolicyPeer.
        :type: UnversionedLabelSelector
        """

        self._pod_selector = pod_selector

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
