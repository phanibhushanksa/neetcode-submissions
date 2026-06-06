class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            num = nums[i]
            l = i+1
            r = len(nums)-1
            while l<r:
                threeSum = nums[l]+nums[r]+num
                if threeSum >0:
                    r-=1
                    
                elif threeSum <0:
                    l+=1
                      
                else:
                    result.append([num,nums[l],nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    r-=1
                    l+=1
        return result
