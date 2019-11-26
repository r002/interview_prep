from base.question import *

class Str202(Question):

    description = "202) Given a string, find the length of the longest substring without repeating characters."

    def __init__(self):
        s = 'abrkaabcdefghijjxxx'

        print(f"Original string: {s}")

        i = 0
        rs = "a"
        champ = rs
        while i < len(s)-1:
            if s[i+1] != s[i]:
                rs += s[i+1]
                print(f"rs: {rs}")
            else:
                if len(rs)>len(champ):
                    champ = rs
                    print(f"New champ! {champ}")
                rs = s[i+1]
            i += 1

        print(f"Champ: {champ}")
        print(f"Champ length: {len(champ)}")
