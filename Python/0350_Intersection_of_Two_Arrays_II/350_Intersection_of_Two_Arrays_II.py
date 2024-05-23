class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        OUT = []

        nums1.sort()
        nums2.sort()
        
        if ( len(nums1) < len(nums2) ) or ( len(nums1) == len(nums2) ):
            for i in range( len(nums1) ):
                if nums1[i] in nums2:
                    OUT.append( nums1[i] )
                    print( '1', nums1[i], sep='\t')
                    nums2.remove( nums1[i] )
        else:
            for i in range( len(nums2) ):
                if nums2[i] in nums1:
                    OUT.append( nums2[i] )
                    print( '2', nums2[i], sep='\t')
                    nums1.remove( nums2[i] )
        
        return OUT