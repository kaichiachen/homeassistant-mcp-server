
from typing import Dict, Any

async def restart_home_assistant() -> Dict[str, Any]:
    """Restart Home Assistant"""
    from app.client import call_service
    return await call_service("homeassistant", "restart", {})
