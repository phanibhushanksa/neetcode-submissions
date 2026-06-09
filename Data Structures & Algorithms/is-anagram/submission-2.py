class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = {}
        hashmap_t = {}

        if len(s) != len(t):
            return False

        for ch in s:
            if ch in hashmap_s:
                hashmap_s[ch] += 1
            else:
                hashmap_s[ch] = 1

        for ch in t:
            if ch in hashmap_t:
                hashmap_t[ch] += 1
            else:
                hashmap_t[ch] = 1

        

        return hashmap_t == hashmap_s
