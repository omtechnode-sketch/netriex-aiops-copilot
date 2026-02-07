from app.ai.automation_policy import get_policy
from app.ai.aws_executor import scale_service, restart_service

def execute_actions(root_cause: str):
    policy = get_policy(root_cause)

    if not policy["allowed"]:
        return "No automation allowed"

    results = []

    for action in policy["actions"]:
        if action == "scale_service":
            res = scale_service("netriex-cluster", "api-service", 4)
            results.append("Scaled service")

        elif action == "restart_service":
            res = restart_service("netriex-cluster", "api-service")
            results.append("Restarted service")

    return results
