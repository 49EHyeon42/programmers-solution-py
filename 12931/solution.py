def mySolution(n):
    answer = 0
    while n>0:
        answer += n%10
        n //= 10
    return answer

def Solution1(number):
    if number < 10:
        return number
    return (number % 10) + Solution1(number // 10)

def Solution2(number):
    return sum([int(i) for i in str(number)])

def Solution3(number):
    return sum(map(int,str(number)))