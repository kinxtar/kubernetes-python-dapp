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


class V1ServiceSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, cluster_ip=None, deprecated_public_i_ps=None, external_i_ps=None, external_name=None, load_balancer_ip=None, load_balancer_source_ranges=None, ports=None, selector=None, session_affinity=None, type=None):
        """
        V1ServiceSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cluster_ip': 'str',
            'deprecated_public_i_ps': 'list[str]',
            'external_i_ps': 'list[str]',
            'external_name': 'str',
            'load_balancer_ip': 'str',
            'load_balancer_source_ranges': 'list[str]',
            'ports': 'list[V1ServicePort]',
            'selector': 'dict(str, str)',
            'session_affinity': 'str',
            'type': 'str'
        }

        self.attribute_map = {
            'cluster_ip': 'clusterIP',
            'deprecated_public_i_ps': 'deprecatedPublicIPs',
            'external_i_ps': 'externalIPs',
            'external_name': 'externalName',
            'load_balancer_ip': 'loadBalancerIP',
            'load_balancer_source_ranges': 'loadBalancerSourceRanges',
            'ports': 'ports',
            'selector': 'selector',
            'session_affinity': 'sessionAffinity',
            'type': 'type'
        }

        self._cluster_ip = cluster_ip
        self._deprecated_public_i_ps = deprecated_public_i_ps
        self._external_i_ps = external_i_ps
        self._external_name = external_name
        self._load_balancer_ip = load_balancer_ip
        self._load_balancer_source_ranges = load_balancer_source_ranges
        self._ports = ports
        self._selector = selector
        self._session_affinity = session_affinity
        self._type = type


    @property
    def cluster_ip(self):
        """
        Gets the cluster_ip of this V1ServiceSpec.
        clusterIP is the IP address of the service and is usually assigned randomly by the master. If an address is specified manually and is not in use by others, it will be allocated to the service; otherwise, creation of the service will fail. This field can not be changed through updates. Valid values are \"None\", empty string (\"\"), or a valid IP address. \"None\" can be specified for headless services when proxying is not required. Only applies to types ClusterIP, NodePort, and LoadBalancer. Ignored if type is ExternalName. More info: http://kubernetes.io/docs/user-guide/services#virtual-ips-and-service-proxies

        :return: The cluster_ip of this V1ServiceSpec.
        :rtype: str
        """
        return self._cluster_ip

    @cluster_ip.setter
    def cluster_ip(self, cluster_ip):
        """
        Sets the cluster_ip of this V1ServiceSpec.
        clusterIP is the IP address of the service and is usually assigned randomly by the master. If an address is specified manually and is not in use by others, it will be allocated to the service; otherwise, creation of the service will fail. This field can not be changed through updates. Valid values are \"None\", empty string (\"\"), or a valid IP address. \"None\" can be specified for headless services when proxying is not required. Only applies to types ClusterIP, NodePort, and LoadBalancer. Ignored if type is ExternalName. More info: http://kubernetes.io/docs/user-guide/services#virtual-ips-and-service-proxies

        :param cluster_ip: The cluster_ip of this V1ServiceSpec.
        :type: str
        """

        self._cluster_ip = cluster_ip

    @property
    def deprecated_public_i_ps(self):
        """
        Gets the deprecated_public_i_ps of this V1ServiceSpec.
        deprecatedPublicIPs is deprecated and replaced by the externalIPs field with almost the exact same semantics.  This field is retained in the v1 API for compatibility until at least 8/20/2016.  It will be removed from any new API revisions.  If both deprecatedPublicIPs *and* externalIPs are set, deprecatedPublicIPs is used.

        :return: The deprecated_public_i_ps of this V1ServiceSpec.
        :rtype: list[str]
        """
        return self._deprecated_public_i_ps

    @deprecated_public_i_ps.setter
    def deprecated_public_i_ps(self, deprecated_public_i_ps):
        """
        Sets the deprecated_public_i_ps of this V1ServiceSpec.
        deprecatedPublicIPs is deprecated and replaced by the externalIPs field with almost the exact same semantics.  This field is retained in the v1 API for compatibility until at least 8/20/2016.  It will be removed from any new API revisions.  If both deprecatedPublicIPs *and* externalIPs are set, deprecatedPublicIPs is used.

        :param deprecated_public_i_ps: The deprecated_public_i_ps of this V1ServiceSpec.
        :type: list[str]
        """

        self._deprecated_public_i_ps = deprecated_public_i_ps

    @property
    def external_i_ps(self):
        """
        Gets the external_i_ps of this V1ServiceSpec.
        externalIPs is a list of IP addresses for which nodes in the cluster will also accept traffic for this service.  These IPs are not managed by Kubernetes.  The user is responsible for ensuring that traffic arrives at a node with this IP.  A common example is external load-balancers that are not part of the Kubernetes system.  A previous form of this functionality exists as the deprecatedPublicIPs field.  When using this field, callers should also clear the deprecatedPublicIPs field.

        :return: The external_i_ps of this V1ServiceSpec.
        :rtype: list[str]
        """
        return self._external_i_ps

    @external_i_ps.setter
    def external_i_ps(self, external_i_ps):
        """
        Sets the external_i_ps of this V1ServiceSpec.
        externalIPs is a list of IP addresses for which nodes in the cluster will also accept traffic for this service.  These IPs are not managed by Kubernetes.  The user is responsible for ensuring that traffic arrives at a node with this IP.  A common example is external load-balancers that are not part of the Kubernetes system.  A previous form of this functionality exists as the deprecatedPublicIPs field.  When using this field, callers should also clear the deprecatedPublicIPs field.

        :param external_i_ps: The external_i_ps of this V1ServiceSpec.
        :type: list[str]
        """

        self._external_i_ps = external_i_ps

    @property
    def external_name(self):
        """
        Gets the external_name of this V1ServiceSpec.
        externalName is the external reference that kubedns or equivalent will return as a CNAME record for this service. No proxying will be involved. Must be a valid DNS name and requires Type to be ExternalName.

        :return: The external_name of this V1ServiceSpec.
        :rtype: str
        """
        return self._external_name

    @external_name.setter
    def external_name(self, external_name):
        """
        Sets the external_name of this V1ServiceSpec.
        externalName is the external reference that kubedns or equivalent will return as a CNAME record for this service. No proxying will be involved. Must be a valid DNS name and requires Type to be ExternalName.

        :param external_name: The external_name of this V1ServiceSpec.
        :type: str
        """

        self._external_name = external_name

    @property
    def load_balancer_ip(self):
        """
        Gets the load_balancer_ip of this V1ServiceSpec.
        Only applies to Service Type: LoadBalancer LoadBalancer will get created with the IP specified in this field. This feature depends on whether the underlying cloud-provider supports specifying the loadBalancerIP when a load balancer is created. This field will be ignored if the cloud-provider does not support the feature.

        :return: The load_balancer_ip of this V1ServiceSpec.
        :rtype: str
        """
        return self._load_balancer_ip

    @load_balancer_ip.setter
    def load_balancer_ip(self, load_balancer_ip):
        """
        Sets the load_balancer_ip of this V1ServiceSpec.
        Only applies to Service Type: LoadBalancer LoadBalancer will get created with the IP specified in this field. This feature depends on whether the underlying cloud-provider supports specifying the loadBalancerIP when a load balancer is created. This field will be ignored if the cloud-provider does not support the feature.

        :param load_balancer_ip: The load_balancer_ip of this V1ServiceSpec.
        :type: str
        """

        self._load_balancer_ip = load_balancer_ip

    @property
    def load_balancer_source_ranges(self):
        """
        Gets the load_balancer_source_ranges of this V1ServiceSpec.
        If specified and supported by the platform, this will restrict traffic through the cloud-provider load-balancer will be restricted to the specified client IPs. This field will be ignored if the cloud-provider does not support the feature.\" More info: http://kubernetes.io/docs/user-guide/services-firewalls

        :return: The load_balancer_source_ranges of this V1ServiceSpec.
        :rtype: list[str]
        """
        return self._load_balancer_source_ranges

    @load_balancer_source_ranges.setter
    def load_balancer_source_ranges(self, load_balancer_source_ranges):
        """
        Sets the load_balancer_source_ranges of this V1ServiceSpec.
        If specified and supported by the platform, this will restrict traffic through the cloud-provider load-balancer will be restricted to the specified client IPs. This field will be ignored if the cloud-provider does not support the feature.\" More info: http://kubernetes.io/docs/user-guide/services-firewalls

        :param load_balancer_source_ranges: The load_balancer_source_ranges of this V1ServiceSpec.
        :type: list[str]
        """

        self._load_balancer_source_ranges = load_balancer_source_ranges

    @property
    def ports(self):
        """
        Gets the ports of this V1ServiceSpec.
        The list of ports that are exposed by this service. More info: http://kubernetes.io/docs/user-guide/services#virtual-ips-and-service-proxies

        :return: The ports of this V1ServiceSpec.
        :rtype: list[V1ServicePort]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """
        Sets the ports of this V1ServiceSpec.
        The list of ports that are exposed by this service. More info: http://kubernetes.io/docs/user-guide/services#virtual-ips-and-service-proxies

        :param ports: The ports of this V1ServiceSpec.
        :type: list[V1ServicePort]
        """
        if ports is None:
            raise ValueError("Invalid value for `ports`, must not be `None`")

        self._ports = ports

    @property
    def selector(self):
        """
        Gets the selector of this V1ServiceSpec.
        Route service traffic to pods with label keys and values matching this selector. If empty or not present, the service is assumed to have an external process managing its endpoints, which Kubernetes will not modify. Only applies to types ClusterIP, NodePort, and LoadBalancer. Ignored if type is ExternalName. More info: http://kubernetes.io/docs/user-guide/services#overview

        :return: The selector of this V1ServiceSpec.
        :rtype: dict(str, str)
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """
        Sets the selector of this V1ServiceSpec.
        Route service traffic to pods with label keys and values matching this selector. If empty or not present, the service is assumed to have an external process managing its endpoints, which Kubernetes will not modify. Only applies to types ClusterIP, NodePort, and LoadBalancer. Ignored if type is ExternalName. More info: http://kubernetes.io/docs/user-guide/services#overview

        :param selector: The selector of this V1ServiceSpec.
        :type: dict(str, str)
        """

        self._selector = selector

    @property
    def session_affinity(self):
        """
        Gets the session_affinity of this V1ServiceSpec.
        Supports \"ClientIP\" and \"None\". Used to maintain session affinity. Enable client IP based session affinity. Must be ClientIP or None. Defaults to None. More info: http://kubernetes.io/docs/user-guide/services#virtual-ips-and-service-proxies

        :return: The session_affinity of this V1ServiceSpec.
        :rtype: str
        """
        return self._session_affinity

    @session_affinity.setter
    def session_affinity(self, session_affinity):
        """
        Sets the session_affinity of this V1ServiceSpec.
        Supports \"ClientIP\" and \"None\". Used to maintain session affinity. Enable client IP based session affinity. Must be ClientIP or None. Defaults to None. More info: http://kubernetes.io/docs/user-guide/services#virtual-ips-and-service-proxies

        :param session_affinity: The session_affinity of this V1ServiceSpec.
        :type: str
        """

        self._session_affinity = session_affinity

    @property
    def type(self):
        """
        Gets the type of this V1ServiceSpec.
        type determines how the Service is exposed. Defaults to ClusterIP. Valid options are ExternalName, ClusterIP, NodePort, and LoadBalancer. \"ExternalName\" maps to the specified externalName. \"ClusterIP\" allocates a cluster-internal IP address for load-balancing to endpoints. Endpoints are determined by the selector or if that is not specified, by manual construction of an Endpoints object. If clusterIP is \"None\", no virtual IP is allocated and the endpoints are published as a set of endpoints rather than a stable IP. \"NodePort\" builds on ClusterIP and allocates a port on every node which routes to the clusterIP. \"LoadBalancer\" builds on NodePort and creates an external load-balancer (if supported in the current cloud) which routes to the clusterIP. More info: http://kubernetes.io/docs/user-guide/services#overview

        :return: The type of this V1ServiceSpec.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1ServiceSpec.
        type determines how the Service is exposed. Defaults to ClusterIP. Valid options are ExternalName, ClusterIP, NodePort, and LoadBalancer. \"ExternalName\" maps to the specified externalName. \"ClusterIP\" allocates a cluster-internal IP address for load-balancing to endpoints. Endpoints are determined by the selector or if that is not specified, by manual construction of an Endpoints object. If clusterIP is \"None\", no virtual IP is allocated and the endpoints are published as a set of endpoints rather than a stable IP. \"NodePort\" builds on ClusterIP and allocates a port on every node which routes to the clusterIP. \"LoadBalancer\" builds on NodePort and creates an external load-balancer (if supported in the current cloud) which routes to the clusterIP. More info: http://kubernetes.io/docs/user-guide/services#overview

        :param type: The type of this V1ServiceSpec.
        :type: str
        """

        self._type = type

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
