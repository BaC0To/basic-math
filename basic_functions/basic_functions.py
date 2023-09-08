import decimal

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
        if isinstance(self.a,str) or isinstance(self.b,str):
            raise TypeError(f"Stage.__init__ called with a non-numeric value")
                       


    def add(self):
        """Return the sum of two numbers.

        Args:
            self (int/float): two numbers in integer or float format.

        Returns:
            int/float: sum of two numbers in int or float format.
        """
        
        return self.a+self.b
    
    def subtract(self):
        """Return the subtraction of two numbers.

        Args:
            self (int/float): two numbers in integer or float format.

        Returns:
            int/float: sum of two numbers in int or float format.
        """
        
        return self.a-self.b
    

    def multiply(self):
        """Return the multiplication of two numbers.

        Args:
            self (int/float): two numbers in integer or float format.

        Returns:
            int/float: multiplication of two numbers in int or float format.
        """
        
        return self.a*self.b


    def divide(self):
        """Return the multiplication of two numbers.

        Args:
            self (int/float): two numbers in integer or float format.

        Returns:
            int/float: division of two numbers in int or float format.
        """
        
        return self.a/self.b
    

num1=4.233
num2=1.23

final_precision=0
num1_precision=0
num2_precision=0

if "." in str(num1):
    num1_precision=(len(str(num1).split(".")[-1]))
    
if "." in str(num2):
    num2_precision=(len(str(num2).split(".")[-1]))

if num2_precision>=num1_precision:
    final_precision=num2_precision

if num2_precision<num1_precision:
    final_precision=num1_precision

x=BasicMath(num1,num2)


#print(f"Result is: {x.divide()}")
print(f"Result is: {x.divide():.{final_precision}f}")