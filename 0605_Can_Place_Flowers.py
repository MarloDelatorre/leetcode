from unittest import main, TestCase

def canPlaceFlowers(flowerbed, n):
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            absent_left = i - 1 < 0 or flowerbed[i - 1] == 0
            absent_right = i + 1 >= len(flowerbed) or flowerbed[i + 1] == 0
            if absent_left and absent_right:
                flowerbed[i] = 1
                n -= 1
        if n <= 0:
            return True
    return False 

class Test(TestCase):
    def test_given_case_1(self):
        self.assertTrue(canPlaceFlowers([1, 0, 0, 0, 1], 1))

    def test_given_case_2(self):
        self.assertFalse(canPlaceFlowers([1, 0, 0, 0, 1], 2))

    def test_single_one(self):
        self.assertFalse(canPlaceFlowers([1], 1))

    def test_single_zero(self):
        self.assertTrue(canPlaceFlowers([0], 1))

if __name__ == "__main__":
    main()