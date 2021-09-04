"""
File: add2.py
Name: Hsuan Tung, Lin
------------------------
There are two existed linked list.
Each node of a linked list stores a value, putting these value in reversed order is the ture value of the linked list.
The program adds the true values up and construct a new linked list.
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    The program finds the values of 2 linkedlist and add them up.
    Then, construct a new linkedlist to store the value.
    :param l1: linkedlist, storing first value
    :param l2: linkedlist, storing second value
    :return: linkedlist, storing total value
    """
    ans = 0  # int, the total value

    # storing first value in a str1
    head1 = l1
    str1 = str(head1.val)
    cur = head1
    while cur.next is not None:
        cur = cur.next
        str1 = str(cur.val) + str1

    # storing second value in a str2
    head2 = l2
    str2 = str(head2.val)
    cur = head2
    while cur.next is not None:
        cur = cur.next
        str2 = str(cur.val) + str2

    ans_val = int(str1) + int(str2)             # addition
    reverse_ans_str = ''                        # reverse the value and convert it to a string
    for i in range(len(str(ans_val))):
        num = str(ans_val)[i]
        reverse_ans_str = num + reverse_ans_str

    # construct a new linkedlist
    for i in range(0, (len(reverse_ans_str))):
        if i == 0:  # first node
            ans = ListNode(int(reverse_ans_str[i]), None)
            cur = ans
        else:       # other nodes
            cur.next = ListNode(int(reverse_ans_str[i]), None)
            cur = cur.next
    return ans


####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)



def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
