from arrays.q01 import *
from arrays.q02 import *
# import arrays.q02 as aq02

def invoke_exit():
    print("Bye! Have a great day!")
    exit()

options = { 1 : Arr001,
            2 : Arr002,
            0 : invoke_exit
}

d = { "Arr001_desc" : Arr001.description,
      "Arr002_desc" : Arr002.description
}

# Present an options menu to solicit the user's input
while True:
    prompt = """
_______________________________

 ------- Interview Prep ------
_______________________________

Please select interview question:

Array Questions:
{Arr001_desc}
{Arr002_desc}

Algo Questions:
3) aaa
4) aaa
5) aaa
0) Exit

$Command me, baby> """.format(**d)
    choice = input(prompt)
    print()
    options[int(choice)]()

    prompt = """
Do you wish to continue?
"""
    choice = input(prompt)
