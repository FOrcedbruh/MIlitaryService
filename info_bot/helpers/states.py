

class OrderByNumberState:

    def __init__(self):
        self.state: bool = False

    def set_true(self):
        self.state = True
    
    def set_false(self):
        self.state = False