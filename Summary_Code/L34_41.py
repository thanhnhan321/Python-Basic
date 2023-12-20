from typing import List

#Object-Oriented Programming in Python
class Person:
    def __init__(self, name: str, age: int):
        # Khởi tạo đối tượng Person với tên và tuổi
        self.name = name
        self.age = age

    def __str__(self) -> str:
        # Phương thức để hiển thị thông tin của đối tượng dưới dạng dễ đọc
        return f"{self.name} ({self.age} tuổi)"

    def __repr__(self) -> str:
        # Phương thức để tạo chuỗi biểu diễn chính xác của đối tượng
        return f"{self.__class__.__name__}('{self.name}', {self.age})"

    @classmethod
    def create_person(cls, name: str, age: int) -> 'Person':
        # Phương thức class để tạo đối tượng Person
        return cls(name, age)

    @staticmethod
    def is_adult(age: int) -> bool:
        # Phương thức static để kiểm tra xem một người có đủ tuổi làm việc hay không
        return age >= 18

class Student(Person):
    def __init__(self, name: str, age: int, student_id: int):
        # Kế thừa từ Person và thêm thuộc tính student_id
        super().__init__(name, age)
        self.student_id = student_id

    def __repr__(self) -> str:
        # Ghi đè phương thức __repr__ để tạo chuỗi biểu diễn chính xác của học viên
        return f"{self.__class__.__name__}('{self.name}', {self.age}, {self.student_id})"

    def __str__(self) -> str:
        # Ghi đè phương thức __str__ để hiển thị thông tin học viên
        return f"Sinh viên {super().__str__()}, ID: {self.student_id}"

# Class inheritance
class Teacher(Person):
    def __init__(self, name: str, age: int, courses: List[str]):
        # Kế thừa từ Person và thêm thuộc tính courses
        super().__init__(name, age)
        self.courses = courses

    def __str__(self) -> str:
        # Ghi đè phương thức __str__ để hiển thị thông tin giáo viên
        return f"Giáo viên: {super().__str__()}, Các môn giảng dạy: {', '.join(self.courses)}"

    def __repr__(self) -> str:
        # Ghi đè phương thức __repr__ để tạo chuỗi biểu diễn chính xác của giáo viên
        return f"{self.__class__.__name__}('{self.name}', {self.age}, {self.courses})"

    @classmethod
    def create_teacher(cls, name: str, age: int, courses: List[str]) -> 'Teacher':
        # Phương thức class để tạo đối tượng Teacher
        return cls(name, age, courses)

#Class composition
class School(Person):
    def __init__(self, name: str, students: List[Student], teachers: List[Teacher]):
        # Khởi tạo đối tượng School với tên, danh sách học viên, và danh sách giáo viên
        self.name = name
        self.students = students
        self.teachers = teachers

    def __str__(self) -> str:
        # Phương thức để hiển thị thông tin về trường học
        student_info = "\n".join([f"  - {student}" for student in self.students])
        teacher_info = "\n".join([f"  - {teacher}" for teacher in self.teachers])
        return f"Trường học: {self.name}\n\nDanh sách học viên và giáo viên hiện tại\nHọc viên:\n{student_info}\nGiáo viên:\n{teacher_info}"

    #Type hinting in Python 3.5
    def __repr__(self) -> str:
        # Phương thức để tạo chuỗi biểu diễn chính xác của đối tượng School
        return f"{self.__class__.__name__}('{self.name}', {self.students}, {self.teachers})"


if __name__ == "__main__":
    # Sử dụng @classmethod để tạo đối tượng Person
    name = str(input("Nhập tên: "))
    age = int(input("Nhập tuổi: "))
    person = Person.create_person(name, age)

    # Sử dụng @staticmethod để kiểm tra xem một người có đủ tuổi tham gia khóa học chưa
    is_adult = Person.is_adult(age)
    print(f"Có phải bạn đã đủ tuổi để tham gia khóa học? {is_adult}\n")

    print("Thông tin khóa học:")
    # Sử dụng @classmethod để tạo đối tượng teacher
    teacher = Teacher.create_teacher("Mr Thanh", 40, ["Lịch Sử", "Địa Lý"])
    print(teacher)

    # Tạo đối tượng Trường học và hiển thị thông tin
    school = School("HCMUS", [Student("Hoa", 20, 123)], [teacher])
    print(school)
