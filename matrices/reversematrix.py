class Solution(object):
    def reverseGrid(self, grid, k):
        ans=[]
        for i in grid:
            ans.append(i[::-1])
        return ans[::-1]
        