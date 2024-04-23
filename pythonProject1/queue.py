class Queueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def add_new(self, new_item):
        self.queue.append(new_item)

    def read_remove(self):
        if not self.is_empty():
            item = self.queue[0]
            self.queue.pop(0)
            return item




