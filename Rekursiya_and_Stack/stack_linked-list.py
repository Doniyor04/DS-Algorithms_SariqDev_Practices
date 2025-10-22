class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def len_list(self):
        # Listni uzunligini aniqlaydi
        current = self.head
        i = 0
        while current:
            current = current.next
            i += 1 
        return i
    # Listni uzunligini aniqlashdan maqsad listda nechta element borligi. Listni bo'sh yoki to'la ekanligini aniqlash
    
    def push(self, data):
        # List oxiriga element qo'shadi 
        if self.len_list() == 5: # Agar list to'la bo'lsa element qo'shmaydi
            return "To'plam to'la"
        
        new_node = Node(data)
        if self.head is None: # List bo'sh bo'lsa listni boshiga element qo'shadi
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def deleteNode(self, key):
        # Listdan element o'chiradi, deleteNode ni pop() metodi uchun ishlatamiz
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

    def pop_node(self):
        # Listdagi oxirgi elementni sug'urib oladi va return qiladi
        current = self.head
        if current is None: # list bo'shligini tekshiradi
            return "To'plam bo'sh"
        
        while current.next:
            current = current.next
        self.deleteNode(current.data)
        return current.data
        
    def isEmpty(self):
        # Listda qancha joy borligini yoki bo'shligini tekshiradi
        current = self.head
        if not current:
            return "To'plam bo'sh"
        
        len_list = self.len_list()
        return f"To'plamda {5 - len_list} ta bo'sh joy bor" if 5 - len_list > 0 else "To'plam to'la"
    
    def isFull(self):
        # Listni to'laligini yoki qancha element borligini tekshiradi
        len_list = self.len_list()
        if len_list == 5:
            return "To'plam to'la"
        
        return f"To'plamda {len_list} ta element bor" if len_list > 0 else "To'plam bo'sh"
    
    def peek(self):
        # Listdagi oxirgi elementni ko'rsatadi
        current = self.head
        if current is None: # List bo'shligini tekshiradi
            return "To'plam bo'sh"

        while current.next:
            current = current.next

        return current.data


    