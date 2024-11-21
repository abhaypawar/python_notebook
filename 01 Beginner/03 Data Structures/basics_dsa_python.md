A comprehensive list of **data structures** commonly used in computer science, programming, and software development. They can be broadly categorized based on their type and usage.

---

## **1. Primitive Data Structures**
These are the simplest types of data structures, typically provided by the programming language itself.

- **Integer**
- **Float**
- **Character**
- **Boolean**

---

## **2. Linear Data Structures**
These structures store data sequentially.

### **a. Static Linear Data Structures**  
- **Array**: Fixed-size, contiguous memory allocation for storing elements of the same type.  
  Examples: `int[]`, `char[]`.

### **b. Dynamic Linear Data Structures**  
- **Linked List**: Elements (nodes) linked via pointers.
  - **Singly Linked List**
  - **Doubly Linked List**
  - **Circular Linked List**

- **Stack**: Follows LIFO (Last In, First Out) principle.  
  Operations: `push`, `pop`, `peek`.

- **Queue**: Follows FIFO (First In, First Out) principle.  
  Variants:
  - **Simple Queue**
  - **Circular Queue**
  - **Priority Queue**
  - **Deque** (Double-Ended Queue)

---

## **3. Non-Linear Data Structures**
These structures do not store data sequentially.

- **Trees**: Hierarchical structure with a root node and child nodes.
  - **Binary Tree**
  - **Binary Search Tree (BST)**
  - **Balanced Trees**: 
    - **AVL Tree**
    - **Red-Black Tree**
    - **B-trees** and **B+ trees**
  - **Heap**: 
    - **Min-Heap**
    - **Max-Heap**
  - **Trie (Prefix Tree)**: For efficient search of strings/prefixes.

- **Graphs**: Consists of vertices (nodes) and edges.
  - **Directed Graph (Digraph)**
  - **Undirected Graph**
  - **Weighted Graph**
  - **Cyclic/ Acyclic Graph**
  - **Sparse Graph**
  - **Dense Graph**

---

## **4. Hash-Based Data Structures**
These structures use a hash function to map keys to values.

- **Hash Table / Hash Map**: Efficient key-value pair storage.
- **Hash Set**: For storing unique elements.

---

## **5. Specialized Data Structures**
These are designed for specific use cases.

- **Matrix**: Two-dimensional array representation for data (e.g., grids, images).
- **Bloom Filter**: Probabilistic data structure for membership testing.
- **Segment Tree**: Used for range queries and updates.
- **Fenwick Tree (Binary Indexed Tree)**: For prefix sums and updates.
- **Suffix Array**: For string processing.
- **Disjoint Set (Union-Find)**: For partitioning sets and finding connected components.

---

## **6. Abstract Data Types (ADTs)**
These are theoretical models used to implement real data structures.

- **List**: Ordered collection of elements.
- **Set**: Collection of unique elements.
- **Map**: Collection of key-value pairs.
- **Deque**: Double-ended queue for both FIFO and LIFO.

---

## **7. File-Based Data Structures**
For managing and organizing data in storage systems.

- **Flat Files**
- **Indexed Files**
- **B-Trees for Databases**

---

## **8. Advanced/Hybrid Data Structures**
- **Skip List**: For fast search in sorted data.
- **Suffix Tree**: For fast pattern matching in strings.
- **Treap (Tree + Heap)**: Combines properties of binary search trees and heaps.
- **Quad Tree**: Used in spatial partitioning.
- **Octree**: For 3D partitioning in graphics/physics.

---

### **How to Choose a Data Structure**
1. **Access Pattern**: Do you need sequential, random, or hierarchical access?
2. **Mutability**: Do you need to frequently add/remove/modify elements?
3. **Search Efficiency**: Are you optimizing for faster search or compact storage?
4. **Memory Constraints**: Does the data structure fit in memory or require storage?
5. **Concurrency**: Will it be accessed by multiple threads?


The list of **data structures** with Python-specific explanations and examples:

---

### **1. Primitive Data Structures**
These are built-in data types in Python:
```python
# Integer
a = 10  # Example of an integer

# Float
b = 3.14  # Example of a float

# Boolean
c = True  # Example of a boolean

# Character (single characters are strings in Python)
d = 'A'  # Example of a character
```

---

### **2. Linear Data Structures**

#### **a. Array** (via `list`)
Python doesn’t have native arrays but uses lists for similar functionality.
```python
# Array-like list
arr = [10, 20, 30, 40]
print(arr[1])  # Access element at index 1: 20
```

For performance-critical applications, you can use `array` from the `array` module:
```python
import array
arr = array.array('i', [10, 20, 30, 40])  # Array of integers
print(arr[1])  # Access element at index 1: 20
```

---

#### **b. Linked List**  
Python doesn’t have a built-in linked list but you can implement it:
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Usage
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()  # Output: 30 -> 20 -> 10 -> None
```

---

#### **c. Stack**
Python provides stacks using `list` or `collections.deque`.
```python
stack = []  # Using list
stack.append(10)  # Push
stack.append(20)
print(stack.pop())  # Pop: 20
```

---

#### **d. Queue**
Use `collections.deque` for an efficient queue:
```python
from collections import deque
queue = deque()
queue.append(10)  # Enqueue
queue.append(20)
print(queue.popleft())  # Dequeue: 10
```

---

#### **e. Priority Queue**
Use `heapq` for priority queues:
```python
import heapq
pq = []
heapq.heappush(pq, 20)  # Push
heapq.heappush(pq, 10)
print(heapq.heappop(pq))  # Pop: 10 (lowest priority)
```

---

### **3. Non-Linear Data Structures**

#### **a. Tree**
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Binary Tree
root = Node(10)
root.left = Node(5)
root.right = Node(15)
```

#### **b. Graph**
Python doesn’t have a graph structure but uses dictionaries or lists:
```python
# Adjacency List Representation
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2]
}

# BFS Example
from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])

bfs(graph, 1)  # Output: 1 2 3 4
```

---

### **4. Hash-Based Data Structures**

#### **a. Hash Table (Dictionary)**
```python
hash_table = {}
hash_table["key1"] = "value1"
print(hash_table["key1"])  # Output: value1
```

#### **b. Hash Set**
```python
hash_set = set()
hash_set.add(10)
hash_set.add(20)
print(10 in hash_set)  # Output: True
```

---

### **5. Specialized Data Structures**

#### **a. Matrix**
```python
# 2D Matrix using lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])  # Access row 1, column 2: 6
```

#### **b. Trie**
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

# Usage
trie = Trie()
trie.insert("hello")
print(trie.search("hello"))  # Output: True
print(trie.search("world"))  # Output: False
```

---

### **6. Advanced/Hybrid Data Structures**

#### **a. Skip List**
```python
# Not built-in, install `sortedcontainers`
from sortedcontainers import SortedList
skip_list = SortedList()
skip_list.add(10)
skip_list.add(5)
print(skip_list)  # Output: [5, 10]
```

#### **b. Union-Find (Disjoint Set)**
```python
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x

# Usage
uf = UnionFind(5)
uf.union(0, 1)
print(uf.find(1))  # Output: 0
```

---
