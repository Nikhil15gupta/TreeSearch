# Write a console app that builds a tree made up of nodes containing a label & id.
# Use the words in the attached document as the label.
# The app should prompt users to perform either a breadth-first or depth-first search for a node by label,
# and it outputs the node id and the time it took to find it.

#importing required packages
import itertools
import time
from collections import deque

#reading the text file
file = open(r"random-words.txt", "r")
lines = file.readlines()
words = []
for line in lines:
    words.append(line.strip("\n"))

#creating a Node class
class Node:
    id_iter = itertools.count()

    def __init__(self, label):
        self.left = None
        self.right = None
        self.label = label
        self.id = next(self.id_iter)

    #function to insert a node in the tree
    def insert(self, label):
        # Compare the new value with the parent node
        if self.label:
            if label < self.label:
                if self.left is None:
                    self.left = Node(label)
                else:
                    self.left.insert(label)
            elif label > self.label:
                if self.right is None:
                    self.right = Node(label)
                else:
                    self.right.insert(label)
        else:
            self.label = label

    # breadth-first-search
    def bfs(self, target, r=None):
        if r is None:
            return
        if r.label == target:
            print("\nBreadth First Search: id of", r.label, "is", r.id)
            return
        queue = deque([r])
        while queue:
            cur_node = queue.popleft()

            if cur_node.left is not None:
                if cur_node.left.label == target:
                    print("\nBreadth First Search: id of", cur_node.left.label, "is", cur_node.left.id)
                    return
                queue.append(cur_node.left)

            if cur_node.right is not None:
                if cur_node.right.label == target:
                    print("\nBreadth First Search: id of", cur_node.right.label, "is", cur_node.right.id)
                    return
                queue.append(cur_node.right)

        print("The label", target, "doesn't exist in the Tree.")

#function to create Adjacency List
def makeList(r):
    if r is None:
        return
    else:
        d[r] = []
        makeList(r.left)
        if r.left:
            d[r].append(r.left)
        if r.right:
            d[r].append(r.right)
        makeList(r.right)
    return d

#Depth-First-Search
def dfs(al, r, target):
    if r is None:
        return
    if r.label == target:
            print("\nDepth First Search: id of", r.label, "is", r.id)
            return
    stack = deque([r])
    visited = []
    while stack:
        curr_node = stack.pop()
        if curr_node not in visited:
            if curr_node.label == target:
                print("\nDepth First Search: id of", curr_node.label, "is", curr_node.id)
                return
            visited.append(curr_node)
            [stack.append(x) for x in al[curr_node]]
    print("The label", target, "doesn't exist in the Tree.")

# Depth first search Using Recursion
# def dfs(target, r=None):
#     if r is None:
#         return
#     if r.label == target:
#         print("\nDepth First Search: id of", r.label, "is", r.id)
#         return
#     if r.left:
#         if r.left.label == target:
#             print("\nDepth First Search: id of", r.left.label, "is", r.left.id)
#             return
#         dfs(target, r.left)
#     if r.right:
#         if r.right.label == target:
#             print("\nDepth First Search: id of", r.right.label, "is", r.right.id)
#             return
#         dfs(target, r.right)
    # print("The label", target, "doesn't exist in the Tree.")

#main function
if __name__ == '__main__':
    root = Node(words[0])
    for i in range(len(words)):
        root.insert(words[i])
    d = {}
    aList = makeList(root)
    while(True):
        search_type = input("\nPlease select the search type(Enter number):\n\n1: Breadth First Search\n2: Depth First Search\n3: Exit\n")
        if search_type == "3":
            break        
        if search_type == "1":    
            label = input("\nPlease enter the Label to search:\n")
            start_time = time.time()
            root.bfs(label, root)
            end_time = time.time()
            print("Execution Time:", (end_time - start_time)*1000, "miliseconds")
        elif search_type == "2":
            label = input("\nPlease enter the Label to search:\n")
            start_time = time.time()
            dfs(aList, root, label)
            end_time = time.time()
            print("Execution Time:", (end_time - start_time)*1000, "miliseconds")
        else:
            print("\nIncorrect option selected.")


