class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}
        for i, key in enumerate(s):
            seen[key] = seen.get(key, 0) + 1
        for i, key in enumerate(t):
            if key in seen:
                if seen[key] <= 0:
                    return False
                seen[key] = seen.get(key) - 1
            else:
                return False
        return True