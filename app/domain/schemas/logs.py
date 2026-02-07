from pydantic import BaseModel

class LogIngest(BaseModel):
    service: str
    level: str
    message: str
