class Node:
    def __init__(self, val=0, next=None):
        self.val= val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        for i in range(index):
            if curr: 
                curr = curr.next
            else:
                return -1 #defensive
        return curr.val if curr else -1 #defensive

    def addAtHead(self, val: int) -> None:
        head_node = Node(val)
        head_node.next = self.head
        self.head = head_node

        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_tail = Node(val)

        if not self.head:
            self.head = new_tail
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_tail
        
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index < 0:
            return
        elif index == self.size:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            curr = self.head
            new_node = Node(val)
            for i in range(index-1):
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node
        
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return

        if index == 0:
            if self.head:
                self.head = self.head.next
        else:
            curr = self.head
            for i in range(index-1):
                curr = curr.next
            if curr and curr.next:
                curr.next = curr.next.next
        
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
