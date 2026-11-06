class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        output = []

        for s in strs:
            pattern = ''.join(sorted(s))
            
            if pattern in hashMap:
                hashMap[pattern].append(s)
            else:
                hashMap[pattern] = [s]

        return list(hashMap.values())
            