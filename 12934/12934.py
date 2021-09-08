import unittest

def solution(n):
    sqrt = n ** (1/2)
    return ((sqrt + 1) ** 2 if sqrt%1 == 0 else -1)

class SolutionTest(unittest.TestCase):
    def test_Method1(self):
        answer = solution(121)
        self.assertEqual(answer, 144)

    def test_Method2(self):
        answer = solution(3)
        self.assertEqual(answer, -1)

if __name__ == '__main__':
    unittest.main()