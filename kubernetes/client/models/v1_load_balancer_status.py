# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1LoadBalancerStatus(object):
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
        'ingress': 'list[V1LoadBalancerIngress]'
    }

    attribute_map = {
        'ingress': 'ingress'
    }

    def __init__(self, ingress=None):
        """
        V1LoadBalancerStatus - a model defined in Swagger
        """

        self._ingress = None
        self.discriminator = None

        if ingress is not None:
          self.ingress = ingress

    @property
    def ingress(self):
        """
        Gets the ingress of this V1LoadBalancerStatus.
        Ingress is a list containing ingress points for the load-balancer. Traffic intended for the service should be sent to these ingress points.

        :return: The ingress of this V1LoadBalancerStatus.
        :rtype: list[V1LoadBalancerIngress]
        """
        return self._ingress

    @ingress.setter
    def ingress(self, ingress):
        """
        Sets the ingress of this V1LoadBalancerStatus.
        Ingress is a list containing ingress points for the load-balancer. Traffic intended for the service should be sent to these ingress points.

        :param ingress: The ingress of this V1LoadBalancerStatus.
        :type: list[V1LoadBalancerIngress]
        """

        self._ingress = ingress

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
        if not isinstance(other, V1LoadBalancerStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
