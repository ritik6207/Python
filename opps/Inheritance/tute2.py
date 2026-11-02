# The super() function

class ParentDemo:
    def __init__(self, msg):
        self.msg = msg
    def showMessage(self):
        print(self.msg)
class ChildDemo(ParentDemo):
    def __init__(self, msg):
        super().__init__(msg)
obj = ChildDemo("Welcome to Super Method")
obj.showMessage()