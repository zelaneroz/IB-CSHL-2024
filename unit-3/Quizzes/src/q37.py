class CompoundInterest:
    def __init__(self,principal,rate,num_years):
        self.principal=principal
        self.rate=rate
        self.numyears=num_years

    def calculate_interest(self):
        interest=round(self.principal*(1+self.rate)**self.numyears, 2)
        return interest

class AccountingProgram(CompoundInterest):
    def __init__(self):
        self.compound=CompoundInterest(0,0,0)

    def set_principal(self,principal):
        if principal<0:
            raise ValueError("Principal should be greater than zero")
        else:
            self.compound.principal=principal

    def set_rate(self,rate:int):
        if rate<0:
            raise ValueError("Interest rate should be greater than zero")
        else:
            self.compound.rate=rate

    def set_years(self,years:int):
        if years<0:
            raise ValueError("Years should be greater than zero")
        else:
            self.compound.numyears=years

    def calculate_interest(self):
        return self.compound.calculate_interest()