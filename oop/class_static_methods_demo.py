class Calculator:
    # Class attribute used by the class method
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method that returns the sum of two numbers.
        Does not depend on class or instance state.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method that returns the product of two numbers.
        Prints the class-level calculation_type before multiplying.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b