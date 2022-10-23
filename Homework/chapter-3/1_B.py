from binary import Binary

class Ternary(Binary):
    def __init__(self, num, other):
        self.num = num
        self.other = other

        self.base = 3
        self.num_str = str(self.num)
        self.other_str = str(self.other)
        self.num_dec = 0
        self.other_dec = 0

        for i in range(len(self.num_str)):
            self.num_dec += int(self.num_str[i]) * (self.base ** (len(self.num_str) - i - 1))

        for i in range(len(self.other_str)):
            self.other_dec += int(self.other_str[i]) * (self.base ** (len(self.other_str) - i - 1))

        self.__add__()           
        self.__sub__()
        self.__mul__()
        self.__floordiv__()

a = Ternary(10, 2)