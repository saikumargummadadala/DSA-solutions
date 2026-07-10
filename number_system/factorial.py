def fact(n):
    #uses recursion to find fcatorial of a number
    if n==1:
        return 1
    return fact(n-1)*n
print(fact(int(input())))