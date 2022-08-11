from mimetypes import init
import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(node):
    print(node.data, end='')
    if node.left != '.':
        preorder(node.left)
    if node.right != '.':
        preorder(node.right)

def inorder(node):
    if node.left != '.':
        inorder(node.left)
    print(node.data, end='')
    if node.right != '.':
        inorder(node.right)

def postorder(node):
    if node.left != '.':
        postorder(node.left)
    if node.right != '.':
        postorder(node.right)
    print(node.data, end='')


n = int(input())
t = []
for _ in range(n):
    data, left, right = input().split()
    node = Node(data)

    node.left = left
    node.right = right

    t.append(node)

for i in range(n):
    for j in range(n):
        if t[i].data == t[j].left:
            t[j].left = t[i]
        elif t[i].data == t[j].right:
            t[j].right = t[i]

preorder(t[0])
print()
inorder(t[0])
print()
postorder(t[0])