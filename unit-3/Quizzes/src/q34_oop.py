class quiz34:
    def __init__(self,num:int):
        self.num=num
        print("An object has been created")
    def to_roman(self)->str:
        num = self.num
        if num > 100:
            raise ValueError("Please input a number no greater than 100")
        converted = ""
        numbers,romans,i = [1, 4, 5, 9, 10, 40, 50, 90, 100],['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C'],8
        while num:
            div = num // numbers[i]
            num %= numbers[i]
            while div:
                converted += str(romans[i])
                div -= 1
                if div == 0:
                    break
            i -= 1
        return converted

case1 = quiz34(num=1)
solution = case1.to_roman()
print(solution)
