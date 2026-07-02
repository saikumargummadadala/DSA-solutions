arr=list(map(int,input().split(",")))
arr.sort()
#arr=[1,2,3,4,5,6]
target=int(input())
#target=6
x=0
y=len(arr)-1

while x<y:
    if arr[x]+arr[y]==target:
        break
    elif arr[x]+arr[y]<target:
        x+=1
    else:
        y-=1
print(arr[x],arr[y])