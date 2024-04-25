from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models.supportTicket import SupportTicket
from ..schemas.supportTicket import SupportTicketUpdate, SupportTicketCreate


def create_support_ticket(db: Session, ticket_request: SupportTicketCreate, customer_id: int):
    new_ticket = SupportTicket(**ticket_request.dict(), customer_id=customer_id)
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket

def get_support_ticket(db: Session, ticket_id: int):
    ticket = db.query(SupportTicket).filter(SupportTicket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Support ticket not found")
    return ticket

def update_support_ticket(db: Session, ticket_id: int, update_request: SupportTicketUpdate):
    ticket = db.query(SupportTicket).filter(SupportTicket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Support ticket not found")
    ticket.update(update_request.dict(exclude_unset=True))
    db.commit()
    return ticket
