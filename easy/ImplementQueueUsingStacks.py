class MyQueue:

    def __init__(self):
        self.queue = []
        self.front = None
    def push(self, x: int) -> None:
        self.queue.append(x)
        print(self.queue)

    def pop(self) -> int:
        self.front = self.queue[0]
        self.queue= self.queue[1:]
        print(self.queue)
        return self.front

    def peek(self) -> int:
        
        return self.queue[0]

    def empty(self) -> bool:
        if len(self.queue) < 1:
            return True
        else:
            return False


obj = MyQueue()
obj.push(1)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()

