# Review the following link for the question prompt: https://leetcode.com/problems/median-of-two-sorted-arrays/

# O(log N) time | O(1) space
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalLen = len(nums1) + len(nums2)
        m0, m1 = self.findMedianSortedArraysHelper(totalLen, nums1, nums2) 
        
        if totalLen % 2 == 0:
            return (m0 + m1) / 2.0
        else:
            return m1
    
    def findMedianSortedArraysHelper(self, totalLen, nums1, nums2):
        medianIdx = int(totalLen / 2) + 1
        
        nums1Idx = 0
        nums2Idx = 0
        counter = 0
        m0 = 0
        m1 = 0
        nums1.append(float('inf'))
        nums2.append(float('inf'))
        
        while nums1Idx < len(nums1) or nums2Idx < len(nums2):
            if counter == medianIdx:
                break
            
            if nums1[nums1Idx] < nums2[nums2Idx]:
                m0 = m1
                m1 = nums1[nums1Idx]
                nums1Idx += 1
            else:
                m0 = m1
                m1 = nums2[nums2Idx]
                nums2Idx += 1
            counter += 1
        
        return m0,m1