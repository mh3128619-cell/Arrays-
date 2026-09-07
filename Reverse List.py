class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

def reverseList(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

def printList(head):
    res = []
    temp = head
    while temp:
        res.append(str(temp.val))
        temp = temp.next
    print(" -> ".join(res))

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Original list:")
printList(head)

reversed_head = reverseList(head)
print("Reversed list:")
printList(reversed_head)
