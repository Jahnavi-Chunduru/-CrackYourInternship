class Solution:     
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            a = tuple(sorted(s))
            if a in anagrams:
                anagrams[a].append(s)
            else:
                anagrams[a] = [s]
        return anagrams.values()
