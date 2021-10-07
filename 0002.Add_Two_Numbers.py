class ListNode:
    def __init__(self, val, next=None):
        self.val = value
        self.next = next
class SLinkedList:
    def __init__(self):
        self.head = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        li1=li2=n1=n2=0
        print(l1)
        while l1 is not None:
            li1+=(l1.val*(10**n1))
            n1+=1
            l1=l1.next
        while l2 is not None:
            li2+=(l2.val*(10**n2))
            n2+=1
            l2=l2.next
        li3=li4=[]
        l3=SLinkedList()
        for i in str(li1+li2):
            li3.append(int(i))
        li4=reversed(li3)
        print(li4)
        for i in li4:
                node=i
                l3.next=node
        return(l3)
