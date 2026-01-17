# homeassistant-mcp-server

A Model Context Protocol (MCP) server for Home Assistant, utilizing Streamable HTTP for real-time communication. This allows you to expose your Home Assistant entities and services to MCP clients (like Claude Desktop or other AI agents).

## Features

- **Entity Listing**: List and filter Home Assistant entities (e.g., lights, switches, sensors).
- **Control**: Turn devices on/off and control other services.
- **Real-time**: Built on `mcp` library with Streamable HTTP transport.
- **Multi-Arch**: Supports `amd64` and `aarch64` (ARM64), making it perfect for Raspberry Pi.

## Installation

### Method 1: Home Assistant Add-on

1.  **Add Repository**:
    - Go to **Settings** > **Add-ons** > **Add-on Store**.
    - Click the three dots (top right) > **Repositories**.
    - Add the URL of this repository: `https://github.com/kaichiachen/homeassistant-mcp-server`.
2.  **Install**:
    - Find "homeassistant-mcp-server" in the list and click **Install**.
3.  **Configure**:
    - Go to the **Configuration** tab of the add-on.
    - Set `ha_url` (e.g., `http://homeassistant.local:8123` for internal access or your external URL).
    - Set `ha_token` (Long-Lived Access Token created in your Profile).
4.  **Start**:
    - Click **Start**. Check the "Log" tab to ensure it's running on port 8000.

### Method 2: Docker (Remote Server)

To deploy on a remote server (e.g., a VPS or another Raspberry Pi):

**Using Docker Run:**

```bash
docker run -d \
  --name homeassistant-mcp-server \
  -p 8000:8000 \
  -e HA_URL="http://your-home-assistant-ip:8123" \
  -e HA_TOKEN="your-long-lived-access-token" \
  ghcr.io/kaichiachen/homeassistant-mcp-server:latest
```

**Using Docker Compose:**

```yaml
services:
  homeassistant-mcp-server:
    image: ghcr.io/kaichiachen/homeassistant-mcp-server:latest
    container_name: homeassistant-mcp-server
    ports:
      - "8000:8000"
    environment:
      - HA_URL=http://your-home-assistant-ip:8123
      - HA_TOKEN=your-long-lived-access-token
    restart: unless-stopped
```

## Configuration

| Environment Variable | Add-on Option | Description | Default |
|----------------------|---------------|-------------|---------|
| `HA_URL`             | `ha_url`      | URL of Home Assistant instance | `http://localhost:8123` |
| `HA_TOKEN`           | `ha_token`    | Long Lived Access Token | _Required_ |

## Development

1.  **Install `uv`**:
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
2.  **Run Locally**:
    ```bash
    export HA_URL="http://localhost:8123"
    export HA_TOKEN="your-token"
    uv run python -m app.server
    # The server will be available at http://localhost:8000/mcp/
    # Health check: http://localhost:8000/health

    # Verify connectivity (requires Accept header for stateless mode):
    curl -v -H "Accept: application/json, text/event-stream" \
         -H "Content-Type: application/json" \
         -d '{"jsonrpc": "2.0", "method": "initialize", "id": 1, "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "test", "version": "1.0"}}}' \
         http://localhost:8000/mcp/
    ```
