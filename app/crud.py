from sqlalchemy.orm import Session
from .models import Policy, PolicyVersion, Acknowledgement
from .schemas import PolicyCreate, PolicyVersionCreate, AcknowledgementCreate

def create_policy(db: Session, policy: PolicyCreate):
    db_policy = Policy(**policy.dict())
    db.add(db_policy)
    db.commit()
    db.refresh(db_policy)
    return db_policy

def add_policy_version(db: Session, policy_id: int, version: PolicyVersionCreate):
    db_version = PolicyVersion(policy_id=policy_id, **version.dict())
    db.add(db_version)
    db.commit()
    return db_version

def acknowledge_policy(db: Session, policy_id: int, ack: AcknowledgementCreate):
    db_ack = Acknowledgement(policy_id=policy_id, employee_name=ack.employee_name)
    db.add(db_ack)
    db.commit()
    return db_ack
