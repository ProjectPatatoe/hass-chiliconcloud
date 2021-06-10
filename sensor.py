"""power generation sensor for chilicon cloud"""
import logging
import re
import requests
import voluptuous as vol

from homeassistant.const import (
    CONF_USERNAME,
    CONF_PASSWORD,
    ENERGY_WATT_HOUR,
    POWER_WATT,
)
from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv

DOMAIN = "chiliconcloud"
CONF_INSTALLATION_HASH = "installation_hash"
ROOT_URL = 'https://cloud.chiliconpower.com'
LOGIN_URL = ROOT_URL + '/login'
INSTALLATION_URL = ROOT_URL + '/installation/' #and then hash
UPDATE_URL = ROOT_URL + '/ajax/fetchOwnerUpdate' #and then ?today=2020-01-23

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_USERNAME): cv.string,
        vol.Required(CONF_PASSWORD): cv.string,
        vol.Required(CONF_INSTALLATION_HASH): cv.string,
    }
)

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the sensor platform."""
    add_entities([ChiliconCloudSensor()])


class ChiliconCloudSensor(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = None
        _LOGGER.info("chili_username: %s" % CONF_USERNAME)
        _LOGGER.info("chili_hash: %s" % CONF_INSTALLATION_HASH)

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Chilicon Cloud'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return POWER_WATT

    def update(self):
        """Fetch new state data for the sensor.
        This is the only method that should fetch new data for Home Assistant.
        """
        
        self._state = 23