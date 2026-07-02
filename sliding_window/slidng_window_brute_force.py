arr=input()
#prints out every substring in it
n=len(arr)
ans=[]
for i in range(n):
    for j in range(i,n):
        ark=[]
        for k in range (i,j+1):
            ark.append(arr[k])
        ans.append(ark)
print(ans)        