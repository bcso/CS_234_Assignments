"""CS 234 Assignment 1 Question 3 - Integer matrix class
"""
class IntMatrix (object):
    def __init__(self, m11, m12, m21, m22):
        """
        Assumptions
        all the matrix values (m11, m12, m21, m22)
        are integers between -999 and 999

        preconditions: provide 4 integers that range between -999 and 999
        postcondition: return a new IntMatrix object
        """
        
        if (type(m11) != type(1)):
            raise TypeError, "m11 must be an integer"
        elif (type(m12) != type(1)):
            raise TypeError, "m12 must be an integer"
        elif (type(m21) != type(1)):
            raise TypeError, "m21 must be an integer"
        elif (type(m22) != type(1)):
            raise TypeError, "m22 must be an integer"
        else:
            self.matrix = {"m11" : m11, "m12" : m12, "m21" : m21, "m22" : m22}

    def getm11(self):
        return self.matrix.get("m11")

    def getm12(self):
        return self.matrix.get("m12")

    def getm21(self):
        return self.matrix.get("m21")

    def getm22(self):
        return self.matrix.get("m22")
        
    def __str__(self):
        
        m11 = self.getm11()     
        m12 = self.getm12()
        m21 = self.getm21()
        m22 = self.getm22()
        return("%4d %4d\n%4d %4d") %(m11, m12, m21, m22)


    def addm(self, m):        
        m11 = self.getm11() + m.getm11()
        m12 = self.getm12() + m.getm12()
        m21 = self.getm21() + m.getm21()
        m22 = self.getm11() + m.getm22()

        return IntMatrix(m11,m12,m21,m22)

    def subtractm(self, m):
        m11 = self.getm11() - m.getm11()
        m12 = self.getm12() - m.getm12()
        m21 = self.getm21() - m.getm21()
        m22 = self.getm11() - m.getm22()

        return IntMatrix(m11,m12,m21,m22)

    def multiplym(self, m):
        m11 = self.getm11() * m.getm11() + self.getm12() * m.getm21()
        m12 = self.getm11() * m.getm12() + self.getm12() * m.getm22()
        m21 = self.getm21() * m.getm11() + self.getm22() * m.getm21()
        m22 = self.getm21() * m.getm12() + self.getm22() * m.getm22() 

        return IntMatrix(m11,m12,m21,m22)

    def equals(self, m):
        return ((self.getm11() == m.getm11()) and (self.getm12() == m.getm12()) and (self.getm21() == m.getm21()) and (self.getm22() == m.getm22()))

    def notEquals(self, m):
        return ((self.getm11() != m.getm11()) or (self.getm12() != m.getm12()) or (self.getm21() != m.getm21()) or (self.getm22() != m.getm22()))


    def det(self):
        """
        Assumptions

        Input must be an object that is a class of IntMatrix, which has
        an identical matrix structure

        postcondition: return a single integer value that is the determininant
        """
        
        return self.getm11() * self.getm22() - self.getm21() * self.getm12()
