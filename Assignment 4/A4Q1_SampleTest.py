from A4Q1e import LinkedList

#Q1 a)

a = LinkedList()
a.append(2.0)
a.append('good')
print (len(a))


a.append(2)
a.append('b')
a.append(True)
# print (str(a))

#Q1 c)

a.remove(2.0)
# print(a)


#Q1 e)

a.pop(3)
# print(a)

a.insert(0, 2)
print(a)

print (a.count(2))
