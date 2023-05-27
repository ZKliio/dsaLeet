class Element(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList(object):

    def __init__(self, head=None):
        self.head = head     
        
    def append(self, new_element):     # 1>100  100_2->200 200_3->300
        new = Element(new_element)
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new
        else:
            self.head = new

    def printList(self):
        current = self.head
        while current is not None:
            print(current.val)
            current = current.next

def initializeLL():
    list1 = LinkedList(Element(1))
    list1.append(2)
    list1.append(4)

    list2 = LinkedList(Element(1))
    list2.append(3)
    list2.append(4)

    # list1.printList()
    # list2.printList()
    return list1, list2


x, y = initializeLL()

def mergeTwoLists(list1=x, list2=y):
    
    curr1 = list1.head #head of list1
    curr2 = list2.head #head of list2
    
    # if curr1 == [] and curr2 == []:
    #     return []
    # if curr1 ==[] or curr2 == []:
    #     if curr1.next is not None:
    #         curr1 = curr2
    #     return curr1
    #     curr2 = curr1
    #     return curr2

        
    # while curr1:
    #     print(curr1.val)
    #     curr1 = curr1.next
        
    # #curr1 = curr2      #connect both
    # i = 0
    # j = 0

    # curr1 = list1.head #reset to top
    # while curr1.next:

    #     if curr1.val <= curr2.val:
    #         curr1 = curr1.next 
    #         i+=1
    #         j+=1
    #     elif curr1.val > curr2.val:
    #         prev = list1.head
    #         prev2 = list2.head
    #         for _ in range(i):
    #             prev = prev.next
            
    #         for _ in range(j):
    #             prev2 = prev2.next

    #         #swapping algorithm
    #         tmp = curr2.next
    #         prev.next = curr2
    #         curr2.next = prev2
    #         prev2.next = curr1
    #         curr2 = tmp


    
    pre = Element(0) # make a dummyhat
    curr0 = pre
    while curr1 != None and curr2 != None:

        if curr1.val < curr2.val:
            curr0.next = curr1
            curr1 = curr1.next
            #curr0 = curr0.next
        else:
            curr0.next = curr2
            curr2 = curr2.next
            #curr0 = curr0.next
        curr0 = curr0.next

    if curr1 is not None:
        curr0.next = curr1
    elif curr2 is not None:
        curr0.next = curr2
    curr0 = pre
    while curr0:
        print(curr0.val)
        curr0 = curr0.next
    
    
    # list1.printList()
    # list2.printList()












mergeTwoLists(x, y)