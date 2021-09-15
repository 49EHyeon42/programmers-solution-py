import unittest

def solution(s):
    answer = []
    for arr in s.lower().split(" "):
        word = []
        for idx, val in enumerate(arr):
            word.append(val.upper()) if idx%2 == 0 else word.append(val)
        answer.append(''.join(word))
    return ' '.join(answer)


class SolutionTest(unittest.TestCase):
    def test_Method1(self):
        answer = solution("try hello world")
        self.assertEqual(answer, "TrY HeLlO WoRlD")

    # 파라미터가 대문자인 경우
    def test_Method2(self):
        answer = solution("trY hello wOrld")
        self.assertEqual(answer, "TrY HeLlO WoRlD")
        
if __name__ == '__main__':
    unittest.main()