from unittest import main, TestCase

class Solution():
    @staticmethod
    def subdomainVisits(cpdomains):
        subdomain_visits = {}
        
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(' ')
            subdomains = domain.split('.')

            for i in range(len(subdomains)):
                subdomain = ".".join(subdomains[i:])
                if (visits := subdomain_visits.get(subdomain)) is None:
                    subdomain_visits[subdomain] = visits = 0
                subdomain_visits[subdomain] += int(count)

        return [f"{visits} {subdomain}" for subdomain, visits in subdomain_visits.items()]

class Test(TestCase):
    def test_given_cases(self):
        cases = [
            (
                ["9001 discuss.leetcode.com"],
                ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
            ),
            (
                [
                    "900 google.mail.com", "50 yahoo.com",
                    "1 intel.mail.com", "5 wiki.org"
                ],
                [
                    "901 mail.com","50 yahoo.com","900 google.mail.com",
                    "5 wiki.org","5 org","1 intel.mail.com","951 com"
                ]
            )
        ]

        for input, expected in cases:
            with self.subTest(input):
                self.assertEqual(
                    set(Solution.subdomainVisits(input)),
                    set(expected)
                )
                
if __name__ == '__main__':
    main()