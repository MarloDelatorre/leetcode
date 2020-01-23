from typing import List
from unittest import TestCase, main

num_to_letters = {
    "2": "abc", "3": "def", 
    "4": "ghi", "5": "jkl", "6": "mno",
    "7": "pqrs", "8": "tuv", "9": "wxyz"
}

def letterCombinations(digits: str) -> List[str]:
    if not digits:
        return []

    length = len(digits)
    combinations= []
    builder = []

    def generate(index: int):
        global num_to_letters
        nonlocal digits, length, combinations, builder
        if index >= length:
            combinations.append("".join(builder))
            return

        for letter in num_to_letters[digits[index]]:
            builder.append(letter)
            generate(index + 1)
            builder.pop()

    generate(0)
    return combinations

class Test(TestCase):
    def test_no_digits(self):
        self.assertEqual(letterCombinations(""), [])

    def test_single_digit(self):
        self.assertEqual(set(letterCombinations("2")), set(["a", "b", 'c']))

    def test_multiple_digits(self):
        self.assertEqual(
            set(letterCombinations("3659")),
            set([
                "dmjw", "dmjx", "dmjy", "dmjz", "dmkw", "dmkx", "dmky", "dmkz",
                "dmlw", "dmlx", "dmly", "dmlz", "dnjw", "dnjx", "dnjy", "dnjz",
                "dnkw", "dnkx", "dnky", "dnkz", "dnlw", "dnlx", "dnly", "dnlz",
                "dojw", "dojx", "dojy", "dojz", "dokw", "dokx", "doky", "dokz",
                "dolw", "dolx", "doly", "dolz", "emjw", "emjx", "emjy", "emjz",
                "emkw", "emkx", "emky", "emkz", "emlw", "emlx", "emly", "emlz",
                "enjw", "enjx", "enjy", "enjz", "enkw", "enkx", "enky", "enkz",
                "enlw", "enlx", "enly", "enlz", "eojw", "eojx", "eojy", "eojz",
                "eokw", "eokx", "eoky", "eokz", "eolw", "eolx", "eoly", "eolz",
                "fmjw", "fmjx", "fmjy", "fmjz", "fmkw", "fmkx", "fmky", "fmkz",
                "fmlw", "fmlx", "fmly", "fmlz", "fnjw", "fnjx", "fnjy", "fnjz",
                "fnkw", "fnkx", "fnky", "fnkz", "fnlw", "fnlx", "fnly", "fnlz",
                "fojw", "fojx", "fojy", "fojz", "fokw", "fokx", "foky", "fokz",
                "folw", "folx", "foly", "folz"
            ])
        )

if __name__ == "__main__":
    main()