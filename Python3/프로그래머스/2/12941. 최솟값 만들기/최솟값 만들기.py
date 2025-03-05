def solution(A, B):
    a = sorted(A)  # 오름차순 정렬
    b = sorted(B, reverse=True)  # 내림차순 정렬
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]  # 같은 인덱스의 요소를 곱함
    return answer