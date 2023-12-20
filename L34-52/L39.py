class Device:
    def __init__(self, name, connected_by):
        self.name = str(name)
        self.connected_by = str(connected_by)
        self.connected = True

    def __str__(self):
        #giá trị của biến ược hiển thị bằng cách sử dụng hàm repr() để lấy chuỗi biểu diễn
        return f"Device {self.name!r}({self.connected_by})"
    
    def disconnected(self):
        self.connected = False
        print("Disconnected.")

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = int(capacity)
        self.remaining_pages = int(capacity)

    def __str__(self):
        return f"{super().__str__()}({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected!")
            return
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages


printer = Printer("Printer", "USB", 500)
printer.print(20)

print(printer)

printer.disconnected()
printer.print(30)

