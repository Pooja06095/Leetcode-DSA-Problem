class Solution:
    def reverseBetween(self, head, left, right):
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        # Move prev to node just before left
        for _ in range(left - 1):
            prev = prev.next

        current = prev.next

        # Reverse the required portion
        for _ in range(right - left):
            next_node = current.next
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next