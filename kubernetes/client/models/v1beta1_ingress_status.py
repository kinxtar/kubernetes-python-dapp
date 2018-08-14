# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.11.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1beta1IngressStatus(object):
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
        'load_balancer': 'V1LoadBalancerStatus'
    }

    attribute_map = {
        'load_balancer': 'loadBalancer'
    }

    def __init__(self, load_balancer=None):
        """
        V1beta1IngressStatus - a model defined in Swagger
        """

        self._load_balancer = None
        self.discriminator = None

        if load_balancer is not None:
          self.load_balancer = load_balancer

    @property
    def load_balancer(self):
        """
        Gets the load_balancer of this V1beta1IngressStatus.
        LoadBalancer contains the current status of the load-balancer.

        :return: The load_balancer of this V1beta1IngressStatus.
        :rtype: V1LoadBalancerStatus
        """
        return self._load_balancer

    @load_balancer.setter
    def load_balancer(self, load_balancer):
        """
        Sets the load_balancer of this V1beta1IngressStatus.
        LoadBalancer contains the current status of the load-balancer.

        :param load_balancer: The load_balancer of this V1beta1IngressStatus.
        :type: V1LoadBalancerStatus
        """

        self._load_balancer = load_balancer

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
        if not isinstance(other, V1beta1IngressStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
