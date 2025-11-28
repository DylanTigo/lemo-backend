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

WORKDIR /app

# Copy installed deps from builder
COPY --from=builder /root/.local /root/.local

# Add PATH
ENV PATH=/root/.local/bin:$PATH

# Copy app code
COPY . .

# Non-root user (security)
RUN useradd -m fastapiuser
USER fastapiuser

# Expose port
EXPOSE 8000

# Start server
CMD ["sh", "-c", "uvicorn src.main:app --host 0.0.0.0 --port $PORT"]
