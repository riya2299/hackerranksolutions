def mergeLists(head1, head2):
    head=SinglyLinkedListNode(0)
    ptr=head
    while True:
        if head1==None and head2==None:
            break
        elif head1 is None:
            ptr.next=head2
            break
        elif head2 is None:
            ptr.next=head1
            break
        else:
            small=0
            if head1.data>head2.data:
                small=head2.data
                head2=head2.next
            else:
                small=head1.data
                head1=head1.next
            newnode=SinglyLinkedListNode( small)
            ptr.next=newnode
            ptr=ptr.next
    return head.next