# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode()
        current = res
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
            
        return res.next
    
new_linked = Solution()
new_linked.mergeTwoLists([1,2,3],[1,3,4])
print(new_linked)


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    # def __str__(self):
    #     temp_node = ListNode()
    #     result = ''
    #     while temp_node is not None:
    #         result += str(temp_node.val)
    #         if temp_node.next is not None:
    #             result += ' -> '
    #         temp_node = temp_node.next
    #     return result
    
    
    # def deleteDuplicates(self, head):
    #     if head is None:
    #         return None
    #     # head = ListNode()
    #     current = head
    #     obj = {}
    #     prev = None
    #     while current:
    #         if current.val in obj:
    #             if current.next is None:
    #                 self.tail = prev
    #                 self.tail.next = None
    #             else:
    #                 prev.next = current.next
    #         else:
    #             obj[current.val] = True
    #             prev = current
    #         current = current.next
    #     # return head
    # def deleteDuplicates(self, head):
    #     if head is None:
    #         return None
    #     current = head
    #     while current and current.next:
    #         if current.val == current.next.val:
    #             current.next = current.next.next
    #             # current.next = None
    #         else:
    #             current = current.next
    #     return head
    
    def isPalindrome(self, head):
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        l,r = 0, len(arr) -1
        while l <= r:
            if arr[l] != arr[r]:
                return False
            l += 1
            r -= 1
            return True
    
    def isPalindrome(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
            
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True
    
    def middleNode(self, head):
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        leng = len(arr) // 2
        pointer = leng
        return pointer
    
    def findMergeNode(head1, head2):
        length1 = 0
        length2 = 0
        current1 = head1
        current2 = head2
        
        while current1:
            length1 += 1
            current1 = current1.next
            
        while current2:
            length2 += 1
            current2 = current2.next
        
        length_diff = abs(length1 - length2)
        
        current1 = head1
        current2 = head2
        
        if length1 > length2:
            for _ in range(length_diff):
                current1 = current1.next
        else:
            for _ in range(length_diff):
                current2 = current2.next
        
        while current1 != current2:
            current1 = current1.next
            current2 = current2.next
            
        return current1.data
        
            
# new_linked = Solution()
# # new_linked.deleteDuplicates([1,1,2])
# new_linked.middleNode([1,2,3,4,5])
# print(new_linked)
        
        