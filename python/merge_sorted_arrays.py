class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """for i in range(len(nums1)):
            if i>m:
                del nums1[i]"""
        del nums1[m:]
        
            

        for i in nums2:
            nums1.append(i)
        nums1.sort()

        