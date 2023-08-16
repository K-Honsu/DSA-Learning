import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s)
        print(cleaned_s)
        lower = cleaned_s.lower()
        print(lower)
        low = ''.join(reversed(lower))
        print(low)
        sort = sorted(lower)
        if sort == reversed(sort):
            return True
        return False
    
ex = Solution()
ex.isPalindrome("A man, a plan, a canal: Panama")

def find_smallest_int(arr):
    return min(arr)

print(find_smallest_int([1,2,3,4,-1]))