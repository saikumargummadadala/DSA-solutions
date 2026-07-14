class Solution:
    def maxofasubarray(self,nums,k):
        sli=nums[:k]
        x=[]
        x.append(max(sli))
        for i in range(k,len(nums)):
            sli.append(nums[i])
            sli.remove(nums[i-k])
            x.append(max(sli))
        return x
nums=list(map(int,input().split(",")))#the list of elements
k=int(input())#the size of the window or the length of a individual subarray
print(Solution().maxofasubarray(nums,k))