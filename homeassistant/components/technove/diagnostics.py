"""Diagnostics support for TechnoVE."""

from __future__ import annotations

from dataclasses import asdict
from typing import Any

from homeassistant.components.diagnostics import async_redact_data
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN
from .coordinator import TechnoVEDataUpdateCoordinator

TO_REDACT = {"unique_id", "mac_address"}


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for a config entry."""
    coordinator: TechnoVEDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]
    return async_redact_data(asdict(coordinator.data.info), TO_REDACT)
