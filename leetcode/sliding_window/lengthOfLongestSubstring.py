# Longest Substring Without Repeating Characters
# link: Longest Substring Without Repeating Characters
def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Create pointers for each end of the sliding window
        l = 0
        max_len = 0

        # Create a hashmap --> key/value : character/index
        seen = {}

        # Iterate over the all elements in the string s
        for r in range(len(s)):
          # check if the element is already in the hashmap
          if s[r] in seen:
            # if it is, update the LHS pointer by moving it left by 1
            l = max(l, seen[s[r]] + 1)

          # add the new element to the hashmap
          seen[s[r]] = r
          # increment the window size by one
          max_len = max(max_len, r - l + 1)

        # return the maximum length of the given substring
        return max_len
