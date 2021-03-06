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


class Thermostat(object):
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
        'groups': 'list[ThermostatGroups]',
        'displayed_outdoor_humidity': 'int',
        'vacation_hold': 'ThermostatVacationHold',
        'current_schedule_period': 'ThermostatCurrentSchedulePeriod',
        'schedule_capabilities': 'ThermostatScheduleCapabilities',
        'schedule_type': 'ThermostatScheduleType',
        'schedule_status': 'str',
        'allowed_time_increments': 'int',
        'settings': 'ThermostatSettings',
        'device_class': 'str',
        'device_type': 'str',
        'device_id': 'str',
        'user_defined_device_name': 'str',
        'name': 'str',
        'is_alive': 'bool',
        'is_upgrading': 'bool',
        'is_provisioned': 'bool',
        'mac_id': 'str',
        'device_settings': 'object',
        'units': 'str',
        'indoor_temperature': 'float',
        'outdoor_temperature': 'float',
        'allowed_modes': 'list[str]',
        'deadband': 'float',
        'has_dual_setpoint_status': 'bool',
        'min_heat_setpoint': 'float',
        'max_heat_setpoint': 'float',
        'min_cool_setpoint': 'float',
        'max_cool_setpoint': 'float',
        'indoor_humidity': 'int',
        'indoor_humidity_status': 'str',
        'device_model': 'str',
        'changeable_values': 'ThermostatChangeableValues',
        'operation_status': 'ThermostatOperationStatus',
        'priority_type': 'str'
    }

    attribute_map = {
        'groups': 'groups',
        'displayed_outdoor_humidity': 'displayedOutdoorHumidity',
        'vacation_hold': 'vacationHold',
        'current_schedule_period': 'currentSchedulePeriod',
        'schedule_capabilities': 'scheduleCapabilities',
        'schedule_type': 'scheduleType',
        'schedule_status': 'scheduleStatus',
        'allowed_time_increments': 'allowedTimeIncrements',
        'settings': 'settings',
        'device_class': 'deviceClass',
        'device_type': 'deviceType',
        'device_id': 'deviceID',
        'user_defined_device_name': 'userDefinedDeviceName',
        'name': 'name',
        'is_alive': 'isAlive',
        'is_upgrading': 'isUpgrading',
        'is_provisioned': 'isProvisioned',
        'mac_id': 'macID',
        'device_settings': 'deviceSettings',
        'units': 'units',
        'indoor_temperature': 'indoorTemperature',
        'outdoor_temperature': 'outdoorTemperature',
        'allowed_modes': 'allowedModes',
        'deadband': 'deadband',
        'has_dual_setpoint_status': 'hasDualSetpointStatus',
        'min_heat_setpoint': 'minHeatSetpoint',
        'max_heat_setpoint': 'maxHeatSetpoint',
        'min_cool_setpoint': 'minCoolSetpoint',
        'max_cool_setpoint': 'maxCoolSetpoint',
        'indoor_humidity': 'indoorHumidity',
        'indoor_humidity_status': 'indoorHumidityStatus',
        'device_model': 'deviceModel',
        'changeable_values': 'changeableValues',
        'operation_status': 'operationStatus',
        'priority_type': 'priorityType'
    }

    def __init__(self, groups=None, displayed_outdoor_humidity=None, vacation_hold=None, current_schedule_period=None, schedule_capabilities=None, schedule_type=None, schedule_status=None, allowed_time_increments=None, settings=None, device_class=None, device_type=None, device_id=None, user_defined_device_name=None, name=None, is_alive=None, is_upgrading=None, is_provisioned=None, mac_id=None, device_settings=None, units=None, indoor_temperature=None, outdoor_temperature=None, allowed_modes=None, deadband=None, has_dual_setpoint_status=None, min_heat_setpoint=None, max_heat_setpoint=None, min_cool_setpoint=None, max_cool_setpoint=None, indoor_humidity=None, indoor_humidity_status=None, device_model=None, changeable_values=None, operation_status=None, priority_type=None):  # noqa: E501
        """Thermostat - a model defined in OpenAPI"""  # noqa: E501

        self._groups = None
        self._displayed_outdoor_humidity = None
        self._vacation_hold = None
        self._current_schedule_period = None
        self._schedule_capabilities = None
        self._schedule_type = None
        self._schedule_status = None
        self._allowed_time_increments = None
        self._settings = None
        self._device_class = None
        self._device_type = None
        self._device_id = None
        self._user_defined_device_name = None
        self._name = None
        self._is_alive = None
        self._is_upgrading = None
        self._is_provisioned = None
        self._mac_id = None
        self._device_settings = None
        self._units = None
        self._indoor_temperature = None
        self._outdoor_temperature = None
        self._allowed_modes = None
        self._deadband = None
        self._has_dual_setpoint_status = None
        self._min_heat_setpoint = None
        self._max_heat_setpoint = None
        self._min_cool_setpoint = None
        self._max_cool_setpoint = None
        self._indoor_humidity = None
        self._indoor_humidity_status = None
        self._device_model = None
        self._changeable_values = None
        self._operation_status = None
        self._priority_type = None
        self.discriminator = None

        if groups is not None:
            self.groups = groups
        if displayed_outdoor_humidity is not None:
            self.displayed_outdoor_humidity = displayed_outdoor_humidity
        if vacation_hold is not None:
            self.vacation_hold = vacation_hold
        if current_schedule_period is not None:
            self.current_schedule_period = current_schedule_period
        if schedule_capabilities is not None:
            self.schedule_capabilities = schedule_capabilities
        if schedule_type is not None:
            self.schedule_type = schedule_type
        if schedule_status is not None:
            self.schedule_status = schedule_status
        if allowed_time_increments is not None:
            self.allowed_time_increments = allowed_time_increments
        if settings is not None:
            self.settings = settings
        if device_class is not None:
            self.device_class = device_class
        if device_type is not None:
            self.device_type = device_type
        if device_id is not None:
            self.device_id = device_id
        if user_defined_device_name is not None:
            self.user_defined_device_name = user_defined_device_name
        if name is not None:
            self.name = name
        if is_alive is not None:
            self.is_alive = is_alive
        if is_upgrading is not None:
            self.is_upgrading = is_upgrading
        if is_provisioned is not None:
            self.is_provisioned = is_provisioned
        if mac_id is not None:
            self.mac_id = mac_id
        if device_settings is not None:
            self.device_settings = device_settings
        if units is not None:
            self.units = units
        if indoor_temperature is not None:
            self.indoor_temperature = indoor_temperature
        if outdoor_temperature is not None:
            self.outdoor_temperature = outdoor_temperature
        if allowed_modes is not None:
            self.allowed_modes = allowed_modes
        if deadband is not None:
            self.deadband = deadband
        if has_dual_setpoint_status is not None:
            self.has_dual_setpoint_status = has_dual_setpoint_status
        if min_heat_setpoint is not None:
            self.min_heat_setpoint = min_heat_setpoint
        if max_heat_setpoint is not None:
            self.max_heat_setpoint = max_heat_setpoint
        if min_cool_setpoint is not None:
            self.min_cool_setpoint = min_cool_setpoint
        if max_cool_setpoint is not None:
            self.max_cool_setpoint = max_cool_setpoint
        if indoor_humidity is not None:
            self.indoor_humidity = indoor_humidity
        if indoor_humidity_status is not None:
            self.indoor_humidity_status = indoor_humidity_status
        if device_model is not None:
            self.device_model = device_model
        if changeable_values is not None:
            self.changeable_values = changeable_values
        if operation_status is not None:
            self.operation_status = operation_status
        if priority_type is not None:
            self.priority_type = priority_type

    @property
    def groups(self):
        """Gets the groups of this Thermostat.  # noqa: E501


        :return: The groups of this Thermostat.  # noqa: E501
        :rtype: list[ThermostatGroups]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this Thermostat.


        :param groups: The groups of this Thermostat.  # noqa: E501
        :type: list[ThermostatGroups]
        """

        self._groups = groups

    @property
    def displayed_outdoor_humidity(self):
        """Gets the displayed_outdoor_humidity of this Thermostat.  # noqa: E501


        :return: The displayed_outdoor_humidity of this Thermostat.  # noqa: E501
        :rtype: int
        """
        return self._displayed_outdoor_humidity

    @displayed_outdoor_humidity.setter
    def displayed_outdoor_humidity(self, displayed_outdoor_humidity):
        """Sets the displayed_outdoor_humidity of this Thermostat.


        :param displayed_outdoor_humidity: The displayed_outdoor_humidity of this Thermostat.  # noqa: E501
        :type: int
        """

        self._displayed_outdoor_humidity = displayed_outdoor_humidity

    @property
    def vacation_hold(self):
        """Gets the vacation_hold of this Thermostat.  # noqa: E501


        :return: The vacation_hold of this Thermostat.  # noqa: E501
        :rtype: ThermostatVacationHold
        """
        return self._vacation_hold

    @vacation_hold.setter
    def vacation_hold(self, vacation_hold):
        """Sets the vacation_hold of this Thermostat.


        :param vacation_hold: The vacation_hold of this Thermostat.  # noqa: E501
        :type: ThermostatVacationHold
        """

        self._vacation_hold = vacation_hold

    @property
    def current_schedule_period(self):
        """Gets the current_schedule_period of this Thermostat.  # noqa: E501


        :return: The current_schedule_period of this Thermostat.  # noqa: E501
        :rtype: ThermostatCurrentSchedulePeriod
        """
        return self._current_schedule_period

    @current_schedule_period.setter
    def current_schedule_period(self, current_schedule_period):
        """Sets the current_schedule_period of this Thermostat.


        :param current_schedule_period: The current_schedule_period of this Thermostat.  # noqa: E501
        :type: ThermostatCurrentSchedulePeriod
        """

        self._current_schedule_period = current_schedule_period

    @property
    def schedule_capabilities(self):
        """Gets the schedule_capabilities of this Thermostat.  # noqa: E501


        :return: The schedule_capabilities of this Thermostat.  # noqa: E501
        :rtype: ThermostatScheduleCapabilities
        """
        return self._schedule_capabilities

    @schedule_capabilities.setter
    def schedule_capabilities(self, schedule_capabilities):
        """Sets the schedule_capabilities of this Thermostat.


        :param schedule_capabilities: The schedule_capabilities of this Thermostat.  # noqa: E501
        :type: ThermostatScheduleCapabilities
        """

        self._schedule_capabilities = schedule_capabilities

    @property
    def schedule_type(self):
        """Gets the schedule_type of this Thermostat.  # noqa: E501


        :return: The schedule_type of this Thermostat.  # noqa: E501
        :rtype: ThermostatScheduleType
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """Sets the schedule_type of this Thermostat.


        :param schedule_type: The schedule_type of this Thermostat.  # noqa: E501
        :type: ThermostatScheduleType
        """

        self._schedule_type = schedule_type

    @property
    def schedule_status(self):
        """Gets the schedule_status of this Thermostat.  # noqa: E501


        :return: The schedule_status of this Thermostat.  # noqa: E501
        :rtype: str
        """
        return self._schedule_status

    @schedule_status.setter
    def schedule_status(self, schedule_status):
        """Sets the schedule_status of this Thermostat.


        :param schedule_status: The schedule_status of this Thermostat.  # noqa: E501
        :type: str
        """

        self._schedule_status = schedule_status

    @property
    def allowed_time_increments(self):
        """Gets the allowed_time_increments of this Thermostat.  # noqa: E501


        :return: The allowed_time_increments of this Thermostat.  # noqa: E501
        :rtype: int
        """
        return self._allowed_time_increments

    @allowed_time_increments.setter
    def allowed_time_increments(self, allowed_time_increments):
        """Sets the allowed_time_increments of this Thermostat.


        :param allowed_time_increments: The allowed_time_increments of this Thermostat.  # noqa: E501
        :type: int
        """

        self._allowed_time_increments = allowed_time_increments

    @property
    def settings(self):
        """Gets the settings of this Thermostat.  # noqa: E501


        :return: The settings of this Thermostat.  # noqa: E501
        :rtype: ThermostatSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this Thermostat.


        :param settings: The settings of this Thermostat.  # noqa: E501
        :type: ThermostatSettings
        """

        self._settings = settings

    @property
    def device_class(self):
        """Gets the device_class of this Thermostat.  # noqa: E501


        :return: The device_class of this Thermostat.  # noqa: E501
        :rtype: str
        """
        return self._device_class

    @device_class.setter
    def device_class(self, device_class):
        """Sets the device_class of this Thermostat.


        :param device_class: The device_class of this Thermostat.  # noqa: E501
        :type: str
        """

        self._device_class = device_class

    @property
    def device_type(self):
        """Gets the device_type of this Thermostat.  # noqa: E501


        :return: The device_type of this Thermostat.  # noqa: E501
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this Thermostat.


        :param device_type: The device_type of this Thermostat.  # noqa: E501
        :type: str
        """

        self._device_type = device_type

    @property
    def device_id(self):
        """Gets the device_id of this Thermostat.  # noqa: E501


        :return: The device_id of this Thermostat.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this Thermostat.


        :param device_id: The device_id of this Thermostat.  # noqa: E501
        :type: str
        """

        self._device_id = device_id

    @property
    def user_defined_device_name(self):
        """Gets the user_defined_device_name of this Thermostat.  # noqa: E501


        :return: The user_defined_device_name of this Thermostat.  # noqa: E501
        :rtype: str
        """
        return self._user_defined_device_name

    @user_defined_device_name.setter
    def user_defined_device_name(self, user_defined_device_name):
        """Sets the user_defined_device_name of this Thermostat.


        :param user_defined_device_name: The user_defined_device_name of this Thermostat.  # noqa: E501
        :type: str
        """

        self._user_defined_device_name = user_defined_device_name

    @property
    def name(self):
        """Gets the name of this Thermostat.  # noqa: E501


        :return: The name of this Thermostat.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Thermostat.


        :param name: The name of this Thermostat.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def is_alive(self):
        """Gets the is_alive of this Thermostat.  # noqa: E501


        :return: The is_alive of this Thermostat.  # noqa: E501
        :rtype: bool
        """
        return self._is_alive

    @is_alive.setter
    def is_alive(self, is_alive):
        """Sets the is_alive of this Thermostat.


        :param is_alive: The is_alive of this Thermostat.  # noqa: E501
        :type: bool
        """

        self._is_alive = is_alive

    @property
    def is_upgrading(self):
        """Gets the is_upgrading of this Thermostat.  # noqa: E501


        :return: The is_upgrading of this Thermostat.  # noqa: E501
        :rtype: bool
        """
        return self._is_upgrading

    @is_upgrading.setter
    def is_upgrading(self, is_upgrading):
        """Sets the is_upgrading of this Thermostat.


        :param is_upgrading: The is_upgrading of this Thermostat.  # noqa: E501
        :type: bool
        """

        self._is_upgrading = is_upgrading

    @property
    def is_provisioned(self):
        """Gets the is_provisioned of this Thermostat.  # noqa: E501


        :return: The is_provisioned of this Thermostat.  # noqa: E501
        :rtype: bool
        """
        return self._is_provisioned

    @is_provisioned.setter
    def is_provisioned(self, is_provisioned):
        """Sets the is_provisioned of this Thermostat.


        :param is_provisioned: The is_provisioned of this Thermostat.  # noqa: E501
        :type: bool
        """

        self._is_provisioned = is_provisioned

    @property
    def mac_id(self):
        """Gets the mac_id of this Thermostat.  # noqa: E501


        :return: The mac_id of this Thermostat.  # noqa: E501
        :rtype: str
        """
        return self._mac_id

    @mac_id.setter
    def mac_id(self, mac_id):
        """Sets the mac_id of this Thermostat.


        :param mac_id: The mac_id of this Thermostat.  # noqa: E501
        :type: str
        """

        self._mac_id = mac_id

    @property
    def device_settings(self):
        """Gets the device_settings of this Thermostat.  # noqa: E501


        :return: The device_settings of this Thermostat.  # noqa: E501
        :rtype: object
        """
        return self._device_settings

    @device_settings.setter
    def device_settings(self, device_settings):
        """Sets the device_settings of this Thermostat.


        :param device_settings: The device_settings of this Thermostat.  # noqa: E501
        :type: object
        """

        self._device_settings = device_settings

    @property
    def units(self):
        """Gets the units of this Thermostat.  # noqa: E501


        :return: The units of this Thermostat.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this Thermostat.


        :param units: The units of this Thermostat.  # noqa: E501
        :type: str
        """

        self._units = units

    @property
    def indoor_temperature(self):
        """Gets the indoor_temperature of this Thermostat.  # noqa: E501


        :return: The indoor_temperature of this Thermostat.  # noqa: E501
        :rtype: float
        """
        return self._indoor_temperature

    @indoor_temperature.setter
    def indoor_temperature(self, indoor_temperature):
        """Sets the indoor_temperature of this Thermostat.


        :param indoor_temperature: The indoor_temperature of this Thermostat.  # noqa: E501
        :type: float
        """

        self._indoor_temperature = indoor_temperature

    @property
    def outdoor_temperature(self):
        """Gets the outdoor_temperature of this Thermostat.  # noqa: E501


        :return: The outdoor_temperature of this Thermostat.  # noqa: E501
        :rtype: float
        """
        return self._outdoor_temperature

    @outdoor_temperature.setter
    def outdoor_temperature(self, outdoor_temperature):
        """Sets the outdoor_temperature of this Thermostat.


        :param outdoor_temperature: The outdoor_temperature of this Thermostat.  # noqa: E501
        :type: float
        """

        self._outdoor_temperature = outdoor_temperature

    @property
    def allowed_modes(self):
        """Gets the allowed_modes of this Thermostat.  # noqa: E501


        :return: The allowed_modes of this Thermostat.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_modes

    @allowed_modes.setter
    def allowed_modes(self, allowed_modes):
        """Sets the allowed_modes of this Thermostat.


        :param allowed_modes: The allowed_modes of this Thermostat.  # noqa: E501
        :type: list[str]
        """

        self._allowed_modes = allowed_modes

    @property
    def deadband(self):
        """Gets the deadband of this Thermostat.  # noqa: E501


        :return: The deadband of this Thermostat.  # noqa: E501
        :rtype: float
        """
        return self._deadband

    @deadband.setter
    def deadband(self, deadband):
        """Sets the deadband of this Thermostat.


        :param deadband: The deadband of this Thermostat.  # noqa: E501
        :type: float
        """

        self._deadband = deadband

    @property
    def has_dual_setpoint_status(self):
        """Gets the has_dual_setpoint_status of this Thermostat.  # noqa: E501


        :return: The has_dual_setpoint_status of this Thermostat.  # noqa: E501
        :rtype: bool
        """
        return self._has_dual_setpoint_status

    @has_dual_setpoint_status.setter
    def has_dual_setpoint_status(self, has_dual_setpoint_status):
        """Sets the has_dual_setpoint_status of this Thermostat.


        :param has_dual_setpoint_status: The has_dual_setpoint_status of this Thermostat.  # noqa: E501
        :type: bool
        """

        self._has_dual_setpoint_status = has_dual_setpoint_status

    @property
    def min_heat_setpoint(self):
        """Gets the min_heat_setpoint of this Thermostat.  # noqa: E501


        :return: The min_heat_setpoint of this Thermostat.  # noqa: E501
        :rtype: float
        """
        return self._min_heat_setpoint

    @min_heat_setpoint.setter
    def min_heat_setpoint(self, min_heat_setpoint):
        """Sets the min_heat_setpoint of this Thermostat.


        :param min_heat_setpoint: The min_heat_setpoint of this Thermostat.  # noqa: E501
        :type: float
        """

        self._min_heat_setpoint = min_heat_setpoint

    @property
    def max_heat_setpoint(self):
        """Gets the max_heat_setpoint of this Thermostat.  # noqa: E501


        :return: The max_heat_setpoint of this Thermostat.  # noqa: E501
        :rtype: float
        """
        return self._max_heat_setpoint

    @max_heat_setpoint.setter
    def max_heat_setpoint(self, max_heat_setpoint):
        """Sets the max_heat_setpoint of this Thermostat.


        :param max_heat_setpoint: The max_heat_setpoint of this Thermostat.  # noqa: E501
        :type: float
        """

        self._max_heat_setpoint = max_heat_setpoint

    @property
    def min_cool_setpoint(self):
        """Gets the min_cool_setpoint of this Thermostat.  # noqa: E501


        :return: The min_cool_setpoint of this Thermostat.  # noqa: E501
        :rtype: float
        """
        return self._min_cool_setpoint

    @min_cool_setpoint.setter
    def min_cool_setpoint(self, min_cool_setpoint):
        """Sets the min_cool_setpoint of this Thermostat.


        :param min_cool_setpoint: The min_cool_setpoint of this Thermostat.  # noqa: E501
        :type: float
        """

        self._min_cool_setpoint = min_cool_setpoint

    @property
    def max_cool_setpoint(self):
        """Gets the max_cool_setpoint of this Thermostat.  # noqa: E501


        :return: The max_cool_setpoint of this Thermostat.  # noqa: E501
        :rtype: float
        """
        return self._max_cool_setpoint

    @max_cool_setpoint.setter
    def max_cool_setpoint(self, max_cool_setpoint):
        """Sets the max_cool_setpoint of this Thermostat.


        :param max_cool_setpoint: The max_cool_setpoint of this Thermostat.  # noqa: E501
        :type: float
        """

        self._max_cool_setpoint = max_cool_setpoint

    @property
    def indoor_humidity(self):
        """Gets the indoor_humidity of this Thermostat.  # noqa: E501


        :return: The indoor_humidity of this Thermostat.  # noqa: E501
        :rtype: int
        """
        return self._indoor_humidity

    @indoor_humidity.setter
    def indoor_humidity(self, indoor_humidity):
        """Sets the indoor_humidity of this Thermostat.


        :param indoor_humidity: The indoor_humidity of this Thermostat.  # noqa: E501
        :type: int
        """

        self._indoor_humidity = indoor_humidity

    @property
    def indoor_humidity_status(self):
        """Gets the indoor_humidity_status of this Thermostat.  # noqa: E501


        :return: The indoor_humidity_status of this Thermostat.  # noqa: E501
        :rtype: str
        """
        return self._indoor_humidity_status

    @indoor_humidity_status.setter
    def indoor_humidity_status(self, indoor_humidity_status):
        """Sets the indoor_humidity_status of this Thermostat.


        :param indoor_humidity_status: The indoor_humidity_status of this Thermostat.  # noqa: E501
        :type: str
        """

        self._indoor_humidity_status = indoor_humidity_status

    @property
    def device_model(self):
        """Gets the device_model of this Thermostat.  # noqa: E501


        :return: The device_model of this Thermostat.  # noqa: E501
        :rtype: str
        """
        return self._device_model

    @device_model.setter
    def device_model(self, device_model):
        """Sets the device_model of this Thermostat.


        :param device_model: The device_model of this Thermostat.  # noqa: E501
        :type: str
        """

        self._device_model = device_model

    @property
    def changeable_values(self):
        """Gets the changeable_values of this Thermostat.  # noqa: E501


        :return: The changeable_values of this Thermostat.  # noqa: E501
        :rtype: ThermostatChangeableValues
        """
        return self._changeable_values

    @changeable_values.setter
    def changeable_values(self, changeable_values):
        """Sets the changeable_values of this Thermostat.


        :param changeable_values: The changeable_values of this Thermostat.  # noqa: E501
        :type: ThermostatChangeableValues
        """

        self._changeable_values = changeable_values

    @property
    def operation_status(self):
        """Gets the operation_status of this Thermostat.  # noqa: E501


        :return: The operation_status of this Thermostat.  # noqa: E501
        :rtype: ThermostatOperationStatus
        """
        return self._operation_status

    @operation_status.setter
    def operation_status(self, operation_status):
        """Sets the operation_status of this Thermostat.


        :param operation_status: The operation_status of this Thermostat.  # noqa: E501
        :type: ThermostatOperationStatus
        """

        self._operation_status = operation_status

    @property
    def priority_type(self):
        """Gets the priority_type of this Thermostat.  # noqa: E501


        :return: The priority_type of this Thermostat.  # noqa: E501
        :rtype: str
        """
        return self._priority_type

    @priority_type.setter
    def priority_type(self, priority_type):
        """Sets the priority_type of this Thermostat.


        :param priority_type: The priority_type of this Thermostat.  # noqa: E501
        :type: str
        """

        self._priority_type = priority_type

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
        if not isinstance(other, Thermostat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
