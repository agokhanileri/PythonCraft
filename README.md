## Description
![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![License](https://img.shields.io/badge/license-BSD--3--Clause-lightgrey.svg)
![Lint](https://img.shields.io/badge/lint-Ruff-black.svg)

Structured Python learning path with exercises and LeetCode solutions.<br>

_Skip the boring tutorial and go for the fun?_ 👉 [Jump to LeetCode](./leetcode/README.md)<br>

### Tutorial
| #  | Script                                         | Rigidity| Status| Lint | Topics                                                                             |
|----|------------------------------------------------|:-------- |:----:|:----:|------------------------------------------------------------------------------------|
| 01 | [Syntax](./tutorial/syntax.py)                 |Soft     | ✅    | ✅   | Zen, Docstrings, Imports, Comments, Indents, Quotes, Spacing, Namespaces, Encoding |
| 02 | [Scalars](./tutorial/scalars.py)               |Soft     | ✅    | ✅   | Numbers, Boolean, Strings, Arithmetic _for more_ 👉 [MathCraft (TBD)]()            |
| 03 | [Containers](./tutorial/containers.py)         |Soft     | ✅    | ✅   | Lists, Tuples, Sets, Dictionary, Stacks/Queues, Collections, Arrays                |
| 04 | [Loops](./tutorial/loops.py)                   |Soft     | ⚠️    | ❌   | If, For, While, Case, Continue/Break/Pass, Iterables                               |
| 05 | [Functions](./tutorial/functions.py)           |Soft     | ⚠️    | ❌   | Function, Partial, OperatorOverloading, Generator, Coroutines                      |
| 06 | [Interactive](./tutorial/interactive.py)       |Soft     | ⚠️    | ❌   | Printing, PrettyPrint, Prompting, FileHandling, ContextManagers                    |
| 07 | [Classes](./tutorial/classes.py)               |Soft     | ⚠️    | ❌   | Classes, Variables, Decorators                                                     |
| 08 | [OOP](./tutorial/object_oriented.py)           |Med      | ⚠️    | ❌   | Inheritance, Abstraction, Polymorphism, Encapsulation                              |
| 09 | [LinkedLists](./tutorial/linked_lists.py)      |Med      | ⚠️    | ❌   | Implementation, Traversals, Insert/Delete, Reverse, Circular Lists                 |
| 10 | [BinaryTrees](./tutorial/binary_trees.py)      |Med      | ⚠️    | ❌   | Implementation, Traversals (in/pre/post), Height/Balance, Views                    |
| 11 | [HeapsTries](./tutorial/heaps_tries.py)        |Med      | ⚠️    | ❌   | Min/Max, PriorityQueues, Tries, Insert/Search                                      |
| 12 | [Hashing](./tutorial/hashing.py)               |Med      | ⚠️    | ❌   | Construction, Ops, Collision                                                       |
| 13 | [Graphs](./tutorial/graphs.py)                 |Med      | ⚠️    | ❌   | Construction, Ops, Traversal (BFS/DFS)                                             |
| 14 | [SearchAlgos](./tutorial/search_algos.py)      |Med      | ✅    | ❌   | LinearSearch, BinarySearch, JumpSearch, InterpolationSearch                        |
| 15 | [SortAlgos](./tutorial/sort_algos.py)          |Med      | ✅    | ❌   | Bubble, Quick, Merge, Insertio, Selection, Heap, Counting, Radix, Bucket           |
| 16 | [Divide&Conquer](./tutorial/divide_conquer.py) |Med      | ❌    | ❌   | Strassen, Closest Pair                                                             |
| 17 | [GreedyAlgos](./tutorial/greedy_algos.py)      |Med      | ❌    | ❌   |                                          |
| 18 | [DynamicAlgos](./tutorial/dynamic_algos.py)    |Med      | ❌    | ❌   | Recursion, Memoization, Tabulation, 2-Pointer, Knapsack, LIS                       |
| 19 | [GraphAlgos](./tutorial/graph_algos.py)        |Firm     | ❌    | ❌   | Dijkstra, BellmanFord, TopologicalSort, UnionFind, FloydWarshall                   |
| 20 | [Testing](./tutorial/testing.py)               |Firm     | ❌    | ❌   | Exceptions (Assert, Try/Except/Finally), Date/Time/Calendar, Speed, Space Logging  |
| 21 | [BitOps](./tutorial/bit_ops.py)                |Firm     | ❌    | ❌   | Boolean Ops, Bitwise Ops, Bit Math, Bit Shifting, Bit Casting                      |
| 21 | [AdvancedTopics](./tutorial/advanced_topics.py)|Firm     | ❌    | ❌   | Mutation/Override, Zip, Map/Reduc/Struct, Itertools, Fraction, RegEx               |
| HS | [HelperScripts](./extras/helper_scripts.py)    |n/a      | ✅    | ❌   | Searches, Sorts, LL, BT, Graph, Methods (clear_all, cmp)                           |
| PS | [PracticeSoft](./extras/practice_soft.py)      |Soft     | ⚠️    | ❌   | Soft practice questions                                                            |
| PM | [PracticeMed](./extras/practice_medium.py)     |Med      | ⚠️    | ❌   | Medium practice questions                                                          |
| LC | [LeetCode](./leetcode/README.md)               |Soft/Med | ✅    | ---  | Leetcode solutions with comments and testing                                       |


## Manual
### Style
Philosopy: Pythonic | Zen<br>
\- Relevant lines are grouped together as much as possible.<br>

Linter: ruff<br>
Formatter: black<br>

Execution: line-by-line<br>
\- Although some scripts may run directly.<br>

### Dependencies
Python: v3.12

Packages: None

CI/CD: ruff, black, mypy, pytest, pre-commit

### Structure
Inputs: ./inputs (common for all scripts)<br>
Outputs: ./outputs //<br>

Scratch:</b> ./extras/random_notes.py<br>

Helpers: ./extras/helper_scripts.py<br>
\- Class recall: ```from helper_scripts import BinaryTree```<br>
\- Method recall: ```from helper_scripts import * quick_sort```<br>

### Shortcuts:
<pre>
DS = data structures
BT = binary tree
LL = linked list
Q = question
sol = solution
mod = modification
ans = answer
iter = iterate
concat = concatenate
lib = library
func = function
</pre>

## License
This project is licensed under the BSD 3-Clause License.
