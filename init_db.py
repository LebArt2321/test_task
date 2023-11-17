from database import add_template
from models import FormTemplate, FormField


initial_templates = [
    FormTemplate(name="MyForm", fields={
        "user_email": FormField(name="user_email", type="email"),
        "user_phone": FormField(name="user_phone", type="phone"),
    }),
    FormTemplate(name="OrderForm", fields={
        "order_date": FormField(name="order_date", type="date"),
        "customer_name": FormField(name="customer_name", type="text"),
    }),
    FormTemplate(name="FeedbackForm", fields={
        "customer_email": FormField(name="customer_email", type="email"),
        "feedback_text": FormField(name="feedback_text", type="text"),
    }),
]


for template in initial_templates:
    add_template(template)
