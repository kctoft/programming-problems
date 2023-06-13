# First Bad Version
## Link: https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    l, r = 1, n

    while l <= r:
        m = (l + r) // 2
        res = isBadVersion(m)

        if res:
            r = m - 1
        else:
            l = m + 1

    return l
