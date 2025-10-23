import random


def generate_id():
    """
    Generate a random 15-digit number as a string.
    Returns a string to preserve leading zeros if any.
    """
    # Generate a random 15-digit number
    # Range: 100000000000000 to 999999999999999
    return str(random.randint(100000000000000, 999999999999999))
