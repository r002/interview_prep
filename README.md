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
001) No notes.

002) list.sort() in Python naturally sorts in ascending order.

### Algorithms
101) Print the first ten numbers in the Fibonocci Sequence.


### Strings
201) Given a string, s, find the longest palindromic substring in s.
Eg. s = "tracecars" # racecar

202) Given a string, find the length of the longest substring without repeating characters.

203) Validate Balanced Parentheses.
