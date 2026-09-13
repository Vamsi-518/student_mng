class Engine:
    def start(self):
        print("Engine started")

class Vehicle:
    def __init__(self):
        self.engine = Engine()

    def move(self):
        self.engine.start()
        print("Vehicle is moving")

v = Vehicle()
v.move()