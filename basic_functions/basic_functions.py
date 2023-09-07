from decimal import Decimal


def add(a:any,b:any):
    """function that adds 2 numbers and formats according to input type"""
    result=0
    if isinstance(a and b, int):
        print(f"number {a} and {b} are int")
        result=int(a+b)
    elif (isinstance(a, float) or isinstance(b, float)):
        print(f"number {a} or {b} is float")
        result=float(a+b)
    elif (isinstance(a, str) or isinstance(b, str)):
        print(f"number {a} or {b} is a string")
        result=float(a+b)

    return result


my_new_result=add("2","3")
print(f"Result is: {my_new_result} and is of type: {type(my_new_result)}")