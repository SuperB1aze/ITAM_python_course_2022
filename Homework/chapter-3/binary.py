class Binary:
    def __init__(self, num, other):  # инициализация объекта Binary (num - число в 10 сс)
        self.num = num
        self.other = other

        self.base = 2
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


    def __add__(self):  # сложение объекта Binary и other
        self.value = self.num_dec + self.other_dec
        self.__str__()
        print(self.stroke)

    def __sub__(self):  # вычитание other из объекта Binary
        self.value = self.num_dec - self.other_dec
        self.__str__()
        print(self.stroke)

    def __mul__(self):  # умножение объекта Binary на other
        self.value = self.num_dec * self.other_dec
        self.__str__()
        print(self.stroke)

    def __floordiv__(self):  # целочисленное деление объекта Binary на other
        self.value = self.num_dec // self.other_dec
        self.__str__()
        print(self.stroke)

    def __str__(self):  # конвертирование объекта Binary в строку
        self.converted_num = []
        self.stroke = ""

        self.converted_num.append(self.value % self.base)
        while self.value >= self.base:
            self.value = self.value // self.base
            self.converted_num.append(self.value % self.base)
        self.converted_num = self.converted_num[::-1]
        for i in range(0, len(self.converted_num)):
            self.stroke += str(self.converted_num[i])