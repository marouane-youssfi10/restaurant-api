import datetime
import string
import random


def order_ref_generator(size=5, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))


def generate_order_number():
    # Generate order number
    yr = int(datetime.date.today().strftime("%Y"))
    dt = int(datetime.date.today().strftime("%d"))
    mt = int(datetime.date.today().strftime("%m"))
    d = datetime.date(yr, mt, dt)
    current_date = d.strftime("%d%m%Y")  # 20210305
    order_number = current_date + str(order_ref_generator())
    return order_number
