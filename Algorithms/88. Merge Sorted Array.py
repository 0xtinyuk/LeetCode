class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m-1,-1,-1):
            nums1[i+n]=nums1[i]
        p1 = n
        p2 = 0
        for i in range(n+m):
            if p1-n>=m:
                nums1[i]=nums2[p2]
                p2+=1
                continue
            if p2>=n:
                nums1[i]=nums1[p1]
                p1+=1
                continue
            if nums1[p1]<nums2[p2]:
                nums1[i]=nums1[p1]
                p1+=1
            else:
                nums1[i]=nums2[p2]
                p2+=1
        return
        