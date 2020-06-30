class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.cu_index = 0
        

    def visit(self, url: str) -> None:
        while len(self.history) != self.cu_index +1:
            self.history.pop()
        self.cu_index += 1
        self.history.append(url)
        

    def back(self, steps: int) -> str:
        self.cu_index = max(0, self.cu_index - steps)
        return self.history[self.cu_index]
        

    def forward(self, steps: int) -> str:
        self.cu_index = min(len(self.history)-1, self.cu_index+steps)
        return self.history[self.cu_index]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
