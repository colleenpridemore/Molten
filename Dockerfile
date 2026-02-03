# OpenClaw Identity Framework - Dockerfile
# Multi-stage build for optimized image size

FROM python:3.12-slim as builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Final stage
FROM python:3.12-slim

WORKDIR /app

# Copy Python dependencies from builder
COPY --from=builder /root/.local /root/.local

# Copy application code
COPY openclaw_identity/ ./openclaw_identity/
COPY empathy_engine.py .
COPY empathy_engine_example.py .
COPY setup.py .
COPY README.md .

# Install the package
RUN pip install --no-cache-dir -e .

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV OPENCLAW_ENV=production

# Create a non-root user
RUN useradd -m -u 1000 openclaw && chown -R openclaw:openclaw /app
USER openclaw

# Expose port for potential API server
EXPOSE 8080

# Default command (can be overridden)
CMD ["python", "-m", "openclaw_identity.example"]
