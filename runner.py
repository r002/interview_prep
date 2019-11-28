from arrays.q001 import *
from arrays.q002 import *
from arrays.q003 import *
from arrays.q004 import *
from algos.q101 import *
from strings.q201 import *
from strings.q202 import *
from strings.q203 import *
# import arrays.q02 as aq02

def invoke_exit():
    print("Bye! Have a great day!")
    exit()

options = { 1 : Arr001,
            2 : Arr002,
            3 : Arr003,
            4 : Arr004,
            101 : Algo101,
            201 : Str201,
            202 : Str202,
            203 : Str203,
            0 : invoke_exit
}

d = { "Arr001_desc" : Arr001.description,
      "Arr002_desc" : Arr002.description,
      "Arr003_desc" : Arr003.description,
      "Arr004_desc" : Arr004.description,
      "Algo101_desc" : Algo101.description,
      "Str201_desc" : Str201.description,
      "Str202_desc" : Str202.description,
      "Str203_desc" : Str203.description
}

# Present an options menu to solicit the user's input
while True:
    prompt = """
_______________________________

 ------- Interview Prep ------
_______________________________

Please select interview category:

Array Questions:
{Arr001_desc}
{Arr002_desc}
{Arr003_desc}
{Arr004_desc}

Algo Questions:
{Algo101_desc}

String Questions:
{Str201_desc}
{Str202_desc}
{Str203_desc}

0) Exit

$Command me, baby> """.format(**d)
    choice = input(prompt)
    print()
    options[int(choice)]()

    prompt = """
Do you wish to continue?
"""
    choice = input(prompt)
