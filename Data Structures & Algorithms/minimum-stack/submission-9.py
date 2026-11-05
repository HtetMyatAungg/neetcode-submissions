class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min:
            if self.min[-1] > val:
                self.min.append(val)
            else:
                val = self.min[-1]
                self.min.append(val)
        else:
            self.min.append(val)

    def pop(self) -> None:
        self.min.pop()
        self.stack.pop() 
        

    def top(self) -> int:
        length = len(self.stack)
        return self.stack[length - 1]

    def getMin(self) -> int:
        return self.min[-1]
