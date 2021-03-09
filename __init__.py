"""Chilicon Cloud integration."""
from datetime import datetime as dt

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    CONF_PASSWORD,
    CONF_USERNAME,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers import aiohttp_client

from .const import ( # pylint: disable=unused-import
    CONF_INSTALLATION_HASH,
    DOMAIN,
    ROOT_URL,
    LOGIN_URL,
    INSTALLATION_URL,
    UPDATE_URL,
)

#async def async_setup(hass,config):
#        """hello world"""
#        hass.states.async_set('chiliconcloud.current_production', 'unknown')
#
#        return True
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    if await hass.config_entries.async_forward_entry_unload(entry, "sensor"):
        hass.data[DOMAIN].pop(entry.entry_id)
        return True

    return False