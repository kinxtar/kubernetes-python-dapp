# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.14.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1beta1NetworkPolicyEgressRule(object):
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
        'ports': 'list[V1beta1NetworkPolicyPort]',
        'to': 'list[V1beta1NetworkPolicyPeer]'
    }

    attribute_map = {
        'ports': 'ports',
        'to': 'to'
    }

    def __init__(self, ports=None, to=None):
        """
        V1beta1NetworkPolicyEgressRule - a model defined in Swagger
        """

        self._ports = None
        self._to = None
        self.discriminator = None

        if ports is not None:
          self.ports = ports
        if to is not None:
          self.to = to

    @property
    def ports(self):
        """
        Gets the ports of this V1beta1NetworkPolicyEgressRule.
        List of destination ports for outgoing traffic. Each item in this list is combined using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not restricted by port). If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list.

        :return: The ports of this V1beta1NetworkPolicyEgressRule.
        :rtype: list[V1beta1NetworkPolicyPort]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """
        Sets the ports of this V1beta1NetworkPolicyEgressRule.
        List of destination ports for outgoing traffic. Each item in this list is combined using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not restricted by port). If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list.

        :param ports: The ports of this V1beta1NetworkPolicyEgressRule.
        :type: list[V1beta1NetworkPolicyPort]
        """

        self._ports = ports

    @property
    def to(self):
        """
        Gets the to of this V1beta1NetworkPolicyEgressRule.
        List of destinations for outgoing traffic of pods selected for this rule. Items in this list are combined using a logical OR operation. If this field is empty or missing, this rule matches all destinations (traffic not restricted by destination). If this field is present and contains at least one item, this rule allows traffic only if the traffic matches at least one item in the to list.

        :return: The to of this V1beta1NetworkPolicyEgressRule.
        :rtype: list[V1beta1NetworkPolicyPeer]
        """
        return self._to

    @to.setter
    def to(self, to):
        """
        Sets the to of this V1beta1NetworkPolicyEgressRule.
        List of destinations for outgoing traffic of pods selected for this rule. Items in this list are combined using a logical OR operation. If this field is empty or missing, this rule matches all destinations (traffic not restricted by destination). If this field is present and contains at least one item, this rule allows traffic only if the traffic matches at least one item in the to list.

        :param to: The to of this V1beta1NetworkPolicyEgressRule.
        :type: list[V1beta1NetworkPolicyPeer]
        """

        self._to = to

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
        if not isinstance(other, V1beta1NetworkPolicyEgressRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
