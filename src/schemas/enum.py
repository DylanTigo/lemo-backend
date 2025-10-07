# Enums
from enum import Enum 


class UserRole(str, Enum):
    CLIENT = "client"
    ADMIN = "admin"

class OrderStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class AttributeType(str, Enum):
    TEXT = "text"
    NUMBER = "number"
    LIST = "list"
    BOOLEAN = "boolean"