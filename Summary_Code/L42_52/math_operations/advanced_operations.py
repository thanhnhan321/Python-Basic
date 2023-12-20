# File: math_operations/advanced_operations.py

from custom_errors import DivisionByZeroError, ValueError

#Simple decorators in Python
def validate_parameter(value_limit):
    def decorator(func):
        def wrapper(*args):
            # Kiểm tra giá trị của tham số ở đây
            for arg in args:
                if arg > value_limit:
                    raise ValueError(f" {arg} vượt qua giá trị giới hạn là {value_limit}.")
            return func(*args)
        return wrapper
    return decorator

# The '@' syntax for decorators

@validate_parameter(value_limit=10)
def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise DivisionByZeroError("Không thể chia cho 0.")
    return a / b
