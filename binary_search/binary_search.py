class Solution:
    #leetcode problem 
    def search(self, nums, target):
        middle=len(nums)//2
        if target==nums[middle]:
            return middle
        elif target>nums[middle]:
            for i in range(middle,len(nums)):
                if nums[i]==target:
                    return i
            return -1
        elif target<nums[middle]:
            for i in range(0,middle):
                if nums[i]==target:
                    return i 
            return -1
nums=list(map(int,input().split(",")))
target=int(input())
print(Solution().search(nums,target))
