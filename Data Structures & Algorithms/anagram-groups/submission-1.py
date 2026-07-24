class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 대표값을 넣어서 비교
        groups = {}
        for i, target in enumerate(strs):
            key = tuple(sorted(target))
            if key not in groups:
                groups[key] = [target]
            elif key in groups:
                groups[key].append(target)
        return list(groups.values())
