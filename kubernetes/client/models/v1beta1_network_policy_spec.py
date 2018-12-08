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


class V1beta1NetworkPolicySpec(object):
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
        'egress': 'list[V1beta1NetworkPolicyEgressRule]',
        'ingress': 'list[V1beta1NetworkPolicyIngressRule]',
        'pod_selector': 'V1LabelSelector',
        'policy_types': 'list[str]'
    }

    attribute_map = {
        'egress': 'egress',
        'ingress': 'ingress',
        'pod_selector': 'podSelector',
        'policy_types': 'policyTypes'
    }

    def __init__(self, egress=None, ingress=None, pod_selector=None, policy_types=None):
        """
        V1beta1NetworkPolicySpec - a model defined in Swagger
        """

        self._egress = None
        self._ingress = None
        self._pod_selector = None
        self._policy_types = None
        self.discriminator = None

        if egress is not None:
          self.egress = egress
        if ingress is not None:
          self.ingress = ingress
        self.pod_selector = pod_selector
        if policy_types is not None:
          self.policy_types = policy_types

    @property
    def egress(self):
        """
        Gets the egress of this V1beta1NetworkPolicySpec.
        List of egress rules to be applied to the selected pods. Outgoing traffic is allowed if there are no NetworkPolicies selecting the pod (and cluster policy otherwise allows the traffic), OR if the traffic matches at least one egress rule across all of the NetworkPolicy objects whose podSelector matches the pod. If this field is empty then this NetworkPolicy limits all outgoing traffic (and serves solely to ensure that the pods it selects are isolated by default). This field is beta-level in 1.8

        :return: The egress of this V1beta1NetworkPolicySpec.
        :rtype: list[V1beta1NetworkPolicyEgressRule]
        """
        return self._egress

    @egress.setter
    def egress(self, egress):
        """
        Sets the egress of this V1beta1NetworkPolicySpec.
        List of egress rules to be applied to the selected pods. Outgoing traffic is allowed if there are no NetworkPolicies selecting the pod (and cluster policy otherwise allows the traffic), OR if the traffic matches at least one egress rule across all of the NetworkPolicy objects whose podSelector matches the pod. If this field is empty then this NetworkPolicy limits all outgoing traffic (and serves solely to ensure that the pods it selects are isolated by default). This field is beta-level in 1.8

        :param egress: The egress of this V1beta1NetworkPolicySpec.
        :type: list[V1beta1NetworkPolicyEgressRule]
        """

        self._egress = egress

    @property
    def ingress(self):
        """
        Gets the ingress of this V1beta1NetworkPolicySpec.
        List of ingress rules to be applied to the selected pods. Traffic is allowed to a pod if there are no NetworkPolicies selecting the pod OR if the traffic source is the pod's local node, OR if the traffic matches at least one ingress rule across all of the NetworkPolicy objects whose podSelector matches the pod. If this field is empty then this NetworkPolicy does not allow any traffic (and serves solely to ensure that the pods it selects are isolated by default).

        :return: The ingress of this V1beta1NetworkPolicySpec.
        :rtype: list[V1beta1NetworkPolicyIngressRule]
        """
        return self._ingress

    @ingress.setter
    def ingress(self, ingress):
        """
        Sets the ingress of this V1beta1NetworkPolicySpec.
        List of ingress rules to be applied to the selected pods. Traffic is allowed to a pod if there are no NetworkPolicies selecting the pod OR if the traffic source is the pod's local node, OR if the traffic matches at least one ingress rule across all of the NetworkPolicy objects whose podSelector matches the pod. If this field is empty then this NetworkPolicy does not allow any traffic (and serves solely to ensure that the pods it selects are isolated by default).

        :param ingress: The ingress of this V1beta1NetworkPolicySpec.
        :type: list[V1beta1NetworkPolicyIngressRule]
        """

        self._ingress = ingress

    @property
    def pod_selector(self):
        """
        Gets the pod_selector of this V1beta1NetworkPolicySpec.
        Selects the pods to which this NetworkPolicy object applies.  The array of ingress rules is applied to any pods selected by this field. Multiple network policies can select the same set of pods.  In this case, the ingress rules for each are combined additively. This field is NOT optional and follows standard label selector semantics. An empty podSelector matches all pods in this namespace.

        :return: The pod_selector of this V1beta1NetworkPolicySpec.
        :rtype: V1LabelSelector
        """
        return self._pod_selector

    @pod_selector.setter
    def pod_selector(self, pod_selector):
        """
        Sets the pod_selector of this V1beta1NetworkPolicySpec.
        Selects the pods to which this NetworkPolicy object applies.  The array of ingress rules is applied to any pods selected by this field. Multiple network policies can select the same set of pods.  In this case, the ingress rules for each are combined additively. This field is NOT optional and follows standard label selector semantics. An empty podSelector matches all pods in this namespace.

        :param pod_selector: The pod_selector of this V1beta1NetworkPolicySpec.
        :type: V1LabelSelector
        """
        if pod_selector is None:
            raise ValueError("Invalid value for `pod_selector`, must not be `None`")

        self._pod_selector = pod_selector

    @property
    def policy_types(self):
        """
        Gets the policy_types of this V1beta1NetworkPolicySpec.
        List of rule types that the NetworkPolicy relates to. Valid options are Ingress, Egress, or Ingress,Egress. If this field is not specified, it will default based on the existence of Ingress or Egress rules; policies that contain an Egress section are assumed to affect Egress, and all policies (whether or not they contain an Ingress section) are assumed to affect Ingress. If you want to write an egress-only policy, you must explicitly specify policyTypes [ \"Egress\" ]. Likewise, if you want to write a policy that specifies that no egress is allowed, you must specify a policyTypes value that include \"Egress\" (since such a policy would not include an Egress section and would otherwise default to just [ \"Ingress\" ]). This field is beta-level in 1.8

        :return: The policy_types of this V1beta1NetworkPolicySpec.
        :rtype: list[str]
        """
        return self._policy_types

    @policy_types.setter
    def policy_types(self, policy_types):
        """
        Sets the policy_types of this V1beta1NetworkPolicySpec.
        List of rule types that the NetworkPolicy relates to. Valid options are Ingress, Egress, or Ingress,Egress. If this field is not specified, it will default based on the existence of Ingress or Egress rules; policies that contain an Egress section are assumed to affect Egress, and all policies (whether or not they contain an Ingress section) are assumed to affect Ingress. If you want to write an egress-only policy, you must explicitly specify policyTypes [ \"Egress\" ]. Likewise, if you want to write a policy that specifies that no egress is allowed, you must specify a policyTypes value that include \"Egress\" (since such a policy would not include an Egress section and would otherwise default to just [ \"Ingress\" ]). This field is beta-level in 1.8

        :param policy_types: The policy_types of this V1beta1NetworkPolicySpec.
        :type: list[str]
        """

        self._policy_types = policy_types

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
        if not isinstance(other, V1beta1NetworkPolicySpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
