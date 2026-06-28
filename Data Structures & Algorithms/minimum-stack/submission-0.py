class MinStack:

    def __init__(self):
        self.list_ = []

    def push(self, val: int) -> None:
        return self.list_.append(val)
        

    def pop(self) -> None:
        return self.list_.pop(-1)
        

    def top(self) -> int:
        return self.list_[-1]

    def getMin(self) -> int:
        return min(self.list_)
        
