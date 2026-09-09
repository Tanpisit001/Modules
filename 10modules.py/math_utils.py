"""Module 1: คำนวณทางคณิตศาสตร์พื้นฐาน"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("หารด้วยศูนย์ไม่ได้")
    return a / b

def factorial(n):
    if n < 0:
        raise ValueError("ต้องเป็นจำนวนเต็มไม่ติดลบ")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
