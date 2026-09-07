class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeTwolists(list1, list2):
    dummy = Node(0)
    tail = dummy
    
    while list1 and list2:
        if list1.data < list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
        
    return dummy.next

def printList(head):
    res = []
    temp = head
    while temp:
        res.append(str(temp.data))
        temp = temp.next
    print(" -> ".join(res) if res else "Empty List")


list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(5)

list2 = Node(2)
list2.next = Node(4)
list2.next.next = Node(6)

print("List 1:")
printList(list1)
print("List 2:")
printList(list2)


merged = mergeTwolists(list1, list2)

print("\nMerged Result:")
printList(merged)
