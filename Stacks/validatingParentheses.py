# The problem is to calculate the number of new parenthesis to be added to balance the string.

s = input()

stack1 = []

stack2 = []

for i in s:

        if i == "(":

           stack1.append(i)

        elif i == ")":

           if len(stack1) == 0:

                stack2.append(i)

           else:

                stack1.pop()

print(len(stack1)+len(stack2))
