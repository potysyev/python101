class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"({self.a} + {self.b}i)"

    def __add__(self, other):
        if isinstance(other, ComplexNum):
            return ComplexNum(self.a + other.a, self.b + other.b)
        else:
            raise ValueError("Cannot add complex number with not complex number")

    def __sub__(self, other):
        if isinstance(other, ComplexNum):
            return ComplexNum(self.a - other.a, self.b - other.b)
        else:
            raise ValueError("Cannot add complex number with not complex number")

    def __mul__(self, other):
        if isinstance(other, ComplexNum):
            return ComplexNum((self.a * other.a - self.b * other.b), (self.b * other.a + self.a * other.b))
        else:
            raise ValueError("Cannot add complex number with not complex number")


if __name__ == "__main__":
    num1 = ComplexNum(1, 2)
    num2 = ComplexNum(2, 3)
    num3 = num1 + num2
    print(num3)
    num4 = num1 * num2
    print(num4)
