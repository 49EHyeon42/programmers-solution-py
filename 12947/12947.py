import unittest

def solution(x):
    sum = 0 
    num = x
    while num>0:
        sum += num%10
        num //= 10
    return x%sum == 0

# reference 1
# def solution(n):
#     # n은 하샤드 수 인가요?
#     return n % sum([int(c) for c in str(n)]) == 0

class SolutionTest(unittest.TestCase):
    def test_Method1(self):
        answer = solution(10)
        self.assertEqual(answer, True)

    def test_Method2(self):
        answer = solution(12)
        self.assertEqual(answer, True)

    def test_Method3(self):
        answer = solution(11)
        self.assertEqual(answer, False)

    def test_Method4(self):
        answer = solution(13)
        self.assertEqual(answer, False)

if __name__ == '__main__':
    unittest.main()