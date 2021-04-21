
'''
The link to the problem
https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem?isFullScreen=true&utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

'''
def wrapper(f):
    def fun(l):
        # complete the function
        newl = ["+91" + " " + str(number[-10:-5]) +" " +str(number[-5:]) for number in l]
        f(newl)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)