#!/usr/bin/env python3
from thermostat import Thermostat
from indoor_air_sensor import IndoorAirSensor

try:
    import polyinterface
except ImportError:
    import pgc_interface as polyinterface

import sys
import os

from api_helper import ApiHelper

LOGGER = polyinterface.LOGGER


class Controller(polyinterface.Controller):
    def __init__(self, polyglot):
        super(Controller, self).__init__(polyglot)
        self.name = "Honeywell Home Controller"
        self._client_id = ""
        self._client_secret = ""
        self._user_id = ""
        self._api_baseurl = "https://api.honeywell.com"
        self._api = None

        # Don't enable in deployed node server. I use these so I can run/debug directly in IntelliJ.
        LOGGER.debug("Profile Num: " + os.environ.get('PROFILE_NUM'))
        LOGGER.debug("MQTT Host: " + os.environ.get('MQTT_HOST'))
        LOGGER.debug("MQTT Port: " + os.environ.get('MQTT_PORT'))
        LOGGER.debug("Token: " + os.environ.get('TOKEN'))

    def start(self):
        LOGGER.info('Started Honeywell Home Nodeserver')
        if self.check_params():
            self._api = ApiHelper(self._api_baseurl, self._client_id, self._client_secret, self._user_id)
            self.discover()
            self.setDriver('ST', 1)

    def shortPoll(self):
        pass

    def longPoll(self):
        self.query()

    def query(self):
        for node in self.nodes:
            if self.nodes[node] is not self:
                self.nodes[node].query()

            self.nodes[node].reportDrivers()

    def discover(self, *args, **kwargs):
        try:
            LOGGER.debug("Starting discovery")
            # If this is a re-discover than update=True
            update = len(args) > 0

            locations = self._api.get_locations()
            for location in locations:
                if location.devices is None:
                    LOGGER.warn("There were no devices for location {0}", location.name)
                    continue

                for thermostat in location.devices:
                    self.add_thermostat(location.location_id, location.name, thermostat, update)

            LOGGER.info("Discovery Finished")
        except Exception as ex:
            self.addNotice({'discovery_failed': 'Discovery failed please check logs for a more detailed error.'})
            LOGGER.exception("Discovery failed with error %s", ex)

    def add_thermostat(self, location_id, location_name, thermostat, update):
        t_name = location_name + ' - ' + thermostat['userDefinedDeviceName']
        t_device_id = thermostat['deviceID']
        t_addr = thermostat['macID'].lower()
        use_celsius = thermostat['units'].lower() != 'fahrenheit'

        LOGGER.debug('Adding thermostat with id {0} and name {1} and addr {2}'.format(t_device_id, t_name, t_addr))
        self.addNode(Thermostat(self, t_addr, t_addr, t_name, self._api, location_id, t_device_id, use_celsius), update)

        if 'groups' not in thermostat:
            return

        for group in thermostat['groups']:
            group_id = group['id']

            sensors = self._api.get_sensors(location_id, t_device_id, group_id)
            for sensor in sensors.rooms:
                if len(sensor.accessories) == 0:
                    continue

                # TODO: Do we ever have to care about multiple accessory blocks?
                sensor_type = sensor.accessories[0].accessory_attribute.type
                sensor_name = sensor.name
                sensor_addr = t_addr + str(group_id) + str(sensor.id)

                if sensor_type == 'IndoorAirSensor' or sensor_type == 'Thermostat':
                    LOGGER.debug('Adding IndoorAirSensor with name {0} and addr {1} for thermostat {2}'.format(sensor_name, sensor_addr, t_addr))
                    self.addNode(IndoorAirSensor(self, t_addr, sensor_addr, sensor_name, self._api, location_id, t_device_id, group_id, sensor.id, use_celsius))

    def delete(self):
        LOGGER.info('Honeywell Home NS Deleted')

    def stop(self):
        LOGGER.debug('Honeywell Home NS stopped.')

    def check_params(self):
        if 'client_id' in self.polyConfig['customParams']:
            self._client_id = self.polyConfig['customParams']['client_id']
        else:
            LOGGER.error('check_params: client_id not defined in customParams, please add it.  Using {}'.format(self._client_id))

        if 'client_secret' in self.polyConfig['customParams']:
            self._client_secret = self.polyConfig['customParams']['client_secret']
        else:
            LOGGER.error('check_params: client_secret not defined in customParams, please add it.  Using {}'.format(self._client_secret))

        if 'user_id' in self.polyConfig['customParams']:
            self._user_id = self.polyConfig['customParams']['user_id']
        else:
            LOGGER.error('check_params: user_id not defined in customParams, please add it.  Using {}'.format(self._user_id))

        # Make sure they are in the params
        self.addCustomParam({'client_id': self._client_id, 'client_secret': self._client_secret, "user_id": self._user_id})

        # Remove all existing notices
        self.removeNoticesAll()
        # Add a notice if they need to change the user/password from the default.
        if self._client_id == "" or self._client_secret == "" or self._user_id == "":
            self.addNotice({'mynotice': 'Please set proper client_id and client_secret in configuration page, and restart this nodeserver. See:<br />https://github.com/dbarentine/udi-honeywellhome-poly/blob/master/README.md'})
            return False
        else:
            return True

    def remove_notices_all(self, command):
        LOGGER.info('remove_notices_all:')
        # Remove all existing notices
        self.removeNoticesAll()

    def update_profile(self, command):
        LOGGER.info('update_profile:')
        st = self.poly.installprofile()
        return st

    id = 'controller'
    commands = {
        'DISCOVER': discover,
        'UPDATE_PROFILE': update_profile,
        'REMOVE_NOTICES_ALL': remove_notices_all
    }

    drivers = [{'driver': 'ST', 'value': 0, 'uom': 2}]


if __name__ == "__main__":
    try:
        polyglot = polyinterface.Interface('HoneywellHome')
        polyglot.start()
        control = Controller(polyglot)
        control.runForever()
    except (KeyboardInterrupt, SystemExit):
        sys.exit(0)
