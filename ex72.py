class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
    def search(L, key):
        while L and L.data != key:
            L = L.next
        return L
    def insert_after(node, new_node):
        new_node.next = node.next
        node.next = new_node
    def delete_after(node):
        node.next = node.next.next
    def printout(self):
        while self:
            print (self.data)
            self = self.next

def reverse_sublist(L, s, f):
    init = L
    for _ in range(0, s-1):
        init = init.next
    p0 = init.next
    p1 = p0.next
    p2 = p1.next
    for _ in range(0, f-s):
        p1.next = p0
        p0 = p1
        p1 = p2
        if p2 is None:
            break
        p2 = p2.next
    init.next.next = p1
    init.next = p0

myList1 = ListNode(10, ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1, ListNode(11, None)))))));
myList1.printout()
reverse_sublist(myList1, 1, 5)
myList1.printout()
