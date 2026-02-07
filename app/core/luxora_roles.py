from enum import Enum

class UserRole(str, Enum):
    EXPLORE = "explore"
    ELEVATE = "elevate"
    ASCEND = "ascend"


ROLE_LIMITS = {
    UserRole.EXPLORE: 5,
    UserRole.ELEVATE: 50,
    UserRole.ASCEND: 500
}
