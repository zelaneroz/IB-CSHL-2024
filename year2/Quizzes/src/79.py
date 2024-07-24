class palindrome():
    def reverse(text:str):
        new=""
        for i in range(len(text)):
            new+=text[len(text)-1-i]

    def palindrome_numcheck(self,A:int,B:int):
        output=[]
        for j in range(A,B+1):
            if j==int(self.reverse(str(j))):
                output.append(j)
        return output