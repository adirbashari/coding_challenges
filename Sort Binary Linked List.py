# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @param A : head node of linked list
# @return the head node in the linked list


def solve(A):
    one_head = None
    one_tail = None
    zero_tail = None
    zero_head = None
    temp = A
    if A.next == None:
        return A
    while temp is not None:
        if temp.val == 0:
            if zero_head == None:
                zero_head = temp
                zero_tail = temp
            else:
                zero_tail.next = temp
                zero_tail = temp

            temp = temp.next
            zero_tail.next = None

        else:
            if one_head == None:
                one_head = temp
                one_tail = temp
            else:
                one_tail.next = temp
                one_tail = temp
            temp = temp.next
            one_tail.next = None

    zero_tail.next = one_head
    temp = zero_head
    while temp is not None:
        print(temp.val)
        temp = temp.next


a = ListNode(1)
b = ListNode(0)
c = ListNode(0)
d = ListNode(0)
e = ListNode(0)
f = ListNode(1)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

solve(a)
