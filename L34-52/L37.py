class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    #phải có tham chiếu đến đối tượng lớp làm tham số đầu tiên
    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    #không thể có tham số nào cả.
    @staticmethod
    def static_method():
        print("Called static_method.")
        
ClassTest.static_method()
ClassTest.class_method()
