class Solution(object):
    def twoSum(self, nums, target):
        li=[]
        for index,item in enumerate(nums):
            li.append((item,index))
        li.sort()
        x,y=0,len(nums)-1
        while x<y:
            if li[x][0]+li[y][0]>target:
                y-=1
            elif li[x][0]+li[y][0]<target:
                x+=1
            else:
                return(li[x][1],li[y][1])
nums=list(map(int,input().split(",")))
target=int(input())
print(Solution().twoSum(nums,target))           