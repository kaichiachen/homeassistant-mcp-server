# Home Assistant MCP Server Add-on

[![Add Repository](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fkaichiachen%2Fhomeassistant-mcp-server)

MCP (Model Context Protocol) server that connects AI assistants to your Home Assistant.

## Quick Start

1. Click the button above or manually add repository: `https://github.com/kaichiachen/homeassistant-mcp-server`
2. Install the add-on
3. Configure `ha_url` and `ha_token`
4. Start the add-on
5. Configure your MCP client to connect to `http://<your-ha-ip>:8000/mcp/`

## Available Tools

| Tool | Description |
|------|-------------|
| `get_entity` | Get entity state |
| `entity_action` | Control entities (on/off/toggle) |
| `list_entities` | List and search entities |
| `list_automations` | List all automations |
| `list_scripts_tool` | List scripts |
| `get_script_config_tool` | Get script inputs and actions |
| `get_calendar_events_tool` | Query calendar events |
| `get_camera_image_tool` | Get a still image from a camera |
| `call_service_tool` | Call any HA service |
| `system_overview` | Get system overview |
| `get_history` | Get entity history |
| `get_error_log` | Get error logs |

## MCP Client Setup

### Cursor / Antigravity / Claude Desktop

```json
{
  "mcpServers": {
    "ha-mcp-server": {
      "url": "http://your-ha-ip:8000/mcp/"
    }
  }
}
```

### Gemini CLI

```bash
gemini --mcp-server="http://your-ha-ip:8000/mcp/"
```

## Best Practices

- **Unicode Encoding**: Ensure all input strings are UTF-8 encoded.
- **Token Efficiency**: Use domain summaries and filtered searches instead of listing all entities in large installations.

See the [main README](../README.md) for detailed configuration instructions.
