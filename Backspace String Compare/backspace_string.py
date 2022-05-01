class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.get_chars_list(s) == self.get_chars_list(t)

    @staticmethod
    def get_chars_list(string):
        char_list = []
        for char in string:
            if char == '#' and char_list:
                char_list.pop()
            elif char != '#':
                char_list.append(char)
        return char_list
