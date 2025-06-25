from datetime import datetime

from .models import AuthRequest, CPTCode, Referral
from .utils import sanitize_html
from .validators import validate_cpt_code, validate_patient_id


def create_auth_request(patient_id: str, code: str, description: str) -> AuthRequest:
    """Validate inputs and create a sanitized authorization request."""

    validate_patient_id(patient_id)
    safe_code = validate_cpt_code(code)
    safe_desc = sanitize_html(description)

    cpt = CPTCode(code=safe_code, description=safe_desc)
    referral = Referral(
        patient_id=patient_id, cpt_code=cpt, created_at=datetime.utcnow()
    )
    return AuthRequest(referral=referral)
