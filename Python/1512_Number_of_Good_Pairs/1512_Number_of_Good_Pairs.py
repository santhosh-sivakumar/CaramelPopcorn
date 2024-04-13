class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        length = len(nums)
        OUT = []

        for i in range(length):
            for j in range(i):
                if(nums[i] == nums[j]):
                    OUT.append((i, j))
        
        return len(OUT)