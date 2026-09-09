"""Module 7: บันทึกข้อความล็อกอย่างง่าย"""
from datetime import datetime

def log_info(message):
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[INFO {timestamp}] {message}")

def log_error(message):
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[ERROR {timestamp}] {message}")

def log_warning(message):
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[WARNING {timestamp}] {message}")
