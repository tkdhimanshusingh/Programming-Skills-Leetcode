class Solution:
    def nextGreaterElement(self, nums1, nums2):
        d, s = {}, []
        
        for n in nums2[::-1]:
            while s and n > s[-1]:
                s.pop()
            if s:
                d[n] = s[-1]
            s.append(n)
        return [d.get(num, -1) for num in nums1]