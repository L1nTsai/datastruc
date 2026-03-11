class LinkedNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None
        self.size = 0
    def append(self, num):
        New_Node = LinkedNode(num)
        if self.head is None:
            self.head = New_Node
            self.size += 1
            return
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = New_Node
            self.size += 1
    def __str__(self):
        if self.head is None:
            return ""
        temp_list = []
        curr = self.head
        while curr:
            temp_list.append(curr.val)
            curr = curr.next
        return f"{temp_list}"

        pass
llist = LinkedList()
for i in range(3):
    llist.append(i)
print(llist.size)
print(llist)

