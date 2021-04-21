'''
Given a 2D array A, your task is to convert all rows to columns and columns to rows.

Input:
First line contains 2 space separated integers, N - total rows, M - total columns.
Each of the next N lines will contain M space separated integers.

Output:
Print M lines each containing N space separated integers. '''


N,M = map(int,input().split())

mat = [list(map(int,input().split())) for n in range(N)]


# for row in range(M):
#     for col in range(N):
#         ansArray[row][col] = mat[col][row]

ansArray = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

for row in ansArray:
    print(" ".join(map(str,row)))