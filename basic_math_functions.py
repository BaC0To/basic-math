class BasicMath:
    

    @staticmethod            
    def add(number1, number2):
        """Sum function of two numbers.

        :params the numbers to be added
        :returns: the result of summation
        """
        return number1 + number2
    
    @staticmethod 
    def subtract(number1, number2):
        """Subtract function of two numbers.

        :params the numbers to be subtracted
        :returns: the result of subtraction
        """
        return number1 - number2
    
    @staticmethod 
    def multiply(number1, number2):
        """Multiply function of two numbers.

        :params the numbers to be multiplied
        :returns: the result of multiplication
        """
        return number1 * number2

    @staticmethod 
    def divide(number1, number2):
        """Divide function of two numbers.

        :params the numbers to be multiplied
        :returns: the result of division
        """
        if number2 == 0:
            raise ValueError("Can't divide by \"0\"...")
        return number1 / number2
