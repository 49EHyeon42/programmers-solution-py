
# 프로그래머스 해결책, 성공
def mySolution(s):
    answer = []
    for arr in s.lower().split(" "):
        word = []
        for idx, val in enumerate(arr):
            word.append(val.upper()) if idx%2 == 0 else word.append(val)
        answer.append(''.join(word))
    return ' '.join(answer)

# 프로그래머스 1페이지 1번 해결책, 성공
def referenceSolution1(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))

# 프로그래머스 1페이지 2번 해결책, 실패
# * "s.split()" 을 "s.split(' ')" 로 변경하면 성공 가능
def referenceSolution2(s):
    return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split()])

# 프로그래머스 1페이지 3번 해결책, 성공
def referenceSolution3(s):
    a=[]
    s=s.split(" ")
    for i in range(len(s)):
        for j in range(len(s[i])):
            if j%2==0:
                a.append(s[i][j].upper())
            else:
                a.append(s[i][j].lower())
        a.append(" ")

    c="".join(a[:-1])
    return c