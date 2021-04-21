
'''
Problem

A love Guru determines "whether a guy's proposal is going to be accepted by his crush or not" just by doing some mysterious calculation on their names, but it takes too much time for him. So, he hired you as a programmer and now your task is to write a program that helps the Guru.

He reveals his mystery with you and that is:

If the guy's name is a subsequence of his crush's name, then she is going to accept him, otherwise she will reject him.

Input

    First line contains T, the number of test cases.
    Next T lines contain two strings S1 and S2 which are the guy's name and his crush's name respectively.

Output

    For each test case, according to Guru's mystery, if the crush is going to accept the guy then print "Love you too", otherwise print "We are only friends".

Constraints:

    strings contain only lowercase Latin letters. 

    1 <= T <= 60
    1 <= len(S1),len(S2) <= 100000
'''

def SubSeq(s1,s2):
    i,j = (0,0)
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i+=1
        j+=1
    return i==len(s1)

for T in range(int(input())):

    S1,S2 = (input().split())

    if SubSeq(S1,S2):
        print("Love you too")
    else:
        print('We are only friends')