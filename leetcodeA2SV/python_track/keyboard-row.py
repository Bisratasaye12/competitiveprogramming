class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        row1 ="qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"

        rows = defaultdict(list)
        for word in words:
            dummy_word = ''
            for letter in word.lower():
                if letter in row1:
                    dummy_word += "1"
                elif letter in row2:
                    dummy_word += "2"
                else:
                    dummy_word += "3"

            for identifier in dummy_word:
                if identifier != dummy_word[0]:
                    break
            else:
                rows[dummy_word[0]].append(word)

        res = []
        for i in rows:
            if rows[i]:
                res += rows[i]


        return res

