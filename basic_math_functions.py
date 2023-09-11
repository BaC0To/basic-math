class BasicMath:
    

    @staticmethod            
    def add(parameters):
        """Sum function of numbers except strings.

        :params: the numbers to be added
        :returns: the result of summation
        """
        result = 0
        for item in parameters:
            if isinstance(item,str):
                raise TypeError(f"Item \"{item}\" type is: {type(item)} instead of number!")
            result = result + item
        return result
            
    @staticmethod 
    def subtract(number1, number2):
        """Subtract function of two numbers.

        :params: the numbers to be subtracted
        :returns: the result of subtraction
        """
        return number1 - number2
    
    @staticmethod 
    def multiply(number1, number2):
        """Multiply function of two numbers.

        :params: the numbers to be multiplied
        :returns: the result of multiplication
        """
        return number1 * number2

    @staticmethod 
    def divide(number1, number2):
        """Divide function of two numbers.

        :params: the numbers to be multiplied
        :returns: the result of division
        """
        if number2 == 0:
            raise ValueError(f"Can't divide by \"{number2}\"...")
        return number1 / number2
