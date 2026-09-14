class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []
        seen = set()
        highscore = 0

        for alphabet in s:
            if alphabet in seen:
                highscore = max(len(window),highscore)
                while window[0] != alphabet:
                    seen.remove(window[0])
                    del window[0]
                del window[0]
                window.append(alphabet)
            else:
                seen.add(alphabet)
                window.append(alphabet)
        highscore = max(len(window),highscore)
        
        
                
        return highscore

    # short