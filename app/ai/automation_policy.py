POLICIES = {
    "memory_leak": {
        "allowed": True,
        "actions": ["scale_service", "restart_service"]
    },
    "high_latency": {
        "allowed": True,
        "actions": ["scale_service"]
    },
    "db_connection_exhaustion": {
        "allowed": True,
        "actions": ["restart_db_connections"]
    }
}

def get_policy(root_cause: str):
    for key, policy in POLICIES.items():
        if key in root_cause.lower():
            return policy
    return {"allowed": False, "actions": []}
