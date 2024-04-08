class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1, n2 = set(nums1), set(nums2)

        OUT = n1.intersection(n2)

        return list(OUT)