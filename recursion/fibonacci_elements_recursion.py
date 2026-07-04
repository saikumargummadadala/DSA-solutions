def fib(n,a=0,b=1):
    if n==1:
        return a
    return fib(n-1,b,a+b)
print(fib(int(input("input the specific position for calling out fibonacci series element:"))))
#prints the specific positioned element in the fibonnaci series
#used for purely entitle recursion usage
#take the numericals not the indexes indetail start from 1 (natural numbers)