import unittest

def solution(n):
    return ("Even" if n%2 == 0 else "Odd")

class SolutionTest(unittest.TestCase):
    def test_Method1(self):
        answer = solution(3)
        self.assertEqual(answer, "Odd")

    def test_Method2(self):
        answer = solution(4)
        self.assertEqual(answer, "Even")

if __name__ == '__main__':
    unittest.main()