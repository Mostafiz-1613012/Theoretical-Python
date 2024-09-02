class Calculator:

    def addi(self, x, y):
        return x + y

    def subt(self, x, y):
        return x - y

    def mult(self, x, y):
        return x * y

    def divi(self, x, y):
        if y == 0:
            raise ValueError("Not")
        return x / y