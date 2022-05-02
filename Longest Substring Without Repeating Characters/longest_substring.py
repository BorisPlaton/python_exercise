class Solution:

    def __init__(self):
        self.longest_word = {
            'word': set(),
            'length': 0,
        }
        self.start_index = 0

    def lengthOfLongestSubstring(self, s: str) -> int:

        while self.start_index < len(s):
            temporary_word = {
                'word': set(),
                'length': 0,
            }

            for index, char in enumerate(s[self.start_index:]):
                if char not in temporary_word['word']:
                    temporary_word['word'].add(char)
                    temporary_word['length'] += 1
                    continue
                break

            if self.longest_word['length'] < temporary_word['length']:
                self.longest_word = temporary_word

            self.start_index += 1

        return self.longest_word['length']
