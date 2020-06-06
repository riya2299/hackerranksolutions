def reversePrint(head):
    if head==None:
        print("nothing")
    else:
        prev=None
        cur=head
        while(cur):
            nex=cur.next
            cur.next=prev
            prev=cur
            cur=nex
        head=prev
        curr=head
        while(curr!=None):
            print(curr.data)
            curr=curr.next