class Calculator:
    calculator_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculator_type}")
        return a * b