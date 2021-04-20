

N = int(input())
A = list(map(int,input().split()))

M = int(input())
C = list(map(int,input().split()))

B = []
max_A = max(A)
max_C = max(C)

for i in range(abs(max_A-max_C)+1):
    count = 0
    for j in A:
        if i+j in C:
                count +=1
        if count == N:
                B.append(i)
                
B.sort()
print(" ".join(map(str,B)))