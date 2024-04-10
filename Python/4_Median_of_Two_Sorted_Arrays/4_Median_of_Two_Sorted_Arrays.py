class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()

        length = len(nums) - 1
        center = length / 2

        if(int(center) == center):
            return nums[int(center)]
        else:
            return (nums[int(center)] + nums[int(center) + 1]) / 2