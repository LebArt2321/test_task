import requests


def test_myform_valid():
    data = {"user_email": "test@example.com", "user_phone": "+7 123 456 78 90"}
    response = requests.post("http://127.0.0.1:8000/get_form", json=data)
    assert response.status_code == 200
    assert response.json() == {"name": "MyForm"}

def test_unknown_field():
    data = {"random_field": "some value"}
    response = requests.post("http://127.0.0.1:8000/get_form", json=data)
    assert response.status_code == 200
    assert response.json() == {"random_field": "text"}

def test_myform_with_extra_field():
    data = {"user_email": "test@example.com", "user_phone": "+7 123 456 78 90", "extra_field": "extra value"}
    response = requests.post("http://127.0.0.1:8000/get_form", json=data)
    assert response.status_code == 200
    assert response.json() == {"name": "MyForm"}

def test_orderform_valid():
    data = {"order_date": "01.01.2023", "customer_name": "John Doe"}
    response = requests.post("http://127.0.0.1:8000/get_form", json=data)
    assert response.status_code == 200
    assert response.json() == {"name": "OrderForm"}

def test_feedbackform_valid():
    data = {"customer_email": "jane.doe@example.com", "feedback_text": "Great service!"}
    response = requests.post("http://127.0.0.1:8000/get_form", json=data)
    assert response.status_code == 200
    assert response.json() == {"name": "FeedbackForm"}

def test_invalid_email():
    data = {"user_email": "not_an_email", "user_phone": "+7 123 456 78 90"}
    response = requests.post("http://127.0.0.1:8000/get_form", json=data)
    assert response.status_code == 200
    assert response.json() == {"user_email": "text", "user_phone": "phone"}

def test_invalid_phone():
    data = {"user_email": "test@example.com", "user_phone": "1234567890"}
    response = requests.post("http://127.0.0.1:8000/get_form", json=data)
    assert response.status_code == 200
    assert response.json() == {"user_email": "email", "user_phone": "text"}

def test_invalid_date():
    data = {"order_date": "wrong_format", "customer_name": "John Doe"}
    response = requests.post("http://127.0.0.1:8000/get_form", json=data)
    assert response.status_code == 200
    assert response.json() == {"order_date": "text", "customer_name": "text"}

