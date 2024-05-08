
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data, pos):
        new = Node(data)
        temp = self.head
        index = 0
        if pos == 0:
            if self.head is None:
                self.head = new
            else:
                new.next = self.head
                self.head = new

        else:
            while temp != None and index + 1 != pos:
                index += 1
                temp = temp.next

            if temp != None:
                new.next = temp.next
                temp.next = new
            else:
                print("Out of bounds")

    def delete(self, pos):
        temp = self.head
        if pos == 0:
            self.head = self.head.next
        else:
            index = 0
            while index+1 != pos and temp.next != None:
                print(index)
                temp = temp.next
                index += 1
            if temp.next != None:
                temp.next = temp.next.next
            else:
                print("Position doesnt exist")

    def __str__(self):
        current_node = self.head
        data_list = []  # Create an empty list to store the data

        while current_node:
            if current_node.data is not None:  # Check for None before appending
                data_list.append(str(current_node.data))  # Convert to string explicitly
            current_node = current_node.next

        return "LinkedList[" + ", ".join(data_list) + "]"