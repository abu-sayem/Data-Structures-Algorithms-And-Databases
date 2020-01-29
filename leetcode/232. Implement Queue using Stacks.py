class MyQueue:

    def __init__(self):
        self.master_stack = []
        self.slave_stack = []
        

    def push(self, x: int) -> None:
        while(len(self.master_stack) is not 0):
            self.slave_stack.append(self.master_stack.pop())
        self.master_stack.append(x)
        while(len(self.slave_stack) is not 0):
            self.master_stack.append(self.slave_stack.pop())
        

    def pop(self) -> int:
        return self.master_stack.pop() 
        

    def peek(self) -> int:
        return self.master_stack[-1]
        

    def empty(self) -> bool:
        #return self.master_stack == []
        return True if self.master_stack == [] else False

          