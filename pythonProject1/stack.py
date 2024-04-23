class Stackk:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.max_size

    def add_item(self, item):
        if not self.is_full():
            self.stack.insert(0, item)
            return True

        if self.is_full():
            self.stack.pop()
            self.stack.insert(0, item)
            return True

    def pull(self):
        item = self.stack[0]
        self.stack.pop(0)
        return item