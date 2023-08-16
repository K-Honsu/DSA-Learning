class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head):
        self.length = len(head)
        vale = self.length // 2
        return vale.val
    
new_linked = Solution()
print(new_linked.middleNode([1,2,3,4,5]))
        
        