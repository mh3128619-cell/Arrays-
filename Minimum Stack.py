class MinStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, val):
        self.main_stack.append(val)
        
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        self.main_stack.pop()
        self.min_stack.pop()

    def getMin(self):
        return self.min_stack[-1]

obj = MinStack()
obj.push(5)
obj.push(3)
obj.push(7)
obj.push(2)

print(f"Current minimum: {obj.getMin()}")
obj.pop()
print(f"After popping 2, the minimum is: {obj.getMin()}")
