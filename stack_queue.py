class Queue:

    def __init__(self):

        self._items = []

    def enqueue(self, item):

        self._items.append(item)

    def dequeue(self):

        return self._items.pop(0)

    def peek(self):

        return self._items[0]

    def __str__(self):

        return str(self._items)


class Stack:

    def __init__(self):

        self._items = []

    def enstack(self, item):

        self._items.append(item)

    def destack(self):

        return self._items.pop(-1)

    def peek(self):

        return self._items[-1]

    def __str__(self):

        return str(self._items)


def main():

    print('Queue: ')
    new_queue = Queue()
    new_queue.enqueue(5)
    new_queue.enqueue(7)
    new_queue.enqueue(3)
    new_queue.enqueue(1)
    new_queue.enqueue(4)
    new_queue.enqueue(2)
    print(new_queue)
    print(new_queue.peek())
    new_queue.dequeue()
    print(new_queue)
    print(new_queue.peek())

    print('Stack: ')
    new_stack = Stack()
    new_stack.enstack(5)
    new_stack.enstack(7)
    new_stack.enstack(3)
    new_stack.enstack(1)
    new_stack.enstack(4)
    new_stack.enstack(2)
    print(new_stack)
    print(new_stack.peek())
    new_stack.destack()
    print(new_stack)
    print(new_stack.peek())


if(__name__ == '__main__'):

    main()
    
