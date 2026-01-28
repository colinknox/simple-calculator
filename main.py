class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def power(self, base, exponent):
        return base ** exponent
    
    def factorial(self, n):
        factorial_value = 1

        for i in range(5, 0, -1):
            factorial_value *= i

        return factorial_value
    
    def __factorial_numbers(self, value):
        if type(value) == int or type(value) == float:
            return True
        else:
            return False

my_calc = Calculator()

# print(my_calc.add(1, 3))
# print(my_calc.subtract(10, 6))
# print(my_calc.multiply(23, 100))
# print(my_calc.power(3, 5))
# print(my_calc.factorial(5))
print(my_calc._factorial_numbers(True))