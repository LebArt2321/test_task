from pydantic import BaseModel, EmailStr, constr
from typing import Dict
from datetime import datetime
import re


def validate_email(value: str) -> bool:
    pattern = re.compile(r"^\S+@\S+\.\S+$")
    return bool(pattern.match(value))


def validate_phone(value: str) -> bool:
    pattern = re.compile(r'^\+7 \d{3} \d{3} \d{2} \d{2}$')
    return bool(pattern.match(value))

def validate_date(value: str) -> bool:
    for fmt in ("%d.%m.%Y", "%Y-%m-%d"):
        try:
            datetime.strptime(value, fmt)
            return True
        except ValueError:
            pass
    return False

def validate_text(value: str) -> bool:
    return isinstance(value, str)
