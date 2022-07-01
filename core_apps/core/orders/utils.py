import datetime


def generate_order_number(data):
    # Generate order number
    yr = int(datetime.date.today().strftime("%Y"))
    dt = int(datetime.date.today().strftime("%d"))
    mt = int(datetime.date.today().strftime("%m"))
    d = datetime.date(yr, mt, dt)
    current_date = d.strftime("%d%m%Y")  # 20210305
    order_number = current_date + str(data.pkid)
    return order_number
