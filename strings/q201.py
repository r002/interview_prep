from base.question import *

class Str201(Question):

    description = "201) Given a string, s, find the longest palindromic substring in s."
    i = 0  # Number of iterations my solution takes

    def __init__(self):
        # s = 'racecar'
        # s = 'tracecars'
        # s = 'ab'
        # s = 'abcbgh'
        s = 'abcabcabcqqqzzmzzabcd'
        # s = 'cabcabcqqq'
        # s = ''

        print(f"Original string: {s}")
        print(f"Original length: {len(s)}")
        print(f"Worst-case O(n) should be ~ n*(n/2): {len(s)*(len(s)/2)}\n")
        p_cand = s
        champ = ''

        while True:
            print(f"This iteration's candidate: {p_cand}")

            if len(p_cand) <= len(champ):
                print(f"Since len(p_cand) <= len(champ), we can just quit!")
                break

            it_cand = self.check_if_any_exist(p_cand)
            if len(it_cand) > len(champ):
                print(f"\t\tNew champ! {it_cand}")
                champ = it_cand

            # Code the exit condition
            if len(p_cand) < 2:
                break
            else:
                p_cand = p_cand[1:]

        print(f"\nFinal Champ: {champ}")
        print(f"Total iterations: {self.i}")


    def check_if_any_exist(self, p_cand):
        while True:
            self.i += 1
            if p_cand == p_cand[::-1]:
                print(f"\tPalindrome found! {p_cand}")
                return p_cand
            else:
                p_cand = p_cand[:-1]
