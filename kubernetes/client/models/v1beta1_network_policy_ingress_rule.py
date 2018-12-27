# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.13.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1beta1NetworkPolicyIngressRule(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        '_from': 'list[V1beta1NetworkPolicyPeer]',
        'ports': 'list[V1beta1NetworkPolicyPort]'
    }

    attribute_map = {
        '_from': 'from',
        'ports': 'ports'
    }

    def __init__(self, _from=None, ports=None):
        """
        V1beta1NetworkPolicyIngressRule - a model defined in Swagger
        """

        self.__from = None
        self._ports = None
        self.discriminator = None

        if _from is not None:
          self._from = _from
        if ports is not None:
          self.ports = ports

    @property
    def _from(self):
        """
        Gets the _from of this V1beta1NetworkPolicyIngressRule.
        List of sources which should be able to access the pods selected for this rule. Items in this list are combined using a logical OR operation. If this field is empty or missing, this rule matches all sources (traffic not restricted by source). If this field is present and contains at least on item, this rule allows traffic only if the traffic matches at least one item in the from list.

        :return: The _from of this V1beta1NetworkPolicyIngressRule.
        :rtype: list[V1beta1NetworkPolicyPeer]
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this V1beta1NetworkPolicyIngressRule.
        List of sources which should be able to access the pods selected for this rule. Items in this list are combined using a logical OR operation. If this field is empty or missing, this rule matches all sources (traffic not restricted by source). If this field is present and contains at least on item, this rule allows traffic only if the traffic matches at least one item in the from list.

        :param _from: The _from of this V1beta1NetworkPolicyIngressRule.
        :type: list[V1beta1NetworkPolicyPeer]
        """

        self.__from = _from

    @property
    def ports(self):
        """
        Gets the ports of this V1beta1NetworkPolicyIngressRule.
        List of ports which should be made accessible on the pods selected for this rule. Each item in this list is combined using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not restricted by port). If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list.

        :return: The ports of this V1beta1NetworkPolicyIngressRule.
        :rtype: list[V1beta1NetworkPolicyPort]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """
        Sets the ports of this V1beta1NetworkPolicyIngressRule.
        List of ports which should be made accessible on the pods selected for this rule. Each item in this list is combined using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not restricted by port). If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list.

        :param ports: The ports of this V1beta1NetworkPolicyIngressRule.
        :type: list[V1beta1NetworkPolicyPort]
        """

        self._ports = ports

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
        if not isinstance(other, V1beta1NetworkPolicyIngressRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
