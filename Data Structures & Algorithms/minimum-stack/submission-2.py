class MinStack:

    def __init__(self):
        self.st = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.st.append(val)

        if self.minStack:
            self.minStack.append(min(val, self.minStack[-1]))
        else:
            self.minStack.append(val)
            
    def pop(self) -> None:
        self.st.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        x = self.st[-1]
        return x
        

    def getMin(self) -> int:
        x = self.minStack[-1]
        return x

        
