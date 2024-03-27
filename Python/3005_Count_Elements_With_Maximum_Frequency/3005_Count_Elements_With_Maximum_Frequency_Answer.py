class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        a = set(nums)

        c = [nums.count(i) for i in a]
        c.sort()

        ele = c[-1]
        count = 0

        for i in c:
            if i == ele:
                count += i
        
        return count