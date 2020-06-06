def insertNodeAtPosition(head, data, position):
    node=SinglyLinkedListNode(data)
    if head==None:
        head=node
    elif position==0:
        node.next=head
        head=node
    else:
        prev=0
        curr=head
        currpos=0
        while(currpos<position and curr.next!=None):
            prev=curr
            curr=curr.next
            currpos+=1
        prev.next=node
        node.next=curr
    return head