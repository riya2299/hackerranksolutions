def insertNodeAtTail(head, data):
    if (head==None):
        head=SinglyLinkedListNode(data)
    else:
        curr=head
        while(curr.next!=None):
            curr=curr.next
        curr.next=SinglyLinkedListNode(data)
    return head