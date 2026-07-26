class Solution:
    def isPalindrome(self, s: str) -> bool:
        #first, make a clean list which ignores non alphanumeric character.
        #compare s[i] and s[len(s)-i]
        # or make left and right pointer to compare is palindrome or nah
        # the function we are using would be just isalnum
        lp = 0
        rp = len(s) - 1
        while lp <= rp:
            if s[lp].isalnum() == False:
                lp = lp + 1
                continue
            elif s[rp].isalnum() == False:
                rp = rp - 1
                continue
            elif s[lp].lower() != s[rp].lower():
                return False
            else:
                lp = lp + 1
                rp = rp - 1   
        return True
                    
