

def isValid(s:str)->bool:
    pair = {')':'(', '}':'{', ']':'['}
    stack = []
    for c in s:
        if c in '([{':
            stack.append(c)
        elif stack and stack[-1] == pair[c]:
            stack.pop()
        else:
            return False
    if stack:
        return False
    return True

if __name__ == "__main__":
    print(isValid("([]){()}"))
    print(isValid("([]{)()}"))
