import asyncio

async def process_incident(incident_id: int):
    print(f"[WORKER] Processing incident: {incident_id}")

    # Here AI + correlation + RCA engine will run
    # Placeholder for now
    return True
import asyncio
from app.infrastructure.db.session import AsyncSessionLocal
from app.ai.rca_engine import analyze_incident

def process_incident(incident_id: int):
    async def runner():
        async with AsyncSessionLocal() as db:
            result = await analyze_incident(db, incident_id)
            print(f"[AI RCA RESULT] {result}")

    asyncio.run(runner())
