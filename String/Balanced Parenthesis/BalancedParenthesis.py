# Time Complexity - O(n)
# Space Complexity - O(n)

def main():
    expression = input()
    stack = list()

    for char in expression:
        if char == '(' or char == '{' or char == '[':
            stack.append(char)
        elif char == ')' or char == '}' or char == ']':
            if stack[-1] != '(' and char == ')':
                print('Not Balanced')
                return
            elif stack[-1] != '{' and char == '}':
                print('Not Balanced')
                return
            elif stack[-1] != '[' and char == ']':
                print('Not Balanced')
                return
            stack.pop()
    
    print('Balanced' if len(stack) == 0 else 'Not Balanced')
    


if __name__ == "__main__":
    main()
