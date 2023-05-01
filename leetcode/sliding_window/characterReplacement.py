def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = 0 # largest window size to return
        l = 0 # LHS pointer
        max_f = 0 # freq letter
        freq = {} # freq dictorionary

        for r in range(len(s)):
            # if a char is NOT in the freq dict then insert the value of 1 (get() returns 0, then add 1)
            # if a char is in freq dict then add +1
            freq[s[r]] = 1 + freq.get(s[r], 0)
            max_f = max(max_f, freq[s[r]])

            # we want the MAX of seen values with limitation of k
            # get length of current substring, then minus max_freq. Check is this is <= k
            if (r - l + 1) - max_f > k:
                # if we have max k letters, we need to dec freq and move LHS ptr by 1
                freq[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)  # record new max len

        return res

## Alternative approach
# def characterReplacement(self, s, k):
#         """
#         :type s: str
#         :type k: int
#         :rtype: int
#         """
#         l = 0
#         max_len = 0
#         freq = {}

#         for r in range(len(s)):
#             # if a char is NOT in the freq dict then insert the value of 1 (get() returns 0, then add 1)
#             # if a char is in freq dict then add +1
#             freq[s[r]] = freq.get(s[r], 0) + 1

#             # we want the MAX of seen values with limitation of k
#             # get length of current substring, then minus max_freq. Check is this is <= k
#             cur_len = r - l + 1

#             if cur_len - max(freq.values()) <= k:
#                 max_len = max(max_len, cur_len) # record new max len
#             else:
#                 freq[s[l]] -= 1 # if we have max k letters, we need to dec freq and move LHS ptr by 1
#                 l += 1

#         return max_len
