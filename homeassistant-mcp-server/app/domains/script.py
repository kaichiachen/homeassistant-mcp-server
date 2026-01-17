
IMPORTANT_ATTRIBUTES = ["last_triggered"]

from typing import List, Dict, Any, Optional


async def get_script_config(script_id: str) -> Dict[str, Any]:
    """
    Get the configuration of a Home Assistant script including its fields and sequence.
    
    Args:
        script_id: The script ID without 'script.' prefix (e.g., 'homepod_edge_tts')
    
    Returns:
        Script configuration including fields, sequence, alias, mode, etc.
    """
    from app.client import get_client
    from app.config import HA_URL, get_ha_headers
    
    # Remove 'script.' prefix if provided
    if script_id.startswith("script."):
        script_id = script_id[7:]
    
    client = await get_client()
    try:
        response = await client.get(
            f"{HA_URL}/api/config/script/config/{script_id}",
            headers=get_ha_headers()
        )
        
        if response.status_code == 404:
            return {"error": f"Script '{script_id}' not found"}
        
        response.raise_for_status()
        config = response.json()
        
        # Add the script_id to the response for clarity
        config["script_id"] = script_id
        config["entity_id"] = f"script.{script_id}"
        
        return config
        
    except Exception as e:
        return {"error": f"Failed to get script config: {str(e)}"}


async def get_scripts(include_config: bool = False) -> List[Dict[str, Any]]:
    """
    Get a list of all scripts from Home Assistant.
    
    Args:
        include_config: If True, includes the full configuration for each script.
    
    Returns:
        List of scripts with their IDs, names, states, and optionally full configuration.
    """
    from app.client import get_entities
    
    # Get all script entities
    script_entities = await get_entities(domain="script")
    
    if isinstance(script_entities, dict) and "error" in script_entities:
        return script_entities
    
    result = []
    try:
        for entity in script_entities:
            script_info = {
                "script_id": entity["entity_id"].split(".")[1],
                "entity_id": entity["entity_id"],
                "state": entity["state"],
                "alias": entity["attributes"].get("friendly_name", entity["entity_id"]),
            }
            
            if "last_triggered" in entity["attributes"]:
                script_info["last_triggered"] = entity["attributes"]["last_triggered"]
            
            if "mode" in entity["attributes"]:
                script_info["mode"] = entity["attributes"]["mode"]
            
            # Optionally include full configuration
            if include_config:
                config = await get_script_config(script_info["script_id"])
                if "error" not in config:
                    script_info["config"] = config
            
            result.append(script_info)
            
    except (TypeError, KeyError) as e:
        return {"error": f"Error processing script entities: {str(e)}"}
    
    return result
