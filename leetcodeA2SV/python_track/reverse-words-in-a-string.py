class Solution:
    def reverseWords(self, s: str) -> str:
        
        def not_space(string):
            return not string.isspace()

        words = list(filter(not_space, s.strip().split()))

        return " ".join(words[::-1])