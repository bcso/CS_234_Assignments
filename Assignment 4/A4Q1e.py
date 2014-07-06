class ListNode:
   def __init__(self, item, next):
      """
      Post-Conditions: 
         return a ListNode object that has an item entry and a next value
      """

      self.item = item
      self.next = next

class LinkedList:
   def __init__(self):
      "create an empty list"      
      self.head = None
      self.tail = None
      self.size = 0

   def append(self, item):
      """
      Post-Conditions: 
         return a singly linked list of the new node appended to the end of the current list
      """

      #Initialize first element of linked list
      if self.size == 0:
         newNode = ListNode(item, None)         
         self.head = newNode
         self.tail = newNode
         self.size += 1
      #Append the new value to the existing list
      elif self.size != 0:
         newNode = ListNode(item, None)
         self.tail.next = newNode         
         self.tail = self.tail.next         
         self.size += 1

   def remove(self, anItem):
      """      
      Post-Conditions: 
         remove an item from the singly linked list 
      """

      prevNode = None
      currNode = self.head

      while (currNode is not None and currNode.item != anItem):
         prevNode = currNode
         currNode = currNode.next

      #We are dealing with the first value of the list
      if prevNode == None:
         self.head = currNode.next
         self.size -= 1
      elif currNode is not None:
         prevNode.next = currNode.next
         self.size -= 1

   def pop(self, i):      
      """
      Pre-Conditions: 
         i cannot be negative
         i must be of type Integer
         i must be larger than the size of the list - 1
      Post-Conditions:
         return the value of the linked list at position i
         remove the value of the linked list at position i (just like in remove)
      """

      if i < 0:
         raise ValueError, "i must be positive"
      elif type(i) != type(1):
         raise TypeError, "i must be of type Integer"
      elif i > self.size - 1:
         raise IndexError, "i cannot be larger than length of the LinkedList"

      prevNode = None
      currNode = self.head
      currNum = 0
      valueToPop = ""

      #Traverse the linked list
      while (currNode is not None and currNum != i):
         prevNode = currNode
         currNode = currNode.next
         currNum += 1

      #We are dealing with the first value of the list
      if prevNode == None:
         valueToPop = currNode.item
         self.head = currNode.next
         self.size -= 1
      elif currNode is not None:
         valueToPop = currNode.item
         prevNode.next = currNode.next
         self.size -= 1

      return valueToPop

   def insert(self, i, anItem):
      """
      Pre-Conditions: 
         i cannot be negative
         i must be of type Integer
         i must be larger than the size of the list - 1
      Post-Conditions:
         insert anItem into i'th position of the linked list
      """

      if i < 0:
         raise ValueError, "i must be positive"
      elif type(i) != type(1):
         raise TypeError, "i must be of type Integer"
      elif i > self.size - 1:
         raise IndexError, "i cannot be larger than length of the LinkedList"

      prevNode = None
      currNode = self.head
      currNum = 0      
      newNode = ListNode(anItem, None)

      #Traverse the linked list
      while (currNode is not None and currNum != i):
         print currNum
         print i
         prevNode = currNode
         currNode = currNode.next
         currNum += 1

      #We are dealing with the first value of the list
      if prevNode == None:
         newNode.next = currNode
         self.head = newNode
         self.size += 1         
      elif currNode is not None:
         newNode.next = currNode
         prevNode.next = newNode
         self.size += 1   

   def count(self, anItem):
      """
      Post-Conditions:
         return the number of occurences of anItem in the linked list
      """

      currNode = self.head
      count = 0

      #Traverse the linked list
      while(currNode is not None):
         #Matched value, increment counter by 1
         if currNode.item == anItem:
            count +=1
         currNode = currNode.next

      return count

   def __str__(self):
      """
      Post-Conditions: 
         return a string representation of the LinkedList, in a normal list Format
      """

      listString = "["
      if self.size > 0:
         currNode = self.head
         while (currNode is not None):            
            # Convert to string!         
            if type(currNode.item) != type('s'):
               listString += (str(currNode.item) + ", ")
            # Format the element to match a string output in a real list
            elif type(currNode.item) == type('s'):
               listString += ("'" + currNode.item +"'" + ", ")
            currNode = currNode.next
         #Remove the last two characters 
         listString = listString[:-2]

      listString += "]"
      return listString

   def __len__(self):
      """
      Post-Conditions: 
         return the length of the LinkedList
      """

      return self.size


a = LinkedList()
a.append(2.0)
a.append('good')
a.append(2)
a.append('b')
a.append(True)