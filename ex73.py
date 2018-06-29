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
    def create_cycle(from_node, to_node):
        from_node.next = to_node

def test_cyclicity(L):
    fast, slow = L, L
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            it = L
            counter = 1
            while it is not slow:
                it = it.next
                counter += 1
            s1 = counter
            it = it.next
            counter += 1
            while it is not slow:
                it = it.next
                counter += 1
            s2 = counter
            len_cycle = s2-s1
            to_pos = 2*len_cycle - s1
            it = L
            for _ in range(0, to_pos):
                it = it.next
            return it
    return None

n1 = ListNode(1, None)
L = n1
n2 = ListNode(2, None)
n1.insert_after(n2)
n3 = ListNode(3, None)
n2.insert_after(n3)
n4 = ListNode(4, None)
n3.insert_after(n4)
n5 = ListNode(5, None)
n4.insert_after(n5)
L.printout()
n = test_cyclicity(L)
if n:
    print (n.data)
else:
    print("There is not a cycle")
n5.create_cycle(n3)

n = test_cyclicity(L)
if n:
    print (n.data)
else:
    print("There is not a cycle")
