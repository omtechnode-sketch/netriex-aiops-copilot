import boto3
import json
from app.config.settings import settings

client = boto3.client("bedrock-runtime", region_name=settings.AWS_REGION)

def call_llm(prompt: str):
    body = json.dumps({
        "prompt": prompt,
        "max_tokens_to_sample": 500,
        "temperature": 0.3
    })

    response = client.invoke_model(
        modelId="anthropic.claude-v2",
        body=body,
        contentType="application/json",
        accept="application/json"
    )

    result = json.loads(response["body"].read())
    return result["completion"]
