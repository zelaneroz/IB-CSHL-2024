import random

class Account:
    def __init__(self):
        self.balance=0
        self.holder_name=""
        self.holder_email=""
        m,n,o=random.randint(100,999),random.randint(10000,99999),random.randint(0,9)
        self.number = [m,n,o]
        #Make 3 randomized number: 999, 99999,9
        # Number Digit: ###-#####-#

    def get_account_no(self)->str:
        return f"{self.number[0]}-{self.number[1]}-{self.number[2]}"

    def set_holder_name(self,name:str)->str:
        if not isinstance(name,str):
            raise ValueError("Error. Input must be a string.")
        self.holder_name=name
        return f"Holder's name set to {self.holder_name}"

    def set_holder_email(self,email:str)->str:
        self.holder_email=email
        return f"Holder's email set to {self.holder_email}"

    def get_balance(self)->int:
        return self.balance

    def deposit(self,amount:int)->str:
        self.balance+=amount
        return f"New balance: {self.balance} USD"

# case1 = Account()
# solution = case1.get_account_no()
# print(solution)
# print(solution.split("-"))