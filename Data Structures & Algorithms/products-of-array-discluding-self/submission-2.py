class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = []
        pre = 1
        post = 1

        for n in nums:
            prefix.append(pre)
            pre *= n
        
        for n in range(len(nums) - 1,-1,-1):
            prefix[n] *= post
            post *= nums[n]
        
        return prefix