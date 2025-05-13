
# ! In Python, everything is an object, and variables are references (why integers don't overflow like usual)

#! Immutables in python: numbers,str,tuples, bool, frozenset
# ! Mutables: list,dict,set,custom classes (usually)

# ! Immutables like the tuple can still hold mutable elements

#! Python naming conventions: lower_case_snake_case for varaible names, CAPITAL_SNAKECASE for constants, CapitalPascalCase for Classes

# ! Since everything is an object in python, all variables are heap allocated unlike languages like C. The stack is used to track which funtions to call along with when and where to call those functions. Different from compiled languages like C. Due to this, declaring new variables inside something like a for loop just reasigns the pointer of the local variable from the previous iteration of the for loop, so the cost is neglible. Whereas in complied languages like C, new stack frame is allocated and dellocated on the stack for the local variable for each iteration of the for loop.

# ! Stack in python is used to manage function frames. A function frame contains a dictionary or array of pointers to heap objects (NOT the objects themselves), (all variable's data is heap allocated in python since everything in python is an object). Function frames also contain things like return adresses, function arguments, etc. Thus python pushes/pops these function frames at runtime.

# ! C stack (simple):
# ┌──────────────────────────────┐
# │ Local variable: result        │
# │ Function argument: b          │
# │ Function argument: a          │
# │ Saved frame pointer (rbp)     │
# │ Return address (instruction)  │
# └──────────────────────────────┘

# ! Python stack frames (complex) = full runtime environments for each function call
# Python Frame (Top of Stack):
# ┌──────────────────────────────────┐
# │ Operand Stack (temporary values) │
# │ Block Stack (try/except/loops)    │
# │ Locals mapping: {'a': 3, 'b': 4, 'result': 7} │
# │ Globals mapping                  │
# │ Builtins mapping                 │
# │ Code Object (compiled bytecode)  │
# │ Current instruction pointer      │
# │ Previous frame pointer (caller)  │
# └──────────────────────────────────┘

# ! Immutables are thus important in python to 1) Save memory on the heap by variables pointing to existing data on the heap instead of creating/editing new data, these must be immutable so that one variable changing does not affect another


# variables in python are dynamically typed and determined at runtime
n = 0
print("n =" , n)

n = "abc"
print("n = ", n)


#multiple assignments
n,m = 0, "abc"
print(n, "  ", m)


#Increment, note: cant do n++ in python
n += 1


# Null is None in python (Null/None is the absence of a value)
n = 4
n = None

print(n)

#If statements
n = 13

if n > 2:
    n -=1 
elif n == 2:
    n += 1
else:
    n = 3

print(n)


# and = &&   ,  or = ||
n,m = 3,4

# multi-line if statements and while loops need those outer parentheses
if ((n > 2) 
    and ( n>3 or n==4)):
    print(n)


#While loops
while n < 5:
    n *= -10

 
#for loops , key point: the end point is NOT included

#goes from 0 t0 4
for i in range(5):
    print(i)

#goes from 2 to 5
for i in range(2,6):
    print(i)


# goes from 0 to 10, printing every second value
for i in range(1,11,2):
    print(i)

#goes from 5 to 0, note reverse order
for i in range(5,-1, -1):
    print(i)


#Division gives a float by default
print(5/2)

#double slash round DOWN ( floor division)
print(5//2)

# note will give -2 instead of -1, -2 is smaller than -1 and (floor division mathematically rounds towards -Infinity)
print(-3//2) # ----> -2


# Instead can use int() which cuts off the decimal
print(int(-3/2)) # ----> -1


# Modulus
print(10 % 3)

#behaves a bit weird with negative numbers
print(-10 % 3)  # -----> returns 2 not 1, how many times 3 goes to make 10 from -10,  and what is left over after

# if wanting to get -1 instead like in other programming languages, use fmod from math
import math
print(math.fmod(-10,3))

# more math
import math

print(math.floor(3/2))
print(math.ceil(3/2))
print(math.sqrt(2))
print(math.pow(2,3))


#Python integers cannot overflow like typical 32 bit integers (limited by memory only)
n = 10
n = 10 ** 1000;
print(n)
print(type(n)) 

#Python floats can though
# import math
# print(math.pow(2,10000))

#So use float("inf"), float("-inf") to check if they are really big or really small
#note ints are casted to floats for comparisons with an int vs float
print(math.pow(2,100) < float("inf"))


#use math.isclose() to compare floating point numbers
print(math.isclose(3.0,3.000000000000000001))


#Lists (dynamic arrays called lists in python), they are dynamic in size in python, they can also store heterogenous elements,
#! Lists in python are implemented as dynamic arrays, the list starts with some fixed allocated memory and double the space when it needs more
# Index Acess = O(1)
# Append = O(1) amortized ( python doubles the size of list so eventually it will be so large it is just constant time to append)
# Inserting: O(n)
# Removing from end: O(1)
# Removing from middle (including start): O(n)
# Searching for particular element: O(n)

arr = [1,2,3, "a", "b", "c"]

arr.append("d")
print(arr)

# pop removes from a specified index in the list, leave empty for default removal from the end of the list
arr.pop()

#negative indexes in python start from the end of the iterable, -1 is for the last element in the iterable, -2 for second last, etc.
arr.pop(-1)
print(arr)

# insert an element to now be at the specified index
arr.insert(1, 0)
print(arr)


# can use multiplication with lists
arr = [1,2] * 5
print(arr)
 

# Sublists, similar to for loops, end index is not inclusive
arr = [1,2,3,4]
print(arr[1:3])   #---> [2,3] does not include index 3

# Unpacking, has to have same number of variables as size of array
a,b,c = [1,2,3]

# can use * for extended unpacking, now don't need to have same number of variables as the size of the array
a, *b , c = [1,2,3,4,5,6]
print(b)

# Loop through lists
nums = [1,2,3]

# element wise
for n in nums:
    print(n)


#enumerate gives a tuple of the index and element of a list 
for idx,num in enumerate(nums):
    print(f"Index is {idx}, number is: {num}")


# loop through two arrays simultaneously
nums1 = [1,3,5]
nums2 = [2,4,6,7]

# using zip, will produce a tuple of elements from both arrays simultaneosly, zip stops at the shortest list
for n1,n2 in zip(nums1,nums2):
    print(n1,n2)

# reverse an array
nums = [1,2,3]
nums.reverse()

print(nums)


# sorting an array of ONLY numbers, defaults to ascending order, uses >,< behind the hood so be wary with floats
arr = [1,3,6,4,9,10,1]
arr.sort()

print(arr)

#sort in reverse order
arr.sort(reverse=True)

print(arr)

#sorting strings, sorts by alphabetical order
arr = ["zetsuyama", "bob", "alice", ]
arr.sort()

print(arr)

#Custom sort (by length of string), sorts by ascending order of keys , can use reverse here
arr.sort(key = lambda x: len(x))

print(arr)

# List comprehension, (python quick way to make lists)
arr = [i for i in range(5)]
print(arr)

arr = [2 * i for i in range(5)]
print(arr)


# 2-D list comprehension
arr = [[0] * 4 for i in range(4)]
print(arr)

#! This doesn't work as expected, shallow copy, i.e: changing a row will affect all others, [0] is an immutable here before being assigned, why is works. (note: when changing immutables, new memory adress is created for variable)
arr = [[0] * 4] * 4

#Strings are similar to Arrays but immutable
s = "abc"
print(s[0:2])

# wrong, strings are immutable
# s[0] = "z"

# correct way
s += "zbc"   
print(s)

# can convert strings to numbers
string_to_num = int("123")
print(f"Value: {string_to_num}, Type = {type(string_to_num)}")


#can convert numbers to strings
num_to_string = str(123)
print(f"Value: {num_to_string}, Type = {type(num_to_string)}")


# can get ASCII value of a character using ord
print(ord("a"))

# can get the char from integer/ascii value using chr
print(chr(ord("a")))

# Remove leading/trailing spaces
s = "    hello world     "
new_s = s.strip()
print(new_s)      

# replace characters in a string
s = "hello world"
new_s = s.replace("l", "x")  
print(new_s)   # ----> hexxo worxd

# can seperate a string by a delimiter
string = "ab.cd.ed.gh.ij"
strings = string.split(".") 
print(strings)

# can join a list of strings with a delimiter
strings = ["ab", "cd", "ef", "gh", "ij"]
print(" delimiter ".join(strings))

# can slice strings using this notation s[start:stop:step], returns a new string since strings are immutable, stop is not included like in for loops
s = "asdas"
s_new = s[0:2:1]
print(s_new)

# including the whole string
s_new = s[::1]
print(s_new)

# reversing the string
s_new = s[::-1]
print(s_new)


# Check if all chars are digits
print(s.isdigit())

# Check if all chars are alphabetical
print(s.isalpha())

#Check if all chars are either digits or alphabetical
print(s.isalnum())

#Check is all chars are whitespace
print(s.isspace())


#Queues (double ended queue) , implemented using double linked list or circular buffer in python
# append (right or left): O(1)
# pop (right or left): O(1)
# peek (right or left): O(1)
# Search: O(n)

from collections import deque

queue = deque()

queue.append(3)
queue.append(4)
queue.appendleft(2)
queue.appendleft(1)

# note the pop here does not take an index like in regular lists
queue.pop()
queue.popleft()

# peek from front of queue, maximum value in a max heap, minimum value in a min heap
print(queue[0])

# peek the back of queue, doesn't really say much in a heap
print(queue[-1])

print(queue)

 
# ! Hashset (contain time lookup and insertion) , also cannot contain any duplicates since it is a set,  keys must be immutable (important for hashtable algorithm)
# insert : average O(1)
# remove: average O(1)
# lookup: average O(1)

mySet = set()

mySet.add(1)
mySet.add(2)
mySet.add(3)
mySet.add("ad")

print(mySet)
print(len(mySet))

# can use in to check if values are inside a Hashset
print(1 in mySet)
print(3 in mySet)

# can remove values from Hashset
mySet.remove(3)
print(3 in mySet)

#Set comprehension, (use {} instead of [] braces), be careful if not using set comprehension and just use {}, get a dictionary instead
mySet = {i for i in range(5)}
print(mySet)


# ! Hashmap (aka Dictionary in python) , cannot have duplicate keys, keys must be immutable (imporant in context of hashtable algorithm), (operations time complexities are for keys not values)
# insert : average O(1)
# remove: average O(1)
# lookup: average O(1)
# iterate over keys/ items() : O(n) (where n is the amount of data inserted into the Hash Map , not the size of the Hash Map itself)

myMap = {}
myMap["jimmy"] = 88
myMap["bob"] = 89

print(myMap)
print(len(myMap))

# modify/insert Hashmap
myMap["alice"] = 8
myMap["jimmy"] = 91
print(myMap)

# check if key in Hashmap
print("alice" in myMap)

# pop from Hashmap
popped_value = myMap.pop("alice") 
print("alice" in myMap)

# Dict comprehension
newMap = {i : 2*i for i in range(5)}
print(newMap)

# looping from Hashmaps
myMap = {"cookie" : 1, "twoCookie": 2, "threeCookie": 3}

for key in myMap:
    print(f"Key: {key}, Value: {myMap[key]}")

# looping through hashmap values
for val in myMap.values():
    print(f"Value is {val}")

# loop for key and value at same time
for key,val in myMap.items():
    print(f"Key: {key}, Value: {val}")

# Can also use defaultdict to initialize empty values in a dictionary
from collections import defaultdict

list_defaultdict = defaultdict(list)

list_defaultdict["hi"].append("hello") # ----> No error on append since the default element is a list

# Can use .get() to also return default items on Hash Map lookups
new_dict = {}
default_value = new_dict.get("random key", 0)

print(default_value)


# Tuples are like arrays but are immutable
tup = (1,2,3,4)

print(tup[2])
print(len(tup))

# Since tuples are immutable, can use as keys for a Hashmap
myMap = {(1,2): 4}

for key in myMap:
    print(f"Key is: {key}, Value is: {myMap[key]}")

# Searching the hashMap
print((1,2) in myMap)

# can use .get() to return a specified default value if the key is not yet in the hashMap instead of causing a Key Error
myMap = {"first": 1}

print(myMap.get("second", "second is not yet in table"))


#! Heaps, are Lists under the hood, heapq just provides algorithms to operate on the List like a heap, heaps are minHeaps by default in python, heaps are not BST. They are like BST but they don't have an inherent order. In BST: left < root < right , but in Min Heaps: parent just has to be smaller than children. 

# minHeap
# O(1) to get smallest value       
# O(logn) for insert
# O(logn) for delete
# O(n) for search for arbitary value

#BST, (usually implemented using a linked list)
# O(logn) to get smallest value       
# O(logn) for insert
# O(logn) for delete
# O(logn) for search for arbitary value

import heapq

minHeap = []

heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

# since minHeap, Min is always at 0
print(minHeap[0])

while len(minHeap):
    # pops the smallest item off the heap
    print(heapq.heappop(minHeap))

# No max Heaps in python but can get around by multiplying by -1 when pushing onto heap and multiplying by -1 when poppigng out

import heapq

maxHeap = []

# create a max heap of 3,2,4
heapq.heappush(maxHeap,-3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

# notice the negative when returning values in a maxHeap
for i in maxHeap:
    print(-i)

# pop and return largest element, notice the negartive when returning values in a maxHeap
minElements = -maxHeap[0]

print(minElements)

# Build heap from initial values in O(n)
import heapq

arr = [1,4,7,3,8,3,9,2,10]


# ! Can use "if" to check if regular container is empty in python (list, tuple, str, dict,set...)
while arr:
    print(heapq.heappop(arr))


#  Note: containers are different from iterables in python, all containers are iterables but not all iterables are container


# Functions
#  those int,float,bool on the myFunc function signature are type hints which don't affect how the program runs, they are mean for code clarity and to help IDE
# properly handle the code
def myFunc (a: int,b:float) -> bool:
    return a*b

print(myFunc(1,2)) 

# Nested functions
# ! functions have closures in python, inner() function holds a reference to all local variables of the outer function
def outer(a,b):

    c = "c"
    print(id(c))

    def inner():
        print(id(c))
        return a + b + c

    return inner()

print(outer("a", "b"))

# id() is used to check identity of an object. Returns Different values even though several variables reference the same value, but the references are different


# ! Since immutables are reassigned when the value changes, cannot simply change the value of an outer function immutable variable from within an inner function, (remember variables passed by reference from outer to inner function), use "non local" keyword to make possible
def outer():
    count = 0  # Variable in the enclosing scope

    def inner():
        nonlocal count  # Refers to the variable 'count' in the outer function
        count += 1  # Modify the 'count' variable from the outer scope
        print(count)

    inner()

outer()

# copying 
import copy

list = [1,2,3,[4,5]]

shallow_copy = copy.copy(list)

# notice that copy is shallow, shallow_copy list was changed
list[-1][0] = 1
print(shallow_copy[-1][0])


# deep copy
deep_copy = copy.deepcopy(list)

for i,val in enumerate(deep_copy):
    print(f"Index: {i}, Value: {val}")



# Classes, naming convention is to start with a capital for class names
class MyClass:
    # Constructor, notice how self is required to be passed in as the first argument for all class methods (static methods excluded), python automatically passes in the class instance as the first argument to all class methods on class method calls
    def __init__(self, nums):
        self.nums = nums
        self.size = len(nums)

    # notice how self is required to be passed in first for all class methods (static methods excluded)
    def getLength(self):
        return self.size
    

my_class_instance = MyClass([1,2,3])


# Equality
         
# == checks value equality, is checks object equality

a = [1, 2]
b = a
c = [1, 2]

# print(a == c)  # ---> True: contents are equal
# print(a is c)  # ---> False: different objects
# print(a is b)  # ---> True: same object in memory



hashMap = {"a": 32}

print("as" in hashMap)