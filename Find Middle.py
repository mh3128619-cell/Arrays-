class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findMiddle(head):
    
    if not head:
        return None
    
    slow = head
    fast = head 
    
  
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow.data

def printList(head):
    res = []
    temp = head
    while temp:
        res.append(str(temp.data))
        temp = temp.next
    print(" -> ".join(res))

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

print("Original List:")
printList(head)

middle_val = findMiddle(head)

print(f"\nThe middle element is: {middle_val}")
