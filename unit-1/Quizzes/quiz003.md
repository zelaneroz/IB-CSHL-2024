# **Quiz 3**
Create a program that translate the proteins in the DNA chain
[HL]  Input is a whole protein chain as a string


### **Flowchart**

<img width="192" alt="Screen Shot 2022-09-25 at 8 35 19 PM" src="https://user-images.githubusercontent.com/113817801/192141354-2f409d1a-cbd0-4a6e-822d-d902a00eee0a.png">

### **Code**
```
dna = ['','A','C','G','T']
a = str(input())

i,j, output ='',0, ''
for i in a:
    while j<5:
        if i == dna[j]:
            output+= dna[j*-1]
        j+=1
    j=0
print(output)
```

### **Proof**
<img width="256" alt="Screen Shot 2022-09-23 at 11 13 20 PM" src="https://user-images.githubusercontent.com/113817801/191980863-d0f38469-e8fe-41b8-979a-227210dd9f0b.png">
