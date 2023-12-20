# Hàm decorator
def thuchienpheptinh(func):
    def wrapper(a, b):
        result = func(a, b)
        print(f"Kết quả phép tính: {result}")
        return result
    return wrapper

# Sử dụng decorator để mở rộng chức năng của phép toán cộng
@thuchienpheptinh
def phepcong(a, b):
    return a + b

@thuchienpheptinh
def pheptru(a, b):
    return a - b
# pheptru = thuchienpheptinh(pheptru)

# Gọi hàm đã được decorator
phepcong(5, 5)
pheptru(25, 5)
