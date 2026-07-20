class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def find_length(head):
    count = 0
    tmp = head
    while tmp.next != None:
        count += 1
        tmp = tmp.next

    return count


nums = [10, 20, 30, 40, 50]
node = Node(nums[0])
for item in nums[1:]:
    node.next = Node(item)
