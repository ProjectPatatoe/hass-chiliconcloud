"""Chilicon Cloud Config flow"""
import voluptuous as vol
import logging
import asyncio

from homeassistant import config_entries, exceptions
from homeassistant.helpers import aiohttp_client


_LOGGER = logging.getLogger(__name__)

from homeassistant.const import (
    CONF_USERNAME,
    CONF_PASSWORD,
)

from .const import ( # pylint: disable=unused-import
    CONF_INSTALLATION_HASH,
    DOMAIN,
    ROOT_URL,
    LOGIN_URL,
    INSTALLATION_URL,
    UPDATE_URL,
)

DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_USERNAME): str,
        vol.Required(CONF_PASSWORD): str,
        vol.Required(CONF_INSTALLATION_HASH): str, #TODO: make optional via scraping
    }
)

class ChiliconCloudConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Chilicon Cloud user config flow."""

    VERSION = 1

    async def async_step_user(self, user_input):
        # user_input is what the user typed in
        """Get login info"""
        errors = {}

        if user_input is not None:
            #make connection stuff
            _LOGGER.info("make connection stuff")
            req_headers = {
                'Content-Type': 'application/x-www-form-urlencoded'
            }

            form_data = {
                'username': user_input[CONF_USERNAME],
                'password': user_input[CONF_PASSWORD],
                'Login': 'Login'
            }
            async with aiohttp_client.ClientSession() as session:
                async with session.post(LOGIN_URL,data=form_data,headers=req_headers) as resp:
                    _LOGGER.info("Request Headers: %s" % resp.headers)
                    _LOGGER.info("Request Status Code: %s" % resp.status)
                    _LOGGER.info("Request Text: %s" % await resp.text())
            #start saving info here?
            _LOGGER.info("saving info?")
            #return self.async_create_entry(
            #    title="installationnamehere",
            #    data={
            #        "username": user_input[CONF_USERNAME],
            #        "password": user_input[CONF_PASSWORD],
            #        "installtion_hash": user_input[CONF_INSTALLATION_HASH]
            #    }
            #)
        
        return self.async_show_form(
            step_id="user", data_schema=DATA_SCHEMA, errors=errors
        )
