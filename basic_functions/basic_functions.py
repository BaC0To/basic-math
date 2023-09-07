class BasicMath:
    """Basic math class with functions + - * / """
    def __init__(self,result=any):
        self.result=result


    def add(self,a,b):
        """function that adds 2 numbers and result is according to input type"""
        result=None
        if isinstance(a and b, int): # check for both inputs==integers
            print(f"number {a} and {b} are int")
            result=int(a+b)

        if (isinstance(a, float) or isinstance(b, float)):# check if any input is float
            print("One of the input numbers is float")
            result=float(a+b)

        if (isinstance(a, str) or isinstance(b, str)):# check if any input is string
            print(f"number {a} or {b} is a string")
            result= None


        return result


object1=BasicMath()
function_type=input("What kind of basic math over the following 2 numbers you'll want? [A]dd, [S]ubtract, [Divide] or [Multiply] -> ?").upper()
if function_type=="A":
    my_result=object1.add(2,3.1)
    print(f"Result is: {my_result} and is of type: {type(my_result)}")