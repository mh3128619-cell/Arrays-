class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def hasCycle(head):
    # If the list is empty
    if not head:
        return False
    
    slow = head 
    fast = head 
    
   
    while fast and fast.next:
        slow = slow.next      
        fast = fast.next.next  
        
        if slow == fast:
            return True
            
    return False


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

head.next.next.next = head 

if hasCycle(head):
    print("Cycle detected!")
else:
    print("No cycle, the path is safe.")
