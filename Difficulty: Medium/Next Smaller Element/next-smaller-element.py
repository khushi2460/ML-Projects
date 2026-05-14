class Solution:
    def nextSmallerEle(self, arr):
        n = len(arr)
        ans = [-1] * n
        stack = []  
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                ans[i] = arr[stack[-1]]
            stack.append(i)
        
        return ans

