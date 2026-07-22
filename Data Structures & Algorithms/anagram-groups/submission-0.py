class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            # Count the frequency of each letter (a-z)
            count = [0] * 26

            for ch in word:
                count[ord(ch) - ord('a')] += 1

            # Lists can't be dictionary keys, so convert to tuple
            groups[tuple(count)].append(word)

        return list(groups.values())
        