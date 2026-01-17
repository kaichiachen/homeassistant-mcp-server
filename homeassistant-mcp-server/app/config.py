import os
from typing import Optional

import json
import logging

# Home Assistant configuration
HA_URL: str = os.environ.get("HA_URL", "http://homeassistant.local:8123")
HA_TOKEN: str = os.environ.get("HA_TOKEN", "")

# Load configuration from Add-on options if available
options_path = "/data/options.json"
if os.path.exists(options_path):
    try:
        with open(options_path, "r") as f:
            options = json.load(f)
            HA_URL = options.get("ha_url", HA_URL)
            HA_TOKEN = options.get("ha_token", HA_TOKEN)
    except Exception as e:
        # We can't use the logger here yet because it might not be configured
        print(f"Failed to read options from {options_path}: {e}")

def get_ha_headers() -> dict:
    """Return the headers needed for Home Assistant API requests"""
    headers = {
        "Content-Type": "application/json",
    }
    
    # Only add Authorization header if token is provided
    if HA_TOKEN:
        headers["Authorization"] = f"Bearer {HA_TOKEN}"
    
    return headers
