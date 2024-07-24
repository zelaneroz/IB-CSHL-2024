def division(a:int,b:int)->float:
    if not isinstance(a,int):
        raise TypeError("Error. Input must be an integer")
    if not isinstance(b,int):
        raise TypeError("Error. Input must be an integer")
    if b==0:
        raise ValueError("Cannot divide by zero")
    return a/b