class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1 = re.sub(r'[^a-zA-Z0-9]', '', s)
        str2 = str1.lower()
        left = 0
        right = len (str2) - 1
        while left < right:
            if str2[left] != str2[right]:
                return False
            left += 1
            right -= 1
        return True