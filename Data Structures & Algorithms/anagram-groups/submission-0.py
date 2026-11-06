class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        output = []

        for s in strs:
            counter_s = Counter(s)
            pattern = ''
            for k in counter_s:
                pattern+= k*counter_s[k]
            
            pattern = tuple(sorted(pattern))
            if pattern in hashMap:
                hashMap[pattern].append(s)
            else:
                hashMap[pattern] = [s]

        for k in hashMap:
            output.append(hashMap[k])

        return output
            