def to_roman(num:int)->str:
    if num>100:
        raise ValueError("Please input a number no greater than 100")
    converted=""
    numbers = [1,4,5,9,10,40,50,90,100]
    romans = ['I','IV','V','IX','X','XL','L','XC','C']
    i = 8

    while num:
        div=num//numbers[i]
        num %= numbers[i]

        while div:
            converted+=str(romans[i])
            div-=1
            if div==0:
                break
        i-=1
    return converted