class Solution:
    def reverseWords(self, s: str) -> str:
        splited = s.split() # split the sentence in to words
        left = 0
        right = len(splited) - 1
        while left < right:
            splited[left], splited[right] = splited[right], splited[left] # reverse their order in the array/list
            left += 1
            right -= 1
        reverse = " ".join(splited) #then join the reversed words in to one sentence
        return reverse