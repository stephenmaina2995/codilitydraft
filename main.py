# def solution(s):
#     print(solution())
def solution(S):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    for char in S:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack:
                return 0
            if stack[-1] == brackets[char]:
                stack.pop()
            else:
                return 0

    return 1 if not stack else 0

# Test cases
print(solution("{[()()]}"))  # Output: 1
print(solution("([)()]"))    # Output: 0
