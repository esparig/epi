class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def print_me(self):
        e = self
        while e.next:
            print(e.val, "-> ", end="")
            e = e.next
        print(e.val)

def mergeSortLinkedList(A):
    # Base case length of 0 or 1:
    if A is None or A.next is None:
        return A

    leftHalf, rightHalf = splitTheList(A)

    left = mergeSortLinkedList(leftHalf)
    right = mergeSortLinkedList(rightHalf)

    return mergeTheLists(left, right)

def splitTheList(sourceList):
    if sourceList is None or sourceList.next is None:
        leftHalf = sourceList
        rightHalf = None

        return leftHalf, rightHalf

    else:
        midPointer = sourceList
        frontRunner = sourceList.next

        while frontRunner != None:
            frontRunner = frontRunner.next

            if frontRunner != None:
                frontRunner = frontRunner.next
                midPointer = midPointer.next

    leftHalf = sourceList
    rightHalf = midPointer.next
    midPointer.next = None

    return leftHalf, rightHalf

def mergeTheLists(leftHalf, rightHalf):
    fake_head = ListNode(None)
    curr = fake_head

    while leftHalf and rightHalf:
        if leftHalf.val < rightHalf.val:
            curr.next = leftHalf
            leftHalf = leftHalf.next

        else:
            curr.next = rightHalf
            rightHalf = rightHalf.next

        curr = curr.next

    if leftHalf == None:
        curr.next = rightHalf

    elif rightHalf == None:
        curr.next = leftHalf

    return fake_head.next

# Node A:
nodeA1 = ListNode(2)

nodeA2 = ListNode(1)
nodeA1.next = nodeA2

nodeA3 = ListNode(9)
nodeA2.next = nodeA3

nodeA4 = ListNode(3)
nodeA3.next = nodeA4

# Node C:
nodeC1 = ListNode(5)
nodeA4.next = nodeC1

nodeC2 = ListNode(6)
nodeC1.next = nodeC2

nodeC3 = ListNode(4)
nodeC2.next = nodeC3

nodeC4 = ListNode(5)
nodeC3.next = nodeC4

nodeA1.print_me()
mergeSortLinkedList(nodeA1).print_me()
