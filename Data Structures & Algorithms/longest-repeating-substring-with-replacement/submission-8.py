class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # so the most important part is how to get the counts and find the 
        # first XYYX what should we do after I faced X
        # add to the dictionary and count 
        # two pointers : left and right 
        # we go through the using right pointers to expand the sliding window
        # we go through the left when we try to shrink the sliding window
        
        #necessary variables
        d = {0:0}
        left = 0
        right = 0
        high_score = 0
        #use while until the right gets to len(s)
        while right != len(s):
            d[s[right]] = d.get(s[right],0) + 1
            if max(d.values()) + k < right - left + 1: # the majority of alphabet is less than the sliding window
                d[s[left]] = d.get(s[left],0) - 1
                left += 1
            high_score = max(right - left + 1, high_score)
            # how to get the max value in the dictionary?
            # using sort?
            right += 1
        return high_score


        

        