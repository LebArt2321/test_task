from pydantic import BaseModel
from typing import Dict


class FormField(BaseModel):
    name: str
    type: str

class FormTemplate(BaseModel):
    name: str
    fields: Dict[str, FormField]
