
IMPORTANT_ATTRIBUTES = ["last_triggered"]

from typing import List, Dict, Any

async def get_automations() -> List[Dict[str, Any]]:
    """Get a list of all automations from Home Assistant"""
    # Import locally to avoid circular imports since client imports domains
    from app.client import get_entities

    # Reuse the get_entities function with domain filtering
    automation_entities = await get_entities(domain="automation")
    
    # Check if we got an error response
    if isinstance(automation_entities, dict) and "error" in automation_entities:
        return automation_entities  # Just pass through the error
    
    # Process automation entities
    result = []
    try:
        for entity in automation_entities:
            # Extract relevant information
            automation_info = {
                "id": entity["entity_id"].split(".")[1],
                "entity_id": entity["entity_id"],
                "state": entity["state"],
                "alias": entity["attributes"].get("friendly_name", entity["entity_id"]),
            }
            
            # Add any additional attributes that might be useful
            if "last_triggered" in entity["attributes"]:
                automation_info["last_triggered"] = entity["attributes"]["last_triggered"]
            
            result.append(automation_info)
    except (TypeError, KeyError) as e:
        # Handle errors in processing the entities
        return {"error": f"Error processing automation entities: {str(e)}"}
        
    return result

async def reload_automations() -> Dict[str, Any]:
    """Reload all automations in Home Assistant"""
    from app.client import call_service
    return await call_service("automation", "reload", {})
