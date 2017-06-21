# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V2alpha1HorizontalPodAutoscalerStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, current_metrics=None, current_replicas=None, desired_replicas=None, last_scale_time=None, observed_generation=None):
        """
        V2alpha1HorizontalPodAutoscalerStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'current_metrics': 'list[V2alpha1MetricStatus]',
            'current_replicas': 'int',
            'desired_replicas': 'int',
            'last_scale_time': 'datetime',
            'observed_generation': 'int'
        }

        self.attribute_map = {
            'current_metrics': 'currentMetrics',
            'current_replicas': 'currentReplicas',
            'desired_replicas': 'desiredReplicas',
            'last_scale_time': 'lastScaleTime',
            'observed_generation': 'observedGeneration'
        }

        self._current_metrics = current_metrics
        self._current_replicas = current_replicas
        self._desired_replicas = desired_replicas
        self._last_scale_time = last_scale_time
        self._observed_generation = observed_generation

    @property
    def current_metrics(self):
        """
        Gets the current_metrics of this V2alpha1HorizontalPodAutoscalerStatus.
        currentMetrics is the last read state of the metrics used by this autoscaler.

        :return: The current_metrics of this V2alpha1HorizontalPodAutoscalerStatus.
        :rtype: list[V2alpha1MetricStatus]
        """
        return self._current_metrics

    @current_metrics.setter
    def current_metrics(self, current_metrics):
        """
        Sets the current_metrics of this V2alpha1HorizontalPodAutoscalerStatus.
        currentMetrics is the last read state of the metrics used by this autoscaler.

        :param current_metrics: The current_metrics of this V2alpha1HorizontalPodAutoscalerStatus.
        :type: list[V2alpha1MetricStatus]
        """
        if current_metrics is None:
            raise ValueError("Invalid value for `current_metrics`, must not be `None`")

        self._current_metrics = current_metrics

    @property
    def current_replicas(self):
        """
        Gets the current_replicas of this V2alpha1HorizontalPodAutoscalerStatus.
        currentReplicas is current number of replicas of pods managed by this autoscaler, as last seen by the autoscaler.

        :return: The current_replicas of this V2alpha1HorizontalPodAutoscalerStatus.
        :rtype: int
        """
        return self._current_replicas

    @current_replicas.setter
    def current_replicas(self, current_replicas):
        """
        Sets the current_replicas of this V2alpha1HorizontalPodAutoscalerStatus.
        currentReplicas is current number of replicas of pods managed by this autoscaler, as last seen by the autoscaler.

        :param current_replicas: The current_replicas of this V2alpha1HorizontalPodAutoscalerStatus.
        :type: int
        """
        if current_replicas is None:
            raise ValueError("Invalid value for `current_replicas`, must not be `None`")

        self._current_replicas = current_replicas

    @property
    def desired_replicas(self):
        """
        Gets the desired_replicas of this V2alpha1HorizontalPodAutoscalerStatus.
        desiredReplicas is the desired number of replicas of pods managed by this autoscaler, as last calculated by the autoscaler.

        :return: The desired_replicas of this V2alpha1HorizontalPodAutoscalerStatus.
        :rtype: int
        """
        return self._desired_replicas

    @desired_replicas.setter
    def desired_replicas(self, desired_replicas):
        """
        Sets the desired_replicas of this V2alpha1HorizontalPodAutoscalerStatus.
        desiredReplicas is the desired number of replicas of pods managed by this autoscaler, as last calculated by the autoscaler.

        :param desired_replicas: The desired_replicas of this V2alpha1HorizontalPodAutoscalerStatus.
        :type: int
        """
        if desired_replicas is None:
            raise ValueError("Invalid value for `desired_replicas`, must not be `None`")

        self._desired_replicas = desired_replicas

    @property
    def last_scale_time(self):
        """
        Gets the last_scale_time of this V2alpha1HorizontalPodAutoscalerStatus.
        lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods, used by the autoscaler to control how often the number of pods is changed.

        :return: The last_scale_time of this V2alpha1HorizontalPodAutoscalerStatus.
        :rtype: datetime
        """
        return self._last_scale_time

    @last_scale_time.setter
    def last_scale_time(self, last_scale_time):
        """
        Sets the last_scale_time of this V2alpha1HorizontalPodAutoscalerStatus.
        lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods, used by the autoscaler to control how often the number of pods is changed.

        :param last_scale_time: The last_scale_time of this V2alpha1HorizontalPodAutoscalerStatus.
        :type: datetime
        """

        self._last_scale_time = last_scale_time

    @property
    def observed_generation(self):
        """
        Gets the observed_generation of this V2alpha1HorizontalPodAutoscalerStatus.
        observedGeneration is the most recent generation observed by this autoscaler.

        :return: The observed_generation of this V2alpha1HorizontalPodAutoscalerStatus.
        :rtype: int
        """
        return self._observed_generation

    @observed_generation.setter
    def observed_generation(self, observed_generation):
        """
        Sets the observed_generation of this V2alpha1HorizontalPodAutoscalerStatus.
        observedGeneration is the most recent generation observed by this autoscaler.

        :param observed_generation: The observed_generation of this V2alpha1HorizontalPodAutoscalerStatus.
        :type: int
        """

        self._observed_generation = observed_generation

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
        if not isinstance(other, V2alpha1HorizontalPodAutoscalerStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
