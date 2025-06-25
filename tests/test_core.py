import json
from pathlib import Path
from typing import Any, Dict, List

import pytest

from core.services import create_auth_request
from core.utils import sanitize_html
from core.validators import validate_cpt_code, validate_patient_id

CONFIG_PATH = Path(__file__).resolve().parent.parent / "seed-config.yaml"


def load_pairs() -> List[Dict[str, str]]:
    with CONFIG_PATH.open() as f:
        data: Any = json.load(f)
    assert isinstance(data, list)
    return [{"cpt": str(item["cpt"]), "icd": str(item["icd"])} for item in data]


def test_create_auth_request() -> None:
    pairs = load_pairs()
    first = pairs[0]
    auth = create_auth_request("patient1", first["cpt"], "<b>Example</b>")
    assert auth.referral.patient_id == "patient1"
    assert auth.referral.cpt_code.code == first["cpt"]
    assert auth.referral.cpt_code.description == "Example"
    assert auth.status == "pending"


def test_sanitize_html() -> None:
    assert sanitize_html("<i>hello</i>") == "hello"


def test_validation_errors() -> None:
    with pytest.raises(ValueError):
        validate_patient_id("??")
    with pytest.raises(ValueError):
        validate_cpt_code("bad!")
