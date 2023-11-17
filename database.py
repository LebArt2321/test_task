from tinydb import TinyDB, Query
from models import FormTemplate

db = TinyDB('db.json')

def get_templates():
    return [FormTemplate(**template) for template in db.all()]

def add_template(template: FormTemplate):
    db.insert(template.dict())
