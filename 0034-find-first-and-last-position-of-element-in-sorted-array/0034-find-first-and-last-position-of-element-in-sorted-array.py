class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lb():
            l,r=0,len(nums)-1
            lb=-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    lb=mid
                    r=mid-1
                elif nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            return lb
        def up():
            l,r=0,len(nums)-1
            ub=-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]<=target:
                    if nums[mid]==target:
                        ub=mid
                    l=mid+1
                else:
                    r=mid-1
            return ub
        
        return [lb(),up()]                    

             
                         


            