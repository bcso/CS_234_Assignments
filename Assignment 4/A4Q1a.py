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

   def __str__(self):
      """
      Post-Conditions: 
         return a string representation of the LinkedList, in a normal list Format
      """

      listString = "["
      if self.size > 0:
         currNode = self.head
         #Traverse the linked list
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