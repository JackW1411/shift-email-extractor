import datetime
from pydantic import BaseModel

class ShiftRequest(BaseModel):
    pharmacy: str
    shift_date: datetime.date
    start_time: datetime.time | None = None
    end_time: datetime.time | None = None
    role: str | None = None
    rate: float | None = None

