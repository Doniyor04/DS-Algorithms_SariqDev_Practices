from linked_lists_funcs import Node, LinkedList

llist = LinkedList()

llist.append("Chorshanba")
llist.push("Dushanba")
llist.push("Yakshanba")
llist.insert_after(llist.head.next, "Seshanba")
llist.deleteNode("Yakshanba")
llist.searchNode("Yakshanba")
llist.print_list()