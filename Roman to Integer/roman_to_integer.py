from collections import namedtuple


class Solution:
    Num = namedtuple('Num', 'roman integer')

    nums = {
        "I": Num(None, 1),
        "V": Num('I', 5),
        "X": Num('I', 10),
        "L": Num('X', 50),
        "C": Num('X', 100),
        "D": Num('C', 500),
        "M": Num('C', 1000),
    }

    def __init__(self):
        self.roman_stack = []
        self.value = 0

    def romanToInt(self, s: str) -> int:

        for roman in s:
            self._analyze_roman(roman)
        return self.value

    def _analyze_roman(self, roman):

        if not self.roman_stack:
            self.value += self.nums[roman].integer
        else:
            if self.roman_stack[-1] == self.nums[roman].roman:
                self.value += self.nums[roman].integer - 2*self.nums[self.roman_stack[-1]].integer
            else:
                self.value += self.nums[roman].integer

        self.roman_stack.append(roman)
