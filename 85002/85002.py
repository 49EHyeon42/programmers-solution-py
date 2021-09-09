import unittest

def solution(weights, head2head):
    answer = []
    for i in range(len(head2head)):
        bouts = (len(head2head) - head2head[i].count('N'))
        rate = 0 if bouts == 0 else head2head[i].count('W') / bouts
        
        heavy = 0
        for j in range(len(weights)):    
            if i != j and head2head[i][j] == 'W' and weights[i] < weights[j] : heavy += 1
        
        answer.append([i+1, weights[i], rate, heavy])

    answer = sorted(answer, key = lambda x: (x[2], x[3], x[1], -x[0]), reverse=True)
    
    return [boxer[0] for boxer in answer]

class SolutionTest(unittest.TestCase):
    def test_Method1(self):
        weights = [50,82,75,120]
        head2head = ["NLWL","WNLL","LWNW","WWLN"]
        result = [3,4,1,2]

        self.assertEqual(solution(weights, head2head), result)

    def test_Method2(self):
        weights = [145,92,86]
        head2head = ["NLW","WNL","LWN"]
        result = [2,3,1]

        self.assertEqual(solution(weights, head2head), result)

    def test_Method3(self):
        weights = [60,70,60]
        head2head = ["NNN","NNN","NNN"]
        result = [2,1,3]

        self.assertEqual(solution(weights, head2head), result)
        
if __name__ == '__main__':
    unittest.main()