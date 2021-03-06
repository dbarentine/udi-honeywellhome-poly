# coding: utf-8

"""
    Honeywell Home

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ThermostatSettingsHardwareSettings(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'brightness': 'int',
        'max_brightness': 'int'
    }

    attribute_map = {
        'brightness': 'brightness',
        'max_brightness': 'maxBrightness'
    }

    def __init__(self, brightness=None, max_brightness=None):  # noqa: E501
        """ThermostatSettingsHardwareSettings - a model defined in OpenAPI"""  # noqa: E501

        self._brightness = None
        self._max_brightness = None
        self.discriminator = None

        if brightness is not None:
            self.brightness = brightness
        if max_brightness is not None:
            self.max_brightness = max_brightness

    @property
    def brightness(self):
        """Gets the brightness of this ThermostatSettingsHardwareSettings.  # noqa: E501


        :return: The brightness of this ThermostatSettingsHardwareSettings.  # noqa: E501
        :rtype: int
        """
        return self._brightness

    @brightness.setter
    def brightness(self, brightness):
        """Sets the brightness of this ThermostatSettingsHardwareSettings.


        :param brightness: The brightness of this ThermostatSettingsHardwareSettings.  # noqa: E501
        :type: int
        """

        self._brightness = brightness

    @property
    def max_brightness(self):
        """Gets the max_brightness of this ThermostatSettingsHardwareSettings.  # noqa: E501


        :return: The max_brightness of this ThermostatSettingsHardwareSettings.  # noqa: E501
        :rtype: int
        """
        return self._max_brightness

    @max_brightness.setter
    def max_brightness(self, max_brightness):
        """Sets the max_brightness of this ThermostatSettingsHardwareSettings.


        :param max_brightness: The max_brightness of this ThermostatSettingsHardwareSettings.  # noqa: E501
        :type: int
        """

        self._max_brightness = max_brightness

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ThermostatSettingsHardwareSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
