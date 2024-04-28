
class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        value = self.front()
        self.items = self.items[1:]
        return value

    def front(self):
        return self.items[0]

    def rear(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def __str__(self):
        return f"Queue({self.items})"



