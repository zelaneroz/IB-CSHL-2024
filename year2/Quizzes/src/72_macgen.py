import random
class macgen():
    def macgenerator(N:int):
        output,temp,chars,i=[],"","0123456789ABCDEF",0
        while i<N:
            for a in range(6):
                for b in range(2):
                    temp+=f"{chars[random.randint(0,15)]}"
                temp+=":"
            if temp not in output:
                output.append(temp[:-1])
                i+=1
        return output

print(macgen.macgenerator(2))


