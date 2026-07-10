def prime(n):
    if n<1:
        return "The given number is not a prime number"
    for i in range(2,int((n**0.5)+1)):
        if n%i==0:
            return "The given number is not a prime number"
        return "The given number is a prime"
print(prime(int(input())))
