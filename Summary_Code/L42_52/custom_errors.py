# File: custom_errors.py

#Custom error classes

class MathError(Exception):
    """Lớp ngoại lệ chung cho các lỗi toán học."""
    pass

class DivisionByZeroError(MathError):
    """Lớp ngoại lệ cho trường hợp chia cho không."""
    pass

class ValueError(MathError):
    """Lớp ngoại lệ cho trường hợp giá trị không hợp lệ."""
    pass
