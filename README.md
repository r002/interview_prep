# interview_prep
Holds all code in my quest to prepare for technical coding interviews. Cue training montage!
Questions are from https://www.byte-by-byte.com/blog/ and Daily Interview Pro emails.


## Runner
To run:
```
C:\code\interview_prep>python -m runner
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


### Algorithms
101) Print the first ten numbers in the Fibonocci Sequence.

102) Given a linked list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time and only use constant space.


### Strings
201) Given a string, s, find the longest palindromic substring in s. `[Twitter]`
Eg. s = "tracecars" # racecar

202) Given a string, find the length of the longest substring without repeating characters. `[Microsoft]`

203) Validate Balanced Parentheses. `[Uber]`
