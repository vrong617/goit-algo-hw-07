class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def find_max_value(node):
    if node is None:
        return None

    current = node
    while current.right is not None:
        current = current.right

    return current.key


def find_min_value(node):
    if node is None:
        return None

    current = node
    while current.left is not None:
        current = current.left

    return current.key


def sum_of_values(node):
    if node is None:
        return 0

    return node.key + sum_of_values(node.left) + sum_of_values(node.right)


root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.right.right = Node(30)
root.right.left = Node(15)

max_value = find_max_value(root)
min_value = find_min_value(root)
sum_of_all_values = sum_of_values(root)

print(f"Найбільше значення в дереві: {max_value}")
print(f"Найменше значення в дереві: {min_value}")
print(f"Сума всіх значень в дереві: {sum_of_all_values}")
