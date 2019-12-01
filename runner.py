import importlib
import os

# From: https://stackoverflow.com/questions/10043485/python-import-every-module-from-a-folder
def import_package(package_name):
    for name in os.listdir(package_name):
        if name.endswith(".py"):
            module = name[:-3] #strip the extension
            # set the module name in the current global name space:
            globals()[module] = importlib.import_module(package_name + "." + module)

import_package("algos")
import_package("arrays")
import_package("strings")

def invoke_exit():
    print("Bye! Have a great day!")
    exit()

options = { 1 : q001.Arr001,
            2 : q002.Arr002,
            3 : q003.Arr003,
            4 : q004.Arr004,
            101 : q101.Algo101,
            102 : q102.Algo102,
            103 : q103.Algo103,
            104 : q104.Algo104,
            105 : q105.Algo105,
            106 : q106.Algo106,
            201 : q201.Str201,
            202 : q202.Str202,
            203 : q203.Str203,
            0 : invoke_exit
}

# Present an options menu to solicit the user's input
while True:
    prompt = f"""
_______________________________

 ------- Interview Prep ------
_______________________________

Please select interview category:

Array Questions:
{q001.Arr001.description}
{q002.Arr002.description}
{q003.Arr003.description}
{q004.Arr004.description}

Algo Questions:
{q101.Algo101.description}
{q102.Algo102.description}
{q103.Algo103.description}
{q104.Algo104.description}
{q105.Algo105.description}
{q106.Algo106.description}

String Questions:
{q201.Str201.description}
{q202.Str202.description}
{q203.Str203.description}

0) Exit

$Command me, baby> """
    choice = input(prompt)
    print()
    options[int(choice)]()

    prompt = """
Do you wish to continue?
"""
    choice = input(prompt)
