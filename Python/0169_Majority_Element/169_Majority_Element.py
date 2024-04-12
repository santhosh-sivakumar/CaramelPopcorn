class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elem = list(set(nums))
        
        n = len(nums)

        for i in elem:
            if nums.count(i) > (n/2):
                return i