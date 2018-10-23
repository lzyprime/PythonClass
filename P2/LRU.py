class LRU:
    def __init__(self, capacity = 3):
        self.data = []
        self.capacity = capacity

    def set(self, v):
        if self.data[-1] == v:
            return
        if v in self.data:
            self.data.remove(v)
        elif len(self.data) == self.capacity:
            self.data.pop(0)
        self.data.append(v)

    def get(self, v):
        if v in self.data:
            if v != self.data[-1]:
                self.data.remove(v)
                self.data.append(v)
            return self.data[-1]
        else:
            return -1

