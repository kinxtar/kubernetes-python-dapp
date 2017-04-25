# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1SecurityContext(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, capabilities=None, privileged=None, read_only_root_filesystem=None, run_as_non_root=None, run_as_user=None, se_linux_options=None):
        """
        V1SecurityContext - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'capabilities': 'V1Capabilities',
            'privileged': 'bool',
            'read_only_root_filesystem': 'bool',
            'run_as_non_root': 'bool',
            'run_as_user': 'int',
            'se_linux_options': 'V1SELinuxOptions'
        }

        self.attribute_map = {
            'capabilities': 'capabilities',
            'privileged': 'privileged',
            'read_only_root_filesystem': 'readOnlyRootFilesystem',
            'run_as_non_root': 'runAsNonRoot',
            'run_as_user': 'runAsUser',
            'se_linux_options': 'seLinuxOptions'
        }

        self._capabilities = capabilities
        self._privileged = privileged
        self._read_only_root_filesystem = read_only_root_filesystem
        self._run_as_non_root = run_as_non_root
        self._run_as_user = run_as_user
        self._se_linux_options = se_linux_options

    @property
    def capabilities(self):
        """
        Gets the capabilities of this V1SecurityContext.
        The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime.

        :return: The capabilities of this V1SecurityContext.
        :rtype: V1Capabilities
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        """
        Sets the capabilities of this V1SecurityContext.
        The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime.

        :param capabilities: The capabilities of this V1SecurityContext.
        :type: V1Capabilities
        """

        self._capabilities = capabilities

    @property
    def privileged(self):
        """
        Gets the privileged of this V1SecurityContext.
        Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false.

        :return: The privileged of this V1SecurityContext.
        :rtype: bool
        """
        return self._privileged

    @privileged.setter
    def privileged(self, privileged):
        """
        Sets the privileged of this V1SecurityContext.
        Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false.

        :param privileged: The privileged of this V1SecurityContext.
        :type: bool
        """

        self._privileged = privileged

    @property
    def read_only_root_filesystem(self):
        """
        Gets the read_only_root_filesystem of this V1SecurityContext.
        Whether this container has a read-only root filesystem. Default is false.

        :return: The read_only_root_filesystem of this V1SecurityContext.
        :rtype: bool
        """
        return self._read_only_root_filesystem

    @read_only_root_filesystem.setter
    def read_only_root_filesystem(self, read_only_root_filesystem):
        """
        Sets the read_only_root_filesystem of this V1SecurityContext.
        Whether this container has a read-only root filesystem. Default is false.

        :param read_only_root_filesystem: The read_only_root_filesystem of this V1SecurityContext.
        :type: bool
        """

        self._read_only_root_filesystem = read_only_root_filesystem

    @property
    def run_as_non_root(self):
        """
        Gets the run_as_non_root of this V1SecurityContext.
        Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.

        :return: The run_as_non_root of this V1SecurityContext.
        :rtype: bool
        """
        return self._run_as_non_root

    @run_as_non_root.setter
    def run_as_non_root(self, run_as_non_root):
        """
        Sets the run_as_non_root of this V1SecurityContext.
        Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.

        :param run_as_non_root: The run_as_non_root of this V1SecurityContext.
        :type: bool
        """

        self._run_as_non_root = run_as_non_root

    @property
    def run_as_user(self):
        """
        Gets the run_as_user of this V1SecurityContext.
        The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.

        :return: The run_as_user of this V1SecurityContext.
        :rtype: int
        """
        return self._run_as_user

    @run_as_user.setter
    def run_as_user(self, run_as_user):
        """
        Sets the run_as_user of this V1SecurityContext.
        The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.

        :param run_as_user: The run_as_user of this V1SecurityContext.
        :type: int
        """

        self._run_as_user = run_as_user

    @property
    def se_linux_options(self):
        """
        Gets the se_linux_options of this V1SecurityContext.
        The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.

        :return: The se_linux_options of this V1SecurityContext.
        :rtype: V1SELinuxOptions
        """
        return self._se_linux_options

    @se_linux_options.setter
    def se_linux_options(self, se_linux_options):
        """
        Sets the se_linux_options of this V1SecurityContext.
        The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.

        :param se_linux_options: The se_linux_options of this V1SecurityContext.
        :type: V1SELinuxOptions
        """

        self._se_linux_options = se_linux_options

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
