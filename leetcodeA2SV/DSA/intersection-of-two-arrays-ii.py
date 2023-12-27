class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        first, second = sorted(nums1), sorted(nums2)
        p, q = 0, 0
        res = []

        while p < len(nums1) and q < len(nums2):
            if first[p] < second[q]:
                p += 1

            elif first[p] > second[q]:
                q += 1
            else:
                res.append(first[p])
                p += 1
                q += 1

        return res


