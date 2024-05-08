
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        current_node = self.head
        data_list = []  # Create an empty list to store the data

        while current_node:
            if current_node.data is not None:  # Check for None before appending
                data_list.append(str(current_node.data))  # Convert to string explicitly
            current_node = current_node.next

        return "DoubleLinkedList[" + ", ".join(data_list) + "]"

    def insert(self, data, pos):
        if self.head == None and pos == 0:
            self.head = Node(data)
        elif pos == 0:
            new = Node(data)
            new.next = self.head
            self.head.prev = new
            self.head = new
        else:
            index = 0
            new = Node(data)
            temp = self.head
            while temp != None and index+1 != pos:
                temp = temp.next
                index += 1

            if temp != None:
                new.next = temp.next
                temp.next = new
                new.prev = temp

            else:
                print("Out of bounds")

    def delete(self, pos):
        temp = self.head
        if pos == 0:
            self.head = self.head.next
            self.head.prev = None
        else:
            index = 0
            while index+1 != pos and temp.next != None:
                print(index)
                temp = temp.next
                index += 1
            if temp.next.next != None:
                temp.next = temp.next.next
                temp.next.next.prev = temp
            elif temp.next != None:
                temp.next = temp.next.next
            else:
                print("Position doesnt exist")