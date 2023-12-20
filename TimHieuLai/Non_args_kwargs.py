def example(arg1, arg2, arg3, name=None, age=None, city=None):
    print(f"Các đối số nhập vào là: {arg1}, {arg2}, {arg3}")

    if name is not None:
        print(f"Tên: {name}")
    if age is not None:
        print(f"Tuổi: {age}")
    if city is not None:
        print(f"Thành phố: {city}")

# Gọi hàm với các đối số khác nhau
example(5, 2, 3, name="Hoa", age=25, city="HCM city")
