# Optimization: Use python slim image for smaller size (~150MB vs ~1GB)
FROM python:3.13-slim

# Install uv from the official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

LABEL \
    io.hass.name="ha-mcp-server" \
    io.hass.description="Model Context Protocol (MCP) server for Home Assistant." \
    io.hass.arch="aarch64|amd64" \
    io.hass.type="addon" \
    io.hass.version="0.1.3"

# Set working directory
WORKDIR /app

# Enable bytecode compilation and copy mode for uv
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

# Install dependencies first (leverage Docker cache)
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project --no-dev

# Copy application code
COPY . .

# Sync the project
RUN uv sync --frozen --no-dev

# Add virtualenv to PATH
ENV PATH="/app/.venv/bin:$PATH"

# Expose the mcp port
EXPOSE 8000

# Run the MCP server directly with python (no uv run overhead)
ENTRYPOINT ["python", "-m", "app.server"]