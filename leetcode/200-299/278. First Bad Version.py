# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        r = n
        l = 0
        while l <= r:
            mid = l + (r-l)//2
            if isBadVersion(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
