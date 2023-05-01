# # use sliding window techinque for finding an anagram of s1 & s2
# def checkInclusion(self, s1, s2):
#         """
#         :type s1: str
#         :type s2: str
#         :rtype: bool
#         """
#         # impossible edge case
#         if len(s1) > len(s2):
#             return False

#         s1_count = [0] * 26
#         s2_count = [0] * 26

#         # set up the "hashmap"
#         for i in range(len(s1)):
#             s1_count[ord(s1[i]) - ord("a")] += 1
#             s2_count[ord(s2[i]) - ord("a")] += 1

#         # check if there is a match s2 == s1 in the maps
#         matches = 0
#         for i in range(26):
#             matches += 1 if s1_count[i] == s2_count[i] else 0

#         # sliding window
#         l = 0
#         for r in range(len(s1), len(s2)):
#             if matches == 26:
#                 return True

#             index = ord(s2[r]) - ord("a")
#             s2_count[index] += 1
#             if s1_count[index] == s2_count[index]:
#                 matches += 1
#             elif s1_count[index] + 1 == s2_count[index]:
#                 matches -= 1

#             index = ord(s2[l]) - ord("a")
#             s2_count[index] -= 1
#             if s1_count[index] == s2_count[index]:
#                 matches += 1
#             elif s1_count[index] - 1 == s2_count[index]:
#                 matches -= 1
#             l += 1

#         return matches == 26

def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # edge case: impossible situation
        if len(s1) > len(s2):
            return False

        # setting up size of maps
        s1_count = [0] * 26
        s2_count = [0] * 26
        k = len(s1)

        # populating maps
        for i in range(k):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        # check if substring permutation match
        if self.matches(s1_count, s2_count):
            return True

        # sliding window
        for i in range(k, len(s2)):
            s2_count[ord(s2[i]) - ord('a')] += 1
            s2_count[ord(s2[i-k]) - ord('a')] -= 1
            if self.matches(s1_count, s2_count):
                return True
        return self.matches(s1_count, s2_count)

    # check if s1 map == s2 map
    def matches(self, s1_count, s2_count):
        for i in range(26):
            if s1_count[i] != s2_count[i]:
                return False
        return True
