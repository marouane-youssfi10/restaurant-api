import string
import random


def generate_order_number(size=5, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))
