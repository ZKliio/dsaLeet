# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Linked_List:
       def __init__(self, head=None):
            self.head = head

       def middleNode(self):
            current = self.head
            counter = 0
            ans = []
            if self.head is None:
                return counter
            while current:
                counter+=1
                current = current.next

            current = self.head
            if counter %2 ==0:
                mid = int((counter/2) + 1)
                for i in range(1, mid):
                     current = current.next
                while current:
                     ans.append(current.val)
                     current = current.next
                return ans
            else:
                mid = (counter//2)+1
                for i in range(1, mid):
                     current = current.next
                while current:
                     ans.append(current.val)
                     current = current.next
                return ans
            
#In leetcode they help u append current to an array. just return current as it is and theyll run thru the ll for u



a = ListNode(1)     
b = ListNode(2) 
c = ListNode(3) 
d = ListNode(4) 
e = ListNode(5)

l = Linked_List(a)

a.next = b
b.next = c
c.next = d
d.next = e


print(l.middleNode())
