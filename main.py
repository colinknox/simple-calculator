class Calculator:
    def add(self, a, b):
        if self.__is_valid_number(a) and self.__is_valid_number(b):
            return a + b
        else:
            print("ERROR: Please input either a integer or a float")
            return None

    def subtract(self, a, b):
        if self.__is_valid_number(a) and self.__is_valid_number(b):
            return a - b
        else:
            print("ERROR: Please input either a integer or a float")
            return None
    
    def multiply(self, a, b):
        if self.__is_valid_number(a) and self.__is_valid_number(b):
            return a * b
        else:
            print("ERROR: Please input either an integer or a float")
            return None
    
    def power(self, base, exponent):
        if self.__is_valid_number(base) and self.__is_valid_number(exponent):
            return self.__multiply_repeatedly(base, exponent)
        else:
            print("ERROR: Please input either a integer or a float")
            return None
    
    def factorial(self, n):
        factorial_value = 1

        if self.__is_valid_number(n) and type(n) == int:
            if n == 0:
                return 1
            elif n >= 0:
                for i in range(n, 0, -1):
                    factorial_value *= i
            else:
                print("ERROR: Please input a positive integer")
                return None
        else:
            print("ERROR: Please input a valid integer")
            return None

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
