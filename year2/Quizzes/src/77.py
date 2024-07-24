class parity():
    def parity_check(data:str):
        count=0
        for i in range(1,len(data)):
            if data[i]=='1':
                count+=1
        if count%2==0 and data[0]==1:
            return True
        else:
            return False

print(parity.parity_check("100111001011001110010110011100101"))
print(parity.parity_check("011101111101110111110111001111"))