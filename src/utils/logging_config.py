# src/utils/logging_config.py
import logging
from typing import List


class HealthCheckFilter(logging.Filter):
    """Filter out health check requests from access logs."""

    def __init__(self, paths: List[str] = None):
        super().__init__()
        # Default health check paths to filter
        self.filtered_paths = paths or [
            "/health",
            "/ready",
            "/live",
            "/readiness",
            "/liveness",
            "/healthz",
            "/ping",
        ]

    def filter(self, record: logging.LogRecord) -> bool:
        """Return False to filter out the log record."""
        # Check if the log message contains any of the filtered paths
        message = record.getMessage()
        return not any(path in message for path in self.filtered_paths)


def setup_logging():
    """Configure logging to filter out health check requests."""
    # Get the uvicorn access logger
    uvicorn_access = logging.getLogger("uvicorn.access")

    # Add the health check filter
    health_filter = HealthCheckFilter()
    uvicorn_access.addFilter(health_filter)

    # Optional: Also filter the main uvicorn logger
    uvicorn_main = logging.getLogger("uvicorn")
    uvicorn_main.addFilter(health_filter)


# Alternative: More specific filter for exact matches
class ExactPathFilter(logging.Filter):
    """Filter out exact path matches from access logs."""

    def __init__(self, paths: List[str] = None):
        super().__init__()
        self.filtered_paths = paths or [
            "/ready",
            "/health",
            "/live",
            "/readiness",
            "/liveness",
            "/healthz",
            "/ping",
        ]

    def filter(self, record: logging.LogRecord) -> bool:
        message = record.getMessage()
        # More precise matching: look for "GET /path HTTP/1.1"
        for path in self.filtered_paths:
            if f'"GET {path} HTTP/1.1"' in message:
                return False
        return True
