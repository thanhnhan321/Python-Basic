class Parent:
    def call_child_method(self):
        print("Phương thức của lớp cha được gọi bởi đối tượng của lớp con")

class Child(Parent):
    def child_method(self):
        print("Phương thức của lớp con được gọi")

# Tạo một đối tượng từ lớp con
child_instance = Child()

# Gọi phương thức của lớp cha, từ đối tượng của lớp con
child_instance.call_child_method()
