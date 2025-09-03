class Secret:
    def __init__(self):
        self.__code = 1234  # private attribute

    def show_code(self):
        print(f"Code: {self.__code}")

s = Secret()
s.show_code()