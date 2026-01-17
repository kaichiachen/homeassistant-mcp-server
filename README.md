# homeassistant-mcp-server

[![Add Repository](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fkaichiachen%2Fhomeassistant-mcp-server)

A Model Context Protocol (MCP) server for Home Assistant, utilizing Streamable HTTP for real-time communication. This allows you to expose your Home Assistant entities and services to MCP clients (like Claude Desktop, Cursor, Antigravity, and other AI agents).

## Features

- **Entity Management**: List, search, and filter Home Assistant entities by domain
- **Device Control**: Turn devices on/off, toggle, and control entity actions
- **Automation & Scripts**: List automations, get script configurations including input fields
- **Calendar Events**: Query calendar events for date ranges
- **System Monitoring**: Get system overview, error logs, entity history, and logbook
- **Service Calls**: Call any Home Assistant service with custom parameters
- **Multi-Arch**: Supports `amd64` and `aarch64` (ARM64), perfect for Raspberry Pi

## Available MCP Tools

| Tool | Description |
|------|-------------|
| `get_version` | Get Home Assistant version |
| `get_entity` | Get entity state with optional field filtering |
| `entity_action` | Perform on/off/toggle actions on entities |
| `list_entities` | List entities with domain filtering and search |
| `search_entities_tool` | Search entities by name, ID, or attributes |
| `domain_summary_tool` | Get summary of entities in a specific domain |
| `system_overview` | Get comprehensive overview of the HA system |
| `list_automations` | List all automations with state and triggers |
| `list_scripts_tool` | List all scripts with optional configuration |
| `get_script_config_tool` | Get script fields (inputs) and sequence (actions) |
| `get_calendar_events_tool` | Get calendar events for a date range |
| `call_service_tool` | Call any Home Assistant service |
| `get_history` | Get entity state change history |
| `get_error_log` | Get Home Assistant error log |
| `get_logbook` | Get logbook entries |

## Installation

### Method 1: Home Assistant Add-on (Recommended)

Click the button below to add the repository:

[![Add Repository](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fkaichiachen%2Fhomeassistant-mcp-server)

Or manually:

1. Go to **Settings** > **Add-ons** > **Add-on Store**
2. Click ⋮ (top right) > **Repositories**
3. Add: `https://github.com/kaichiachen/homeassistant-mcp-server`
4. Find "homeassistant-mcp-server" and click **Install**
5. Configure `ha_url` and `ha_token` in the **Configuration** tab
6. Click **Start**

### Method 2: Docker

```bash
docker run -d \
  --name homeassistant-mcp-server \
  -p 8000:8000 \
  -e HA_URL="http://your-home-assistant-ip:8123" \
  -e HA_TOKEN="your-long-lived-access-token" \
  ghcr.io/kaichiachen/homeassistant-mcp-server:latest
```

## Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `HA_URL` | Home Assistant URL | `http://localhost:8123` |
| `HA_TOKEN` | Long-Lived Access Token | _Required_ |

## MCP Client Configuration

Once your server is running (e.g., at `http://localhost:8000`), configure your MCP client:

### Cursor

Add to `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "ha-mcp-server": {
      "url": "http://localhost:8000/mcp/"
    }
  }
}
```

### Antigravity

Add to `~/.gemini/antigravity/mcp_config.json`:

```json
{
  "mcpServers": {
    "ha-mcp-server": {
      "url": "http://localhost:8000/mcp/"
    }
  }
}
```

### Claude Desktop

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "ha-mcp-server": {
      "url": "http://localhost:8000/mcp/"
    }
  }
}
```

### Gemini CLI

```bash
gemini --mcp-server="http://localhost:8000/mcp/"
```

Or add to `~/.gemini/settings.json`:

```json
{
  "mcpServers": {
    "ha-mcp-server": {
      "url": "http://localhost:8000/mcp/"
    }
  }
}
```

### Claude Code (VS Code Extension)

Add to VS Code settings (`settings.json`):

```json
{
  "claude.mcpServers": {
    "ha-mcp-server": {
      "url": "http://localhost:8000/mcp/"
    }
  }
}
```

## Development

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Run locally
export HA_URL="http://localhost:8123"
export HA_TOKEN="your-token"
uv run python -m app.server

# Server available at http://localhost:8000/mcp/
# Health check: http://localhost:8000/health
```

## License

MIT License - See [LICENSE](LICENSE) file.
