# MCP server Dockerfile for Claude Desktop integration
FROM ghcr.io/astral-sh/uv:0.6.6-python3.13-bookworm

LABEL \
    io.hass.name="ha-mcp-server" \
    io.hass.description="Model Context Protocol (MCP) server for Home Assistant." \
    io.hass.arch="aarch64|amd64" \
    io.hass.type="addon" \
    io.hass.version="0.1.1"

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Set environment for MCP communication
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

# Install package with UV (using --system flag)
RUN uv pip install --system -e .

# Expose the mcp port
EXPOSE 8000

# Run the MCP server with http transport
ENTRYPOINT ["uv", "run", "python", "-m", "app.server"]