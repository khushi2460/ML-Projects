class Solution:
    def getSecondLargest(self, arr):
        c=sorted(set(arr))
        if len(c)<=1:
            return -1
        else:
            return c[-2]
        
        # Code Here