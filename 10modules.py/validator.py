"""Module 5: ตรวจสอบความถูกต้องของข้อมูล"""
import re

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

def is_valid_phone(phone):
    pattern = r"^0[0-9]{9}$"
    return re.match(pattern, phone) is not None

def is_numeric(value):
    return str(value).replace(".", "", 1).isdigit()
