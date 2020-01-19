from unittest import TestCase, main

def countPrimes(n: int) -> int:
    if n <= 1:
        return 0
    sieve = list(range(2, n))
    sift_index = 0

    while sift_index < len(sieve):
        for i, num in enumerate(sieve):
            sift_num = sieve[sift_index]
            if num and num != sift_num and num % sift_num == 0:
                sieve[i] = None

        sift_index += 1
        while sift_index < len(sieve) and not sieve[sift_index]:
            sift_index += 1

    return len([num for num in sieve if num]) 

class Test(TestCase):
    def test_given_case(self):
        self.assertEqual(countPrimes(10), 4)

if __name__ == "__main__":
    countPrimes(5) 
    main()