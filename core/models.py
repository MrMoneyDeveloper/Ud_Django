from dataclasses import dataclass
from datetime import datetime


@dataclass
class CPTCode:
    code: str
    description: str


@dataclass
class Referral:
    patient_id: str
    cpt_code: CPTCode
    created_at: datetime


@dataclass
class AuthRequest:
    referral: Referral
    status: str = "pending"
