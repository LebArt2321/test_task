from fastapi import FastAPI, HTTPException
from database import get_templates, add_template
from validators import validate_email, validate_phone, validate_date, validate_text
from typing import Dict


app = FastAPI()


@app.post("/get_form")
async def get_form(data: Dict[str, str]):
    templates = get_templates()
    if not data:
        raise HTTPException(status_code=400, detail="No data provided")
    for template in templates:
        if all(field_name in data and 
               validate_field(data[field_name], template.fields[field_name].type)
               for field_name in template.fields):
            return {"name": template.name}

    return {name: infer_field_type(value) for name, value in data.items()}

def validate_field(value: str, field_type: str) -> bool:
    print(f"Validating {value} as {field_type}")
    validators = {
        "email": validate_email,
        "phone": validate_phone,
        "date": validate_date,
        "text": validate_text,
    }
    result = validators[field_type](value)
    print(f"Result: {result}")  
    return result


def infer_field_type(value: str) -> str:
    if validate_date(value):
        return "date"
    elif validate_phone(value):
        return "phone"
    elif validate_email(value):
        return "email"
    else:
        return "text"
