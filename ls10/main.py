"""Linked List example"""
from datetime import datetime
import colorama

def log(error_message) -> None:
    """Log func"""
    print(f"""{'-'*20}
{colorama.Fore.RED}ERROR LOG: {datetime.now()} 
ERROR MESSAGE: {error_message}{colorama.Fore.RESET}""")

class Node:
    """List Node - element"""
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    """Linked List CLass"""
    def __init__(self) -> None:
        self.head = None

    def append(self, data) -> None:
        """Append new Node"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert(self, data, position) -> None:
        """Insert data"""
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        for _ in range(position - 1):
            if current is None:
                log('Position out of bounds')
                return
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def remove(self, data) -> None:
        """Remove item by value"""
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        log(f'{data} not found in the list')
        return

    def display(self) -> str:
        """Display Linked List"""
        current = self.head
        build_str = ''
        while current:
            build_str += f'{current.data}{current.next and "->" or " "}'
            current = current.next
        return build_str

    # pop(9) -> index pop() -> last item



linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)
print(linked_list.display())
linked_list.remove(5)
linked_list.remove(7)
print(linked_list.display())
linked_list.insert('a', 4)
linked_list.insert('b', 2)
linked_list.insert('c', 11)
print(linked_list.display())
