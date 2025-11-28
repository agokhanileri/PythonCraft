## Description
Structured Python path built with a focus on comprehension and clarity.

Already fluent in Python and want to skip to the fun part? 👉 [LeetCode](./leetcode/README.md)

### Tutorial
| #  | Script                                         | Rigidity| Status| Lint | Topics                                                                             |
|----|------------------------------------------------|:-------- |:----:|:----:|------------------------------------------------------------------------------------|
| 01 | [Syntax](./tutorial/syntax.py)                 |Soft     | ✅    | ✅   | Zen, Docstrings, Imports, Comments, Indents, Quotes, Spacing, Namespaces, Encoding |
| 02 | [Scalars](./tutorial/scalars.py)               |Soft     | ✅    | ✅   | Numbers, Boolean, Strings, Arithmetic 👉 [MathCraft]() for more (hidden, TBD)      |
| 03 | [Containers](./tutorial/containers.py)         |Soft     | ✅    | ✅   | Lists, Tuples, Sets, Dictionary, Stacks/Queues, Collections, Arrays                |
| 04 | [Loops](./tutorial/loops.py)                   |Soft     | ⚠️    | ❌   | If, For, While, Case, Continue/Break/Pass, Iterables                               |
| 05 | [Functions](./tutorial/functions.py)           |Soft     | ⚠️    | ❌   | Function, Partial, OperatorOverloading, Generator, Coroutines                      |
| 06 | [Interactive](./tutorial/interactive.py)       |Soft     | ⚠️    | ❌   | Printing, PrettyPrint, Prompting, FileHandling, ContextManagers                    |
| 07 | [Classes](./tutorial/classes.py)               |Soft     | ⚠️    | ❌   | Classes, Variables, Decorators                                                     |
| 08 | [OOP](./tutorial/object_oriented.py)           |Med      | ⚠️    | ❌   | Inheritance, Abstraction, Polymorphism, Encapsulation                              |
| 09 | [LinkedLists](./tutorial/linked_lists.py)      |Med      | ⚠️    | ❌   | Implementation, Traversals, Insert/Delete, Reverse, Circular Lists                 |
| 10 | [BinaryTrees](./tutorial/binary_trees.py)      |Med      | ⚠️    | ❌   | Implementation, Traversals (in/pre/post), Height/Balance, Views                    |
| 11 | [HeapsTries](./tutorial/heaps_tries.py)        |Med      | ⚠️    | ❌   | Min/Max, PriorityQueues, Tries, Insert/Search                                      |
| 12 | [Hashing](./tutorial/hashing.py)               |Med      | ⚠️    | ❌   | Stack Construction/Ops, Queue Construction/Ops                                     |
| 13 | [Graphs](./tutorial/graphs.py)                 |Med      | ⚠️    | ❌   | Stack Construction/Ops, Queue Construction/Ops                                     |
| 14 | [SearchAlgos](./tutorial/search_algos.py)      |Med      | ✅    | ❌   | LinearSearch, BinarySearch, JumpSearch, InterpolationSearch                        |
| 15 | [SortAlgos](./tutorial/sort_algos.py)          |Med      | ✅    | ❌   | Bubble, Quick, Merge, Insertio, Selection, Heap, Counting, Radix, Bucket           |
| 16 | [Divide&Conquer](./tutorial/divide_conquer.py) |Med      | ❌    | ❌   |           |
| 17 | [GreedyAlgos](./tutorial/greedy_algos.py)      |Med      | ❌    | ❌   |           |
| 18 | [DynamicAlgos](./tutorial/dynamic_algos.py)    |Med      | ❌    | ❌   |           |
| 19 | [GraphAlgos](./tutorial/graph_algos.py)        |Firm     | ❌    | ❌   |           |
| 20 | [Testing](./tutorial/testing.py)               |Firm     | ❌    | ❌   |           |
| 21 | [BitOps](./tutorial/bit_ops.py)                |Firm     | ❌    | ❌   |           |
| 21 | [AdvancedTopics](./tutorial/advanced_topics.py)|Firm     | ❌    | ❌   |           |
| HS | [HelperScripts](./extras/helper_scripts.py)    |n/a      | ✅    | ❌   | Searches, Sorts, LL, BT, Graph, Methods (clear_all, cmp)                           |
| PS | [PracticeSoft](./extras/practice_soft.py)      |Soft     | ⚠️    | ❌   | Soft practice questions                                                            |
| PM | [PracticeMed](./extras/practice_medium.py)     |Med      | ⚠️    | ❌   | Medium practice questions                                                          |
| LC | [LeetCode](./leetcode/README.md)               |Soft/Med | ✅    | ---  | Leetcode solutions with comments and testing                                       |

###
## Manual

<b>Style:</b> Focus is comprehension and clarity
* Follows Zen style and Ruff formatting.
* Indented for line-by-line execution, although full run might work for some.
* Whitespaces are minimized for better focus and easier scrolling.
* Relevant lines are grouped together as much as possible.
* Printing ommited most of the time.

<b>Requirements:</b>
* Python: version 3.12
* Dependencies: None, except basic CI/CD packages for linting
* CI/CD: ruff, black, mypy, pytest, pre-commit
* I/O: Input/Outputs for all scripts are ./inputs and ./outputs respectively.
* Extras: Helper scripts (/helper_scripts.py) and scratch notes (random_notes.py)


###
Helper classes/methods are utilized in problems:
  * Class import: ``` from helper_scripts import BinaryTree ```
  * Method import: ``` from helper_scripts import * quick_sort```

###
<u>Shortcuts used:</u> <br>
<pre>
Q = Question
DS = Data Structures
BT = Binary Tree, LL = Linked List,
sol = solution, mod = modification, ans = answer, iter = iterate, concat =
concatenate, lib = library, func = function,
</pre>


## License
This project is licensed under the BSD 3-Clause License.
