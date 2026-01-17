
# Import domain modules
from . import (
    light, switch, binary_sensor, sensor, climate, 
    media_player, cover, fan, camera, automation, 
    scene, script
)

# Registry of all domain modules
_DOMAINS = {
    "light": light,
    "switch": switch,
    "binary_sensor": binary_sensor,
    "sensor": sensor,
    "climate": climate,
    "media_player": media_player,
    "cover": cover,
    "fan": fan,
    "camera": camera,
    "automation": automation,
    "scene": scene,
    "script": script,
}

# Aggregate important attributes
DOMAIN_IMPORTANT_ATTRIBUTES = {}

for domain_name, module in _DOMAINS.items():
    if hasattr(module, "IMPORTANT_ATTRIBUTES"):
        DOMAIN_IMPORTANT_ATTRIBUTES[domain_name] = module.IMPORTANT_ATTRIBUTES
