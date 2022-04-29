class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if not ransomNote:
            return True

        char = ransomNote[0]
        index_char = magazine.find(char)
        if index_char == -1:
            return False

        return self.canConstruct(ransomNote[1:], magazine[:index_char] + magazine[index_char + 1:])
