ROLE_LIMITS = {
    "explore": 5,
    "elevate": 50,
    "ascend": 500
}

usage_store = {}

def can_send(user_id: str, role: str):
    usage = usage_store.get(user_id, 0)
    if usage >= ROLE_LIMITS[role]:
        return False
    usage_store[user_id] = usage + 1
    return True
