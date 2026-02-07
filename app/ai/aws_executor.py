import boto3
from app.config.settings import settings

ecs = boto3.client("ecs", region_name=settings.AWS_REGION)

def scale_service(cluster: str, service: str, desired_count: int):
    return ecs.update_service(
        cluster=cluster,
        service=service,
        desiredCount=desired_count
    )

def restart_service(cluster: str, service: str):
    return ecs.update_service(
        cluster=cluster,
        service=service,
        forceNewDeployment=True
    )
