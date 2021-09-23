# def solution(arr):
#     answer = [arr[0]]
#     for i in range(len(arr)-1):
#         if arr[i] != arr[i+1]:
#             answer.append(arr[i+1])
#     return answer

def solution(arr):
    answer = [arr[0]]
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]: answer.append(arr[i+1])
    return answer

# 한줄 만들기 실패
# def solution(arr):
#     return [arr[i+1] for i in range(len(arr)-1) if arr[i] != arr[i+1]].insert(0, arr[0])


a = [1,1,3,3,0,1,1] 
b = [4,4,4,3,3]
print(solution(a))