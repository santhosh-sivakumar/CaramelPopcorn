class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        out = []
        nums.sort()
        
        while (len(nums) != 0):
            out.append(nums[1])
            out.append(nums[0])
            nums = nums[2:]
        
        return out