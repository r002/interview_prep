# interview_prep
Holds all code in my quest to prepare for technical coding interviews. Cue training montage!
Questions are from https://www.byte-by-byte.com/blog/ and Daily Interview Pro emails.


## Runner
To run:
```
C:\code\interview_prep> python -m runner
C:\code\interview_prep> light-server -s . -p 7000 -w "web/*"
```


## REPL Notes
```
from importlib import reload
import questions.array_questions as qaq
aq = qaq.ArrayQuestions
reload(qaq)
aq = qaq.ArrayQuestions  # Reassign the alias to refresh the reference
```

## Notes
### Arrays
001) Find the mean of the medians of two sorted arrays.

002) Find the median of two sorted arrays. (list.sort() in Python naturally sorts in ascending order.)

003) Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a target element, x. Return -1 if the target is not found. `[Airbnb]`

004) Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time. Bonus: Use constant space. `[Google]`

005) You are given an array of integers in an arbitrary order. Return whether or not it is possible to make the array non-decreasing by modifying at most 1 element to any value. We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n). `[Microsoft]`


### Algorithms
101) Print the first ten numbers in the Fibonocci Sequence.

102) Given a linked list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time and only use constant space.

103) Given a singly-linked list, reverse the list. This can be done iteratively or recursively. Can you get both solutions?  `[Google]`

104) Convert a list to a doubly linked list.

105) Reverse a singly linked list into a doubly linked list.


### Strings
201) Given a string, s, find the longest palindromic substring in s. `[Twitter]`
Eg. s = "tracecars" # racecar

202) Given a string, find the length of the longest substring without repeating characters. `[Microsoft]`

203) Validate Balanced Parentheses. `[Uber]`
