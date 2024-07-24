class average():
    def solution_a(A:list):
        avg=0
        for i in range(len(A)):
            avg+=A[i]
        return avg//len(A)

    def solution_b(A:list):
        i,avg=0,0
        while i<len(A):
            avg+=A[i]
            i+=1
        return avg//len(A)

    def solution_c(A:list):
        avg=0
        for i in range(len(A)-1,-1,-1):
            avg+=A[i]
        return avg//len(A)

x=[1,2,3,4,5,6,7,8,9]
print(average.solution_a(x))
print(average.solution_b(x))
print(average.solution_c(x))