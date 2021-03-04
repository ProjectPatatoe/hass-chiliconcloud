"""Chilicon Cloud integration."""

import asyncio
import logging

import voluptuous as vol

from homeassistant.helpers import config_validation as cv

#from homeassistant.config_entries import ConfigEntry
#from homeassistant.const import (
#       CONF_USERNAME,
#       CONF_PASSWORD,
#       CONF_INSTALLATION_HASH,
#)

from .const import (
        DOMAIN,
        CONF_USERNAME,
        CONF_PASSWORD,
        CONF_INSTALLATION_HASH,
        ROOT_URL,
        LOGIN_URL,
        INSTALLATION_URL,
        UPDATE_URL,
)
#DOMAIN = "chiliconcloud"

#python voluptuous for config validation?
CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                vol.Required(CONF_USERNAME): cv.string,
                vol.Required(CONF_PASSWORD): cv.string,
                vol.Required(CONF_INSTALLATION_HASH): cv.string,
            }
        )
    },
    extra=vol.ALLOW_EXTRA,
)

async def async_setup(hass,config):
        """hello world"""
        hass.states.async_set('hello_world.Hello_World', 'hihihi')

        return True
