class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def insertHead(self, val: int) -> None:
        new_node = Node(val, self.head)
        self.head = new_node
        self.size += 1

    def insertTail(self, val: int) -> None:
        if not self.head:
            self.insertHead(val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val)
        self.size += 1

    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        res = []
        curr = self.head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res