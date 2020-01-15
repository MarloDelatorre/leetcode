from unittest import TestCase, main

def defangIPaddr(address: str) -> str:
    return "[.]".join(address.split("."))

class Test(TestCase):
    def test_given_case_1(self):
        self.assertEqual(defangIPaddr("1.1.1.1"), "1[.]1[.]1[.]1")

    def test_given_case_2(self):
        self.assertEqual(defangIPaddr("255.100.50.0"), "255[.]100[.]50[.]0")

if __name__ == "__main__":
    main()