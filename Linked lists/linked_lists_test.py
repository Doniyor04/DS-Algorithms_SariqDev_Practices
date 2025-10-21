import unittest
from linked_lists_funcs import Node, LinkedList

llist = LinkedList()
current = llist.head
new_node = Node(30)

class TestNode(unittest.TestCase):

    def test_create(self):

        # llist.head None ga tengmi
        self.assertEqual(current, None)
        # new_node ni data degan atributi bormi
        self.assertIsNotNone(new_node.data)
        # new_node ni data atributi 30 ga tengmi
        self.assertEqual(new_node.data, 30)
        # new_node ni next degan atributi None ga tengmi
        self.assertEqual(new_node.next, None)
        # llist bo'sh holatda head atributi None ga tengmi
        self.assertEqual(current, None)
        

class TestLinkedList(unittest.TestCase):

    def test_create(self):

        # llist.head ni new_node ga tengladik
        current = new_node
        # endi llist ni head degan atributi paydo bo'ldimi
        self.assertIsNotNone(current)
        # current (new_node) ni data atributi 30 ga tengmi 
        self.assertEqual(current.data, 30)

    
    def test_append_push_insertAfter(self):

        # append test
        llist.append(new_node.data)
        self.assertEqual(llist.head.data, new_node.data)
        llist.append(40)
        self.assertEqual(llist.head.next.data, 40)

        # push test
        llist.push(10)
        self.assertEqual(llist.head.data, 10)
        self.assertEqual(llist.head.next.data, 30)

        # insert_after test
        llist.insert_after(llist.head, 20)
        self.assertEqual(llist.head.next.data, 20)

    
    def test_deleteNode_searchNode(self):

        llist.deleteNode(10)
        self.assertEqual(llist.head.data, 20)

        self.assertEqual(llist.searchNode(30), True)
        self.assertEqual(llist.searchNode(10), False)


if __name__ == '__main__':
    unittest.main()