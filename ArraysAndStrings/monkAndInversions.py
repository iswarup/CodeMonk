
for T in range(int(input())):
    N, K = (map(int,input().split()))
    A = list(map(int,input().split()))

    K = K % N
    for i in range(N):
        if i < K:
            print(A[N +i -K], end= " ")
        else:
            print(A[i -K], end= " ")
    
    print()
