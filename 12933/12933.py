import unittest

def solution(n):
    return int(''.join(sorted(str(n), reverse=True)))

class SolutionTest(unittest.TestCase):
    def test_Method1(self):
        answer = solution(118372)
        self.assertEqual(answer, 873211)

if __name__ == '__main__':
    unittest.main()