# Valid Anagram
## Link: https://leetcode.com/problems/valid-anagram/description/
def isAnagram(self, s: str, t: str) -> bool:
        # check if both strings are the same length, if NOT then they cannot be an anagram
        if len(s) != len(t):
            return False

        # create a hashmap for each string
        countS, countT = {}, {}

        # Building hashmap: iterate though using the length of either s or t (same length at this point)
        for i in range(len(s)):
            # count the occurance of character in string 's', where s[i] is the key
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True
