from pydantic import BaseModel
from typing import Optional

class SupportTicketBase(BaseModel):
    subject: str
    message: str

class SupportTicketCreate(SupportTicketBase):
    pass

class SupportTicketUpdate(BaseModel):
    status: Optional[str] = None

class SupportTicketResponse(SupportTicketBase):
    id: int
    status: str

    class Config:
        orm_mode = True
