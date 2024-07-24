# **Quiz 2**
Given 2 numbers, A and B, Output TRUE if one of them is 20 or if their sum is 20.
[HL] You receive two lists of numbers A, and B
<img width="300" alt="Screen Shot 2022-09-22 at 1 50 36 AM" src="https://user-images.githubusercontent.com/113817801/191564615-b50206bd-3151-4879-be4e-0bf15f92f87c.png">



### **Flowchart**
<img width="323" alt="Screen Shot 2022-09-23 at 2 55 21 PM" src="https://user-images.githubusercontent.com/113817801/191899704-7219d95d-73a0-4f15-ad33-71a8548f7b7c.png">



### **Code**
```
a = [int(b) for b in input("Enter a set of values separated by a space :  ").split()]
b = [int(b) for b in input("Enter another set of values separated by a space:  ").split()]

i=0    #while loop iterator
c=0    #temporary boolean value
while i<len(a):
  if a[i]+b[i]==20:
    c+=1
  elif a[1]==20 or b[i]==20:
    c+=1
  i+=1

print(bool(c))
```

### **Proof**

<img width="500" alt="Screen Shot 2022-09-22 at 1 53 57 AM" src="https://user-images.githubusercontent.com/113817801/191565324-66a6b4d0-b2df-42c1-824b-6a3d5481e0ab.png">
<img width="500" alt="Screen Shot 2022-09-22 at 1 55 31 AM" src="https://user-images.githubusercontent.com/113817801/191565616-28e16917-a932-490b-bcc8-64d7992a1b56.png">
<img width="500" alt="Screen Shot 2022-09-22 at 1 57 10 AM" src="https://user-images.githubusercontent.com/113817801/191565938-293e77b8-0160-4c7a-a37d-2554cb6ccd70.png">
