from collections import deque, defaultdict, OrderedDict, namedtuple, ChainMap, Counter
import heapq

#################################################################################################### 1. Deque (Double-ended Queue)
print("1. Deque (Double-ended Queue)")
dq = deque([1, 2, 3])
dq.append(4)         # Adds 4 to the right end
dq.appendleft(0)     # Adds 0 to the left end
print("Deque:", dq)
print("Rightmost element (pop):", dq.pop())        # Removes and returns the rightmost element (4)
print("Leftmost element (popleft):", dq.popleft())  # Removes and returns the leftmost element (0)
print()

#################################################################################################### 2. Heapq (Heap Queue)
print("2. Heapq (Heap Queue)")
heap = [3, 2, 5, 1, 4]
heapq.heapify(heap)        # Convert list into a heap
heapq.heappush(heap, 0)    # Push item onto heap
print("Heap:", heap)
print("Smallest item (pop):", heapq.heappop(heap))  # Pop and return the smallest item from the heap
print()

#################################################################################################### 3. OrderedDict
print("3. OrderedDict")
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
print("OrderedDict:", ordered_dict)
print()

#################################################################################################### 4. DefaultDict
print("4. DefaultDict")
d = defaultdict(int)
d['a'] += 1  # No KeyError even if 'a' is not in the dictionary
print("DefaultDict:", d)
print()

#################################################################################################### 5. NamedTuple
print("5. NamedTuple")
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print("NamedTuple:", p)
print("Accessing elements - x:", p.x, "y:", p.y)
print()

#################################################################################################### 6. ChainMap
print("6. ChainMap")
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
combined_dict = ChainMap(dict1, dict2)
print("ChainMap:", combined_dict)
print()

#################################################################################################### 7. Counter
print("7. Counter")
cnt = Counter([1, 2, 1, 3, 2, 1, 1])
print("Counter:", cnt)
print()

# Additional operations or usage examples can be added as needed for each data structure
