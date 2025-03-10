def solution(s):
    stack = []
    
    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:  # 스택이 비어있으면 짝이 안 맞음
                return False
            stack.pop()  # 짝을 이루면 열린 괄호 하나 꺼냄
    
    return len(stack) == 0  # 빈값이어야 짝이 모두 맞음