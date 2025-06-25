import re

PATIENT_RE = re.compile(r"^[A-Za-z0-9_-]{3,32}$")
CPT_RE = re.compile(r"^[0-9A-Z]{4,5}$")


def validate_patient_id(patient_id: str) -> str:
    if not PATIENT_RE.fullmatch(patient_id):
        raise ValueError("invalid patient id")
    return patient_id


def validate_cpt_code(code: str) -> str:
    if not CPT_RE.fullmatch(code):
        raise ValueError("invalid CPT code")
    return code
