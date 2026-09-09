"""Module 8: สุ่มค่าต่างๆ"""
import random
import string

def random_number(min_val=1, max_val=100):
    return random.randint(min_val, max_val)

def random_string(length=8):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))

def shuffle_list(items):
    shuffled = items.copy()
    random.shuffle(shuffled)
    return shuffled

def pick_random_item(items):
    return random.choice(items)
