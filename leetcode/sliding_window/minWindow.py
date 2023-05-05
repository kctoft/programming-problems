# Minimum Window Substring
# Link: https://leetcode.com/problems/minimum-window-substring/
def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = ""
        # Hashmap to store the character frequency of t
        t_freq_map = {}
        for char in t:
            if char in t_freq_map:
                t_freq_map[char] += 1
            else:
                t_freq_map[char] = 1

        # Two pointers left and right to keep track of the window
        l = 0
        r = 0
        min_len = float('inf')
        min_start = 0

        # Counter to keep track of the number of characters needed from t
        char_needed = len(t_freq_map)

        # Hashmap to keep track of the frequency of characters in the current window
        window_map = {}

        while r < len(s):
            # Add the character at right pointer to the window
            char = s[r]
            if char in t_freq_map:
                if char in window_map:
                    window_map[char] += 1
                else:
                    window_map[char] = 1

                # If the frequency of the character in the window matches the frequency in t_map, decrement char_needed
                if window_map[char] == t_freq_map[char]:
                    char_needed -= 1

            # If all the characters in t have been found, move the left pointer
            while char_needed == 0:
                # Update the minimum length and start index if a smaller window is found
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_start = l

                # Remove the character at left pointer from the window
                char = s[l]
                if char in t_freq_map:
                    window_map[char] -= 1
                    if window_map[char] < t_freq_map[char]:
                        char_needed += 1
                l += 1

            r += 1

        # If no window is found, return an empty string
        return res if min_len == float("inf") else s[min_start:min_start+min_len]
