def insertNodeAtHead(llist, data):
    curr=SinglyLinkedListNode(data)
    curr.next=llist
    llist=curr
    return llist
