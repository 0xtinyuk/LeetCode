class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            t = nums1
            nums1 = nums2
            nums2 = t

        m = len(nums1)
        n = len(nums2)
        l = 0
        r = m
        while l <= r:
            i = (l+r)//2
            j = (m+n+1)//2-i
            if ((i == 0) or (j == n) or (nums1[i-1] <= nums2[j])) and ((j == 0) or (i == m) or (nums2[j-1] <= nums1[i])):
                if (i == 0):
                    ml = nums2[j-1]
                elif (j == 0):
                    ml = nums1[i-1]
                else:
                    ml = max(nums1[i-1], nums2[j-1])
                if (m+n) % 2 == 1:
                    return ml
                if (i == m):
                    mr = nums2[j]
                elif (j == n):
                    mr = nums1[i]
                else:
                    mr = min(nums1[i], nums2[j])
                return (ml+mr)/2
            if ((i > 0) and (nums1[i-1] > nums2[j])):
                r = i-1
            else:
                l = i+1
