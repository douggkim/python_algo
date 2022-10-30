# What I learned 
# 1) add conditions for checking 0 length lists 

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    if head1 == None: 
        return head2 
    if head2 == None: 
        return head1 
        
    rlist = SinglyLinkedList() 
    
    while head1 != None or head2 != None: 
        if head1 == None: 
            rlist.tail.next = head2 
            break
        if head2 == None: 
            rlist.tail.next = head1 
            break 
        if head1.data <= head2.data: 
            rlist.insert_node(head1.data)
            head1=head1.next 
        else: 
            rlist.insert_node(head2.data)
            head2=head2.next 
    
    return rlist.head
        
        
