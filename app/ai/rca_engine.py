from app.ai.context_builder import build_context
from app.ai.llm_client import call_llm
from app.ai.vector_store import vector_store
from app.ai.automation_engine import execute_actions

async def analyze_incident(db, incident_id: int):
    context = await build_context(db, incident_id)

    memory = vector_store.search(context)

    full_context = f"""
PAST INCIDENT MEMORY:
{memory}

CURRENT CONTEXT:
{context}
"""

    response = call_llm(full_context)

    vector_store.add(context)

    actions = execute_actions(response)

    return {"analysis": response, "actions": actions}
