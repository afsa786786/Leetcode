class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: Basic length check
        if len(s) != len(t):
            return False
        
        # Step 2: Count frequencies
        count_s = {}
        count_t = {}
        
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
            
        # Step 3: Compare the two dictionaries
        return count_s == count_t