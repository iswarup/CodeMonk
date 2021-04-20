'''
Problem

You have N rectangles. A rectangle is golden if the ratio of its sides is in between 
1.6,1.7 both inclusive. Your task is to find the number of golden rectangles.

Input format
	
	First line: Integer N denoting the number of rectangles
	
	Each of the N following lines: Two integers W, H denoting the width and height of a rectangle

Output format

    Print the answer in a single line.

Constraints
	1 <= N <= 10**5
	1 <= W,H <= 10**9

'''

def isGolden(w,h):
    ans = max(w,h)/min(w,h)
    if 1.6 <= ans <= 1.7:
        return True
    return False

count = 0

N = int(input())
for n in range(N):
    W,H = map(int,input().split())
    if isGolden(W,H):
        count +=1

print(count)