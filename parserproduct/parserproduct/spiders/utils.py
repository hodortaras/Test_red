"""
Модуль для преобразования строковых цен с розетки в тип float
"""

def str_to_float_join(list_of_price):
    price=''
    for part in list_of_price:
        price+=part
    price=float(price)
    return price
