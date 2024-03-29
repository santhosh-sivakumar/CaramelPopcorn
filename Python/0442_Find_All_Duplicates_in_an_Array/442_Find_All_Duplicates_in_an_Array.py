class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        a = Counter(nums)
        count = [i for i, j in a.items() if j==2]
        return count