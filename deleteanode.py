def deleteNode(head, position):
    if head==None:
        return head
    elif position==0:
        return head.next
    else:
        prev=0
        curr=head
        pos=0
        while(pos<position):
            pos=pos+1
            prev=curr
            curr=curr.next
        prev.next=curr.next
        return head
