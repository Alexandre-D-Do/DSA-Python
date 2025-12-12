from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

# The runtime complexity of this solution is O(N+M)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Empty lists edge cases
        if list1 == None and list2 == None:
            return None
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        # Set merged list head, as well as lists heads based on smaller initial value
        if list1.val <= list2.val:
            merged_list_head = list1
            return_node = list1
            l1_head = list1.next
            l2_head = list2
        elif list1.val > list2.val:
            merged_list_head = list2
            return_node = list2
            l1_head = list1
            l2_head = list2.next
        
        # Break if both heads are equal to None
        while l1_head != None or l2_head != None:
            
            # If one head is equal to None, set merged list head's next to the other head's value and return
            if l1_head == None:
                merged_list_head.next = l2_head
                break
            elif l2_head == None:
                merged_list_head.next = l1_head
                break
            if l1_head.val <= l2_head.val:
                merged_list_head.next = l1_head
                merged_list_head = merged_list_head.next
                l1_head = l1_head.next
            else:
                merged_list_head.next = l2_head
                merged_list_head = merged_list_head.next
                l2_head = l2_head.next
        
        return return_node
           
'''
Prompt:
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.


Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.

Pseudocode:

Check both first values
Set merged list head
Set both list heads
Compare values, setting smaller values as merged list's next
Update head of list with smaller value to smaller value's next
Repeat
Edge cases:
Empty lists
Uneven input lists:
When comparing a value to a none, set merged list's next as the non none value
'''

        