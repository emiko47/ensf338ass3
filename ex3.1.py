import sys

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

def evaluate_expression(expr):
    stack = Stack()

    # Split the expression into tokens
    tokens = expr.split()

    # Process each token
    for token in reversed(tokens):
        if token == '(':
            # Do nothing, '(' is just a separator
            pass
        elif token in ['+', '-', '*', '/']:
            # Pop the last two numbers off the stack
            num1 = stack.pop()
            num2 = stack.pop()

            # Perform the operation and push the result back onto the stack
            if token == '+':
                stack.push(num1 + num2)
            elif token == '-':
                stack.push(num1 - num2)
            elif token == '*':
                stack.push(num1 * num2)
            elif token == '/':
                stack.push(num1 // num2)  # Use integer division instead of float division
        elif token == ')':
            # Do nothing, ')' is just a separator
            pass
        else:
            # Convert the token to a number and push it onto the stack
            stack.push(int(token))

    # The result is the last item on the stack
    return stack.pop()

# Get the expression from the command line arguments
expr = sys.argv[1]

# Evaluate the expression and print the result
result = evaluate_expression(expr)
print(result)
