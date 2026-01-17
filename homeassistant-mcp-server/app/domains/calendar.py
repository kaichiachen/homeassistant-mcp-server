from typing import List, Dict, Any, Optional
from datetime import datetime
import urllib.parse

IMPORTANT_ATTRIBUTES = [
    "message",
    "all_day",
    "start_time",
    "end_time",
    "location",
    "description",
]

async def get_calendar_events(
    entity_id: str,
    start_date: datetime,
    end_date: datetime
) -> List[Dict[str, Any]]:
    """
    Get events for a specific calendar within a date range.
    
    Args:
        entity_id: The calendar entity ID
        start_date: Start datetime object
        end_date: End datetime object
        
    """
    from app.client import get_client
    from app.config import HA_URL, get_ha_headers
    
    client = await get_client()
    
    # Format dates as ISO 8601 strings
    start_str = urllib.parse.quote(start_date.isoformat())
    end_str = urllib.parse.quote(end_date.isoformat())
    
    url = f"{HA_URL}/api/calendars/{entity_id}?start={start_str}&end={end_str}"
    
    response = await client.get(url, headers=get_ha_headers())
    response.raise_for_status()
    
    return response.json()
