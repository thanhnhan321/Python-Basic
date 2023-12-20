# File: main.py

# Relative imports in Python
from math_operations.basic_operations import add, subtract
from math_operations.advanced_operations import multiply, divide
from custom_errors import MathError, DivisionByZeroError, ValueError

def thuc_hien_phep_toan(phep_toan, m, n):
    try:
        ket_qua = phep_toan(m, n)
        print(f"Kết quả của phép toán: {ket_qua}")
    except MathError as e:
        print(f"Lỗi Toán học: {e}")

if __name__ == "__main__":
    m = int(input("Nhap m= "))
    n = int(input("Nhap n= "))

    thuc_hien_phep_toan(add, m, n)

    # Sử dụng first-class functions
    thuc_hien_phep_toan(subtract, m, n)

    thuc_hien_phep_toan(multiply, m, n)

    thuc_hien_phep_toan(divide, m, n)

    # Thử nghiệm phép nhân với tham số không hợp lệ
    try:
        ket_qua_khong_hop_le = multiply(m, n)  # Điều này sẽ gây ra một ValueError
    except ValueError as e:
        pass

    try:
        ket_qua_khong_hop_le = divide(m, n)  # Điều này sẽ gây ra một DivisionByZeroError
    except DivisionByZeroError as e:
        pass

    