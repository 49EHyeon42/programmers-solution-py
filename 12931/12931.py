import unittest

def solution(n):
    answer = 0
    while n>0:
        answer += n%10
        n //= 10
    return answer

class SolutionTest(unittest.TestCase):
    def test_Method1(self):
        answer = solution(123)
        self.assertEqual(answer, 6)

    def test_Method2(self):
        answer = solution(987)
        self.assertEqual(answer, 24)

if __name__ == '__main__':
    unittest.main()