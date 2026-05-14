class myStack:
    def __init__(self, n):
        # Initialize stack with maximum size n
        self.stack = []
        self.max_size = n

    def isEmpty(self):
        # Check if stack is empty
        return len(self.stack) == 0

    def isFull(self):
        # Check if stack is full
        return len(self.stack) == self.max_size

    def push(self, x):
        # Insert x at the top of the stack
        if self.isFull():
            return -1  
        else:
            self.stack.append(x)
            return True

    def pop(self):
        # Removes an element from the top of the stack
        if self.isEmpty():
            return -1   
        else:
            return self.stack.pop()

    def peek(self):
        # Returns the top element of the stack
        if self.isEmpty():
            return -1   
        else:
            return self.stack[-1]
