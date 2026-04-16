# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        if len(lists)==1:
            return lists[0]
        
        def mergeTwoLists(list1, list2):

            node = ListNode()
            head = node
            tail = node
            while list1 is not None and list2 is not None:
                if list1.val <= list2.val:
                    head.next = list1
                    list1 = list1.next
                else:
                    head.next = list2
                    list2 = list2.next
                head = head.next
            while list1 is not None:
                head.next = list1
                list1 = list1.next
                head =  head.next
            while list2 is not None:
                head.next = list2
                list2 = list2.next
                head =  head.next
            return tail.next
        head = mergeTwoLists(lists[0],lists[1])
        for i in range(2,len(lists)):
            head = mergeTwoLists(head,lists[i])
        return head

        