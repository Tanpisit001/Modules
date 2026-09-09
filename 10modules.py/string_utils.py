"""Module 2: จัดการข้อความ/สตริง"""

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    clean = s.replace(" ", "").lower()
    return clean == clean[::-1]

def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")

def to_title_case(s):
    return s.title()
