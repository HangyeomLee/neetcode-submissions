class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # try to count alphabet of s1
        # try to use the sliding window until the dictionary gets empty
        # pass so impossible so why don't we make two dictionary and another dictionary
        d1 = {}
        d2 = {}
        for _ in s1:
            d1[_] = d1.get(_,0) + 1 # done
        print(d1)
        left = 0
        right = 0
        while right != len(s2):
            if right - left + 1 > len(s1):
                if d2[s2[left]] <= 1:
                    del d2[s2[left]]
                else:
                    d2[s2[left]] = d2.get(s2[left],0) - 1
                left += 1
            d2[s2[right]] = d2.get(s2[right],0) + 1
            right += 1
            print(d2)
            if d1 == d2:
                return True
        return False

