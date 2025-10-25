# src/utils/exceptions.py
from typing import Optional, Any


class LemoServiceException(Exception):
    """Custom exception for Lemo services"""

    def __init__(
        self,
        message: str,
        details: Optional[Any] = None,
        status_code: int = 500,
    ):
        self.message = message
        self.details = details
        self.status_code = status_code
        super().__init__(self.message)

    def to_dict(self):
        return {
            "message": self.message,
            "details": self.details,
            "status_code": self.status_code,
        }

class UnauthorizedException(Exception):
    """Exception levée lors d'une erreur d'authentification"""
    pass

class NotFoundException(LemoServiceException):
    """Exception levée lorsqu'une ressource n'est pas trouvée"""

    def __init__(self, message: str, details: Optional[Any] = None):
        super().__init__(message, details, status_code=404)