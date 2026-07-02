class Solution(object):
    def findMaxAverage(self, nums, k):
#also a leetcode problem-643
        x=[]
        avg=(sum(nums[:k]))
        x.append(avg)
        for i in range(k,len(nums)):
            avg=(avg+nums[i]-nums[i-k])
            x.append(avg)
        result=max(x)
        return float(result)/k
nums=list(map(int,input().split(",")))
#nums=[1,12,-5,-6,50,3]
k=int(input())
#k=4
print(Solution().findMaxAverage(nums,k))