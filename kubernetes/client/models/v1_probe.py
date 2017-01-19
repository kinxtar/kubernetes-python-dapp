# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.5.1-660c2a2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1Probe(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, _exec=None, failure_threshold=None, http_get=None, initial_delay_seconds=None, period_seconds=None, success_threshold=None, tcp_socket=None, timeout_seconds=None):
        """
        V1Probe - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            '_exec': 'V1ExecAction',
            'failure_threshold': 'int',
            'http_get': 'V1HTTPGetAction',
            'initial_delay_seconds': 'int',
            'period_seconds': 'int',
            'success_threshold': 'int',
            'tcp_socket': 'V1TCPSocketAction',
            'timeout_seconds': 'int'
        }

        self.attribute_map = {
            '_exec': 'exec',
            'failure_threshold': 'failureThreshold',
            'http_get': 'httpGet',
            'initial_delay_seconds': 'initialDelaySeconds',
            'period_seconds': 'periodSeconds',
            'success_threshold': 'successThreshold',
            'tcp_socket': 'tcpSocket',
            'timeout_seconds': 'timeoutSeconds'
        }

        self.__exec = _exec
        self._failure_threshold = failure_threshold
        self._http_get = http_get
        self._initial_delay_seconds = initial_delay_seconds
        self._period_seconds = period_seconds
        self._success_threshold = success_threshold
        self._tcp_socket = tcp_socket
        self._timeout_seconds = timeout_seconds

    @property
    def _exec(self):
        """
        Gets the _exec of this V1Probe.
        One and only one of the following should be specified. Exec specifies the action to take.

        :return: The _exec of this V1Probe.
        :rtype: V1ExecAction
        """
        return self.__exec

    @_exec.setter
    def _exec(self, _exec):
        """
        Sets the _exec of this V1Probe.
        One and only one of the following should be specified. Exec specifies the action to take.

        :param _exec: The _exec of this V1Probe.
        :type: V1ExecAction
        """

        self.__exec = _exec

    @property
    def failure_threshold(self):
        """
        Gets the failure_threshold of this V1Probe.
        Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.

        :return: The failure_threshold of this V1Probe.
        :rtype: int
        """
        return self._failure_threshold

    @failure_threshold.setter
    def failure_threshold(self, failure_threshold):
        """
        Sets the failure_threshold of this V1Probe.
        Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.

        :param failure_threshold: The failure_threshold of this V1Probe.
        :type: int
        """

        self._failure_threshold = failure_threshold

    @property
    def http_get(self):
        """
        Gets the http_get of this V1Probe.
        HTTPGet specifies the http request to perform.

        :return: The http_get of this V1Probe.
        :rtype: V1HTTPGetAction
        """
        return self._http_get

    @http_get.setter
    def http_get(self, http_get):
        """
        Sets the http_get of this V1Probe.
        HTTPGet specifies the http request to perform.

        :param http_get: The http_get of this V1Probe.
        :type: V1HTTPGetAction
        """

        self._http_get = http_get

    @property
    def initial_delay_seconds(self):
        """
        Gets the initial_delay_seconds of this V1Probe.
        Number of seconds after the container has started before liveness probes are initiated. More info: http://kubernetes.io/docs/user-guide/pod-states#container-probes

        :return: The initial_delay_seconds of this V1Probe.
        :rtype: int
        """
        return self._initial_delay_seconds

    @initial_delay_seconds.setter
    def initial_delay_seconds(self, initial_delay_seconds):
        """
        Sets the initial_delay_seconds of this V1Probe.
        Number of seconds after the container has started before liveness probes are initiated. More info: http://kubernetes.io/docs/user-guide/pod-states#container-probes

        :param initial_delay_seconds: The initial_delay_seconds of this V1Probe.
        :type: int
        """

        self._initial_delay_seconds = initial_delay_seconds

    @property
    def period_seconds(self):
        """
        Gets the period_seconds of this V1Probe.
        How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.

        :return: The period_seconds of this V1Probe.
        :rtype: int
        """
        return self._period_seconds

    @period_seconds.setter
    def period_seconds(self, period_seconds):
        """
        Sets the period_seconds of this V1Probe.
        How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.

        :param period_seconds: The period_seconds of this V1Probe.
        :type: int
        """

        self._period_seconds = period_seconds

    @property
    def success_threshold(self):
        """
        Gets the success_threshold of this V1Probe.
        Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness. Minimum value is 1.

        :return: The success_threshold of this V1Probe.
        :rtype: int
        """
        return self._success_threshold

    @success_threshold.setter
    def success_threshold(self, success_threshold):
        """
        Sets the success_threshold of this V1Probe.
        Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness. Minimum value is 1.

        :param success_threshold: The success_threshold of this V1Probe.
        :type: int
        """

        self._success_threshold = success_threshold

    @property
    def tcp_socket(self):
        """
        Gets the tcp_socket of this V1Probe.
        TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported

        :return: The tcp_socket of this V1Probe.
        :rtype: V1TCPSocketAction
        """
        return self._tcp_socket

    @tcp_socket.setter
    def tcp_socket(self, tcp_socket):
        """
        Sets the tcp_socket of this V1Probe.
        TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported

        :param tcp_socket: The tcp_socket of this V1Probe.
        :type: V1TCPSocketAction
        """

        self._tcp_socket = tcp_socket

    @property
    def timeout_seconds(self):
        """
        Gets the timeout_seconds of this V1Probe.
        Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: http://kubernetes.io/docs/user-guide/pod-states#container-probes

        :return: The timeout_seconds of this V1Probe.
        :rtype: int
        """
        return self._timeout_seconds

    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds):
        """
        Sets the timeout_seconds of this V1Probe.
        Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: http://kubernetes.io/docs/user-guide/pod-states#container-probes

        :param timeout_seconds: The timeout_seconds of this V1Probe.
        :type: int
        """

        self._timeout_seconds = timeout_seconds

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
