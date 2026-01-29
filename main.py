class Calculator:
    def add(self, a, b):
        if self.__is_valid_number(a) and self.__is_valid_number(b):
            return a + b
        else:
            return None

    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def power(self, base, exponent):
        return self.__multiply_repeatedly(base, exponent)
    
    def factorial(self, n):
        factorial_value = 1

        for i in range(5, 0, -1):
            factorial_value *= i

        return factorial_value
    
    def __is_valid_number(self, value):
        if type(value) == int or type(value) == float:
            return True
        else:
            return False

    def __multiply_repeatedly(self, base, times):
        total = 1
        
        for i in range(1, times + 1):
            total *= base

        return total

            





my_calc = Calculator()

# print(my_calc.add(12, 3))
# print(my_calc.subtract(10, 6))
# print(my_calc.multiply(23, 100))
print(my_calc.power(3, 5))
# print(my_calc.factorial(5))
# print(my_calc._factorial_numbers(True))
# print(my_calc._multiply_repeatedly(2, 3))