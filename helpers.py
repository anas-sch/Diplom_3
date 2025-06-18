import random
import string
import time

def generate_unique_email():
    return f"test_{''.join(random.choices(string.ascii_lowercase, k=5))}@examlpe.com"