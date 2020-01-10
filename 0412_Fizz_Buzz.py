import unittest

class Solution():
    @staticmethod
    def fizzBuzz(n):
        output = []

        for i in range(1, n + 1):
            if i % 15 == 0:
                value = "FizzBuzz" 
            elif i % 3 == 0:
                value = "Fizz"
            elif i % 5 == 0:
                value = "Buzz"
            else:
                value = str(i)
            output.append(value)

        return output
                

class Test(unittest.TestCase):
    def test_generic_case(self):
        self.assertListEqual(
            Solution.fizzBuzz(15),
            [
                "1", "2", "Fizz", "4", "Buzz", "Fizz",
                "7", "8", "Fizz", "Buzz", "11", "Fizz",
                "13", "14", "FizzBuzz"
            ]
        )

if __name__ == "__main__":
    unittest.main()