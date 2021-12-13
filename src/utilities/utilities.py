"""Module for utility functions"""
from string import ascii_lowercase, digits
import secrets

def generate_id():
    """Generates a random alphanumeric four-character identifier"""
    chars = ascii_lowercase + digits
    return ''.join(secrets.choice(chars) for _ in range(4))
