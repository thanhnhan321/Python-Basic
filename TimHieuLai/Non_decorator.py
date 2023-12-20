def thuchienpheptinh(func, a, b):
    result = func(a, b)
    print(f"Kết quả phép tính: {result}")
    return result

def phepcong(a, b):
    return a + b

def pheptru(a, b):
    return a - b

# Gọi hàm và in kết quả
thuchienpheptinh(phepcong, 5, 5)
thuchienpheptinh(pheptru, 25, 5)
