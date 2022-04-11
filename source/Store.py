class Store:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def __len__(self):
        return len(self.items)

    def put(self, item):
        if self.capacity == -1:
            self.items.append(item)
        elif len(self) < self.capacity:
            self.items.append(item)
        else:
            return False

    def get(self):
        if self.items:
            return self.items.pop(0)
        else:
            return False

    def empty(self):
        self.items = []
