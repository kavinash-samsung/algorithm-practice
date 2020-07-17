def checkbalanced(string):
    stack = []
    for i in range(len(string)):
        if string[i] == '[' or string[i] == '{' or string[i] == '(':
            stack.append(string[i])
        else: 
            if stack == []:
                return False
            if string[i] == '}' and stack[-1] == '{':
                stack.pop()
            elif string[i] == ']' and stack[-1] == '[':
                stack.pop()
            elif string[i] == ')' and stack[-1] == '(':
                stack.pop()
            else:
                return False
    if stack is None:
        return True
    return False
print(checkbalanced('((())))'))