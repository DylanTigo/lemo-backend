# ----------- BUILD STAGE -----------
FROM python:3.12-slim AS builder

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# ----------- FINAL IMAGE -----------
FROM python:3.12-slim

# Set environment variable
ENV APP_PORT=8000

WORKDIR /app

# Copy installed deps from builder
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Add PATH
ENV PATH=/root/.local/bin:$PATH

# Copy app code
COPY . .

# Expose the FastAPI port
EXPOSE ${APP_PORT}

# Non-root user (security)
RUN useradd -m appuser && \
    chown -R appuser:appuser /app
USER appuser

# Start server
CMD ["sh", "-c", "uvicorn src.main:app --host 0.0.0.0 --port ${APP_PORT}"]
