from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..controllers.supportTicket import create_support_ticket, get_support_ticket, update_support_ticket
from ..schemas.supportTicket import SupportTicketCreate, SupportTicketResponse, SupportTicketUpdate

router = APIRouter()

@router.post("/support-tickets/", response_model= SupportTicketResponse)
def create_ticket(ticket_request: SupportTicketCreate, db: Session = Depends(get_db)):
    customer_id = 1
    return create_support_ticket(db=db, ticket_request=ticket_request, customer_id=customer_id)

@router.get("/support-tickets/{ticket_id}", response_model= SupportTicketResponse)
def read_ticket(ticket_id: int, db: Session = Depends(get_db)):
    return get_support_ticket(db=db, ticket_id=ticket_id)

@router.put("/support-tickets/{ticket_id}", response_model= SupportTicketResponse)
def update_ticket(ticket_id: int, ticket_update: SupportTicketUpdate, db: Session = Depends(get_db)):
    return update_support_ticket(db=db, ticket_id=ticket_id, ticket_update=ticket_update)
