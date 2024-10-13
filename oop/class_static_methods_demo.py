class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static method
    @staticmethod
    def add(a, b):
        """Returns the sum of two numbers"""
        return a + b

    # Class method
    @classmethod
    def multiply(cls, a, b):
        """Returns the product of two numbers, and prints the class attribute 'calculation_type'"""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

from class_static_methods_demo import Calculator

def main():
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()
