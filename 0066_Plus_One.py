from unittest import main, TestCase

def plusOne(digits):
    carry = 1
    for i in range(len(digits)-1, -1, -1):
        digits[i] += carry
        if digits[i] > 9:
            digits[i] = 0
            carry = 1 
        else:
            carry = 0

    if carry:
        digits.insert(0, 1)

    return digits

class Test(TestCase):
    def test_given_case_1(self):
        self.assertListEqual(plusOne([1, 2, 3]), [1, 2, 4])

    def test_given_case_2(self):
        self.assertListEqual(plusOne([4, 3, 2, 1]), [4, 3, 2, 2])

    def test_carry(self):
        self.assertListEqual(plusOne([9]), [1, 0])

    def test_carry_propogate(self):
        self.assertListEqual(plusOne([9, 9, 9, 9]), [1, 0, 0, 0, 0])

if __name__ == "__main__":
    main()