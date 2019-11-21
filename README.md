# interview_prep
Holds all code in my quest to prepare for technical coding interviews. Cue training montage!
Questions are from https://www.byte-by-byte.com/blog/


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
