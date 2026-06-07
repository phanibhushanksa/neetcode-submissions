class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_map = {}

        l = 0

        max_length = 0


        for r in range(len(s)):

            char = s[r]

            if char in char_map:

                # move the l such that the last pointer of existing char is crossed

                l = max(l, char_map[char]+1)

            # update the pointer of existing character to the latest one
            char_map[char] = r
            
            max_length = max(max_length, r-l+1)

        return max_length