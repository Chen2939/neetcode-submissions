class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for s in strs:
            k = [0 for _ in range(26)]
            for c in s:
                k[ord(c) - ord('a')] += 1
            hmap[tuple(k)].append(s)
        return list(hmap.values())