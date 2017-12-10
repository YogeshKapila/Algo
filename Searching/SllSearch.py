"""
Given two Singly linked lists, the task is to check whether the first list is present in 2nd list or not.
"""


# Basic Linked List Management
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_sll(node):
    print("\nLinked List: ", end='')
    while node:
        print("{} ".format(node.data), end='')
        node = node.next


def find_list(listA, listB):
    """
    Search listA in listB
    :param listA: The list to be searched for
    :param listB: The base list
    :return: True if listA found in listB else return False
    """

    first = listA
    second = listB

    # Both Empty
    if first is None and second is None:
        return True

    # Only one empty
    if (first is None) or (second is None):
        return False

    while second:
        p1 = first
        p2 = second

        while p1:
            if not p2:
                return False

            elif p2.data == p1.data:
                p1 = p1.next
                p2 = p2.next

            else:
                break

        if not p1:
            return True

        p1 = first
        second = second.next

    return False


if __name__ == "__main__":
    A = Node(1)
    A.next = Node(2)
    A.next.next = Node(3)
    A.next.next.next = Node(4)

    print_sll(A)

    B = Node(1)
    B.next = Node(2)
    B.next.next = Node(1)
    B.next.next.next = Node(2)
    B.next.next.next.next = Node(3)
    B.next.next.next.next.next = Node(4)

    C = Node(5)
    print_sll(B)
    print("\nList Found: ", find_list(A, B))
