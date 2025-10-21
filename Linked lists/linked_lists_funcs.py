class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        # Listni consolga chiqaradi
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def push(self, data):
        # Listni boshiga node qo'shadi
        new_node = Node(data)
        # Headni Yangi node dan keyinga qo'yamiz 
        new_node.next = self.head
        # Yangi node ni headga olamiz
        self.head = new_node

    def insert_after(self, prev_node, new_data):
        # Listni orasidagi bir node ga yangi node qo'shish
        if prev_node is None:
            print("Tugun mavjud emas")
            return
        # Yangi node yaratamiz
        new_node = Node(new_data)
        # Yangi node ni nexti prev_node dan keyingi node ga teng qilamiz
        new_node.next = prev_node.next
        # Prev_node dan keyin yangi node ni qo'yamiz
        prev_node.next = new_node


    def append(self, data):
        # Listni oxiriga data qo'shadi
        new_node = Node(data)
        # Agar list bo'sh bo'lsa, listni boshi yangi dataga teng bo'ladi 
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        # Listni oxirigacha boradi
        while current.next:
            current = current.next
        # Listni oxiriga kelib yangi datani qo'shadi
        current.next = new_node

    def deleteNode(self, key):
        current = self.head
        if (current and current.data == key):
            self.head = current.next
            current = None
            return
        while current:
            if current.data == key:
                break
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None
    
    def searchNode(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
    
