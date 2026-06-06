class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prod = 1
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i!=j:
                    prod *= nums[j]
            result.append(prod)
        
        return result