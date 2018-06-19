class ListNode:
    def __init__(self, data=0, next=None):
        self.data=data
        self.next=next
    def insert_after(node, new_node):
        new_node.next = node.next
        node.next = new_node
    def printout(self):
        while self:
            print (self.data)
            self = self.next

def merge_two_sorted_lists(L1, L2):
    head = ListNode()
    if L1.data <= L2.data:
        head = L1
        L1 = L1.next
    else:
        head = L2
        L2 = L2.next

    current = head
    while L1 and L2:
        new = ListNode()
        if L1.data <= L2.data:
            new = L1
            L1 = L1.next
        else:
            new = L2
            L2 = L2.next
        current.next = new
        current = current.next

    current.next = L1 or L2
    return head

myList1 = ListNode(2, ListNode(5, ListNode(7, None)));
myList1.printout()
myList2 = ListNode(3, ListNode(11, None));
myList2.printout()

merge_two_sorted_lists(myList1, myList2).printout();
