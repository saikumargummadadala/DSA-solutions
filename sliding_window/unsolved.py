nums=[1,2,3,4,5]
k=2
sli=nums[:k][::-1]
ans=[]
ans.append(sli)
while k<=len(nums):
    ans+=nums[k:k*2]
    k=k*2
ans+=nums[k:]
print(ans)