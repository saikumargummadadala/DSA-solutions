def is_prime(n):
    if n<1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
ans=[]
for j in range(1,n+1):
    if is_prime(j) is True:
        ans.append(j)
print(ans)