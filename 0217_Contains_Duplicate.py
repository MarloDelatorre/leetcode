from unittest import main, TestCase

def containsDuplicate(nums):
    return len(nums) > len(set(nums))

class Test(TestCase):
    def test_given_case_1(self):
        self.assertTrue(containsDuplicate([1, 2, 3, 1]))
    
    def test_given_case_2(self):
        self.assertFalse(containsDuplicate([1, 2, 3, 4]))
    
    def test_given_case_3(self):
        self.assertTrue(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

    def test_empty_case(self):
        self.assertFalse(containsDuplicate([]))

if __name__ == "__main__":
    main()