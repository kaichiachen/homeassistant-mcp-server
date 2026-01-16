# Docker Instructions

## Build
```bash
docker build -t ha-mcp-server .
```

## Run
You need to provide `HA_URL` and `HA_TOKEN` environment variables.

```bash
docker run -d \
  -p 8000:8000 \
  -e HA_URL="http://host.docker.internal:8123" \
  -e HA_TOKEN="your_long_lived_access_token" \
  --name ha-mcp-server \
  ha-mcp-server
```

> **Note**: If your Home Assistant is running on localhost, use `host.docker.internal` (Mac/Windows) or `--network host` (Linux) to allow the container to access it.

## Verify
Check the logs:
```bash
docker logs -f ha-mcp-server
```

Test the connection:
```bash
# Check health
curl http://localhost:8000/health

# Connect to MCP stream
curl http://localhost:8000/mcp
```
