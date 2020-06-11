def has_cycle(head):
    if (head == None):
        return False
    else:
        first = head
        nex = head.next
        while (first != nex) :
            if (nex == None or nex.next == None):
                return False
            else:
                first = first.next;
                nex = nex.next.next;
        return True
