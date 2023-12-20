# Sử dụng lambda để bình phương mỗi phần tử của danh sách
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))

print(squared_numbers)  # Kết quả: [1, 4, 9, 16, 25]
