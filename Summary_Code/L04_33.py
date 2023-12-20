import random

# Hàm tạo id ngẫu nhiêu có độ dài 8 số
def generate_random_id():
    return str(random.randint(10000000, 99999999))

def main():
    # Lệnh input
    student_info = input("Nhập thông tin sinh viên (tên, tuổi, điểm thi - cách nhau bằng dấu phẩy): ")
    # Destructuring variables
    name, age, test_grade = [info.strip() for info in student_info.split(',')]

    # Hiển thị thông tin sinh viên sử dụng dictionaries
    student_data = {'Tên': name, 'Tuổi': age, 'Điểm': test_grade}
    print("Thông tin sinh viên:")
    for key, value in student_data.items():
        print("{}: {}".format(key, value))

    # Sử dụng mệnh đề if và toán tử so sánh
    if float(test_grade) >= 8.0:
        print("Sinh viên {} đã có kết quả thi xuất sắc.".format(name))
    else:
        print("Sinh viên {} đã có kết quả thi không xuất sắc.".format(name))

    # Sử dụng vòng lặp while
    i = 1
    while i <= 3:
        print("Lần {} kiểm tra".format(i))
        i += 1

    # Sử dụng list comprehensions để tạo danh sách từ biểu thức
    grades = [float(input("Nhập điểm cho lần kiểm tra {}: ".format(j + 1))) for j in range(3)]

    # Sử dụng tuple và set
    grades_tuple = tuple(grades)
    unique_grades_set = set(grades)

    # Sử dụng intersection và difference trong list
    best_grades = {8, 9, 10}
    excellent_grades = unique_grades_set.intersection(best_grades)
    other_grades = list(unique_grades_set.difference(best_grades))

    # Sử dụng dictionaries cho thông tin về kiểm tra điểm
    grades_data = {
        'Danh sách điểm': grades,
        'Tuple điểm': grades_tuple,
        'Set điểm (không lặp)': unique_grades_set,
        'Điểm xuất sắc': excellent_grades,
        'Điểm khác': other_grades,
    }

    # Hiển thị thông tin về điểm
    for key, value in grades_data.items():
        # Lệnh format
        print("{}: {}".format(key, value))

    # Sử dụng lambda functions và dictionaries comprehensions để thay đổi điểm
    transform_grade = lambda x: x
    transformed_numbers = {j + 1: transform_grade(grades[j]) for j in range(3)}
    transformed_data = {'Điểm của mỗi lần kiểm tra': transformed_numbers}

    # Hiển thị thông tin về điểm sử dụng dictionaries
    for key, value in transformed_data.items():
        print("{}: {}".format(key, value))

    greeting = greet_student(name)
    print(greeting)

    # Sử dụng unpacking arguments và unpacking keyword arguments
    # Lấy thông tin tự động
    person_info = {'name': name, 'age': age, 'id': generate_random_id()}
    print_person_info(**person_info)

# Function parameters
# Sử dụng default parameter values
def greet_student(name="Unknown"):
    # Function arguments 
    # Functions returning values
    return "Chào mừng, {}!".format(name)

def print_person_info(name, age, id):
    print("Thông tin người dùng đăng nhập: Tên: {}, Tuổi: {}, ID: {}".format(name, age, id))

if __name__ == "__main__":
    main()
