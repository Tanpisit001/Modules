"""Module 4: จัดการวันที่และเวลา"""
from datetime import datetime, timedelta

def get_current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def add_days(date_str, days, fmt="%Y-%m-%d"):
    date_obj = datetime.strptime(date_str, fmt)
    new_date = date_obj + timedelta(days=days)
    return new_date.strftime(fmt)

def days_between(date_str1, date_str2, fmt="%Y-%m-%d"):
    d1 = datetime.strptime(date_str1, fmt)
    d2 = datetime.strptime(date_str2, fmt)
    return abs((d2 - d1).days)
