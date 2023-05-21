#  Guess Number Higher or Lower
## Link: https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):
def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # I pick a number from 1 to n
        l, r = 1, n

        while True:
            m = (l+r) // 2
            res = guess(m)

            # -1: Your guess is higher than the number I picked (i.e. num > pick)
            if res > 0:
                l = m + 1
            # 1: Your guess is lower than the number I picked (i.e. num < pick)
            elif res < 0:
                r = m - 1
            # 0: your guess is equal to the number I picked (i.e. num == pick)
            else:
                return m
