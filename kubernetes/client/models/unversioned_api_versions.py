# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.5.0-snapshot
    
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


class UnversionedAPIVersions(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, server_address_by_client_cid_rs=None, versions=None):
        """
        UnversionedAPIVersions - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'server_address_by_client_cid_rs': 'list[UnversionedServerAddressByClientCIDR]',
            'versions': 'list[str]'
        }

        self.attribute_map = {
            'server_address_by_client_cid_rs': 'serverAddressByClientCIDRs',
            'versions': 'versions'
        }

        self._server_address_by_client_cid_rs = server_address_by_client_cid_rs
        self._versions = versions


    @property
    def server_address_by_client_cid_rs(self):
        """
        Gets the server_address_by_client_cid_rs of this UnversionedAPIVersions.
        a map of client CIDR to server address that is serving this group. This is to help clients reach servers in the most network-efficient way possible. Clients can use the appropriate server address as per the CIDR that they match. In case of multiple matches, clients should use the longest matching CIDR. The server returns only those CIDRs that it thinks that the client can match. For example: the master will return an internal IP CIDR only, if the client reaches the server using an internal IP. Server looks at X-Forwarded-For header or X-Real-Ip header or request.RemoteAddr (in that order) to get the client IP.

        :return: The server_address_by_client_cid_rs of this UnversionedAPIVersions.
        :rtype: list[UnversionedServerAddressByClientCIDR]
        """
        return self._server_address_by_client_cid_rs

    @server_address_by_client_cid_rs.setter
    def server_address_by_client_cid_rs(self, server_address_by_client_cid_rs):
        """
        Sets the server_address_by_client_cid_rs of this UnversionedAPIVersions.
        a map of client CIDR to server address that is serving this group. This is to help clients reach servers in the most network-efficient way possible. Clients can use the appropriate server address as per the CIDR that they match. In case of multiple matches, clients should use the longest matching CIDR. The server returns only those CIDRs that it thinks that the client can match. For example: the master will return an internal IP CIDR only, if the client reaches the server using an internal IP. Server looks at X-Forwarded-For header or X-Real-Ip header or request.RemoteAddr (in that order) to get the client IP.

        :param server_address_by_client_cid_rs: The server_address_by_client_cid_rs of this UnversionedAPIVersions.
        :type: list[UnversionedServerAddressByClientCIDR]
        """
        if server_address_by_client_cid_rs is None:
            raise ValueError("Invalid value for `server_address_by_client_cid_rs`, must not be `None`")

        self._server_address_by_client_cid_rs = server_address_by_client_cid_rs

    @property
    def versions(self):
        """
        Gets the versions of this UnversionedAPIVersions.
        versions are the api versions that are available.

        :return: The versions of this UnversionedAPIVersions.
        :rtype: list[str]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """
        Sets the versions of this UnversionedAPIVersions.
        versions are the api versions that are available.

        :param versions: The versions of this UnversionedAPIVersions.
        :type: list[str]
        """
        if versions is None:
            raise ValueError("Invalid value for `versions`, must not be `None`")

        self._versions = versions

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
