def example(*a, **k):
    # Xử lý các đối số là 1 danh sách không xác định số lượng phần tử được truyền thông qua *args
    print("Các đối số được truyền thông qua *args: ", a)
    
    # Xử lý các đối số là 1 dictionary chưa xác định số lượng cặp key - value được truyền thông qua **kwargs
    print("Các đối số được truyền thông qua **kwargs: ", k)
    
    for arg in a:
        print(f"Các đối số nhập vào là: {arg}")

    for key, value in k.items():
        print(f"Các đối số từ khóa nhập vào: - {key}: {value}")

# Gọi hàm với các đối số khác nhau
example(5, 2, 3, name="Hoa", age=25)

