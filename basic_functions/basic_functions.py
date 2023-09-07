class BasicMath:
    """
    A class to represent a BasicMath object.

    ...

    Attributes
    ----------
    a : int/float
        first nnumber
    b : int/float
        second number
    
    Methods
    -------
    add():
        Summation of two numbers.
    subtract():
        Subtraction of two numbers.
    multiply():
        Multiplication of two numbers.
    divide():
        Division of two numbers.

    """


    def __init__(self,a,b):
        """
        Constructs all the necessary attributes for the BasicMath object.

        Parameters
        ----------
            a : int/float
                first number
            b : int/float
                second number
        """

        self.a=a
        self.b=b      
    
    def add(self):
        """Return the sum of two numbers.

        Args:
            self (int/float): two numbers in integer or float format.

        Returns:
            int/float: sum of two numbers in int or float format.
        """


        if isinstance(self.a and self.b, int): # check for both inputs==integers
            return int(self.a+self.b)
    
        if (isinstance(self.a, float) or isinstance(self.b, float)):# check if any input is float
            return float(self.a+self.b)


    def subtract(self):
        """Return the subtraction of two numbers.

        Args:
            self (int/float): two numbers in integer or float format.

        Returns:
            int/float: subtraction of two numbers in int or float format.
        """


        if isinstance(self.a and self.b, int): # check for both inputs==integers
                return int(self.a-self.b)
        
        if (isinstance(self.a, float) or isinstance(self.b, float)):# check if any input is float
                return float(self.a-self.b)


    def multiply(self):
        """Return the multiplication of two numbers.

        Args:
            self (int/float): two numbers in integer or float format.

        Returns:
            int/float: multiplication of two numbers in int or float format.
        """ 


        if isinstance(self.a and self.b, int): # check for both inputs==integers
            return int(self.a*self.b)
        
        if (isinstance(self.a, float) or isinstance(self.b, float)):# check if any input is float
            return float(self.a*self.b)
            
    def divide(self):
        """Return the division of two numbers.

        Args:
            self (int/float): two numbers in integer or float format.

        Returns:
            int/float: division of two numbers in int or float format.
        """


        try:
            if isinstance(self.a and self.b, int): # check for both inputs==integers
                return int(self.a/self.b)
            
            if (isinstance(self.a, float) or isinstance(self.b, float)):# check if any input is float
                return float(self.a/self.b)
        except ZeroDivisionError:
            print("illigal division by zero")

            
x=BasicMath(4,4.2)
print(f"Result is: {x.multiply()}")
