class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = []



    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.max_size

    def add_new(self, new_item):
        if not self.is_full():
            self.queue.append(new_item)
            return True
        return f"Kapacita naplněna, zkuste to prosím později."

    def read_remove(self):
        if not self.is_empty():
            item = self.queue[0]
            self.queue.pop(0)
            return item

    def read_latest(self):
        print(self.queue[len(self.queue)-1])