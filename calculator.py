class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b
    #change b - a into a - b

    def multiply(self, a, b):
        result = 0
        for i in range(abs(b)):
            result = self.add(result, abs(a))
        return result if (a >= 0 and b >= 0) or (a < 0 and b < 0) else -result
    #Add multiplying with both and one negative number

    def divide(self, a, b):
        if b==0:
            return "Undefined"
        result = 0
        abs_a, abs_b = abs(a), abs(b)
        while abs_a >= abs_b:
            abs_a = self.subtract(abs_a, abs_b)
            result += 1
        if (a < 0) != (b < 0):
            result = -result
        return result
    #Add case b=0 and negative number
    
    def modulo(self, a, b):
        if b==0:
            return "Undefined"
        if a==0:
            return 0
        while a >= b:
            a = a-b
        return a
    #Add case a,b=0 and negative number

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(5, 2))
    print("Example: multiplication: ", calc.multiply(3, 7))
    print("Example: division: ", calc.divide(5, 2))
    print("Example: modulo: ", calc.modulo(5, 2))