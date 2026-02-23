from sqlalchemy.orm import Session
from ..models import AuditEvent


def record_event(db: Session, actor: str, action: str, details: dict) -> AuditEvent:
    evt = AuditEvent(actor=actor, action=action, details=details)
    db.add(evt)
    db.commit()
    db.refresh(evt)
    return evt
