"""Module 3: จัดการไฟล์เบื้องต้น"""
import os

def write_text_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return f"เขียนไฟล์ {path} สำเร็จ"

def read_text_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def file_exists(path):
    return os.path.exists(path)

def get_file_size(path):
    return os.path.getsize(path) if os.path.exists(path) else -1
