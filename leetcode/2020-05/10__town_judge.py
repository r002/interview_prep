import unittest


class Solution:
    def findJudge(self, N:int, trust:list) -> int:
        # Manually handle edge case:
        if N==1: return 1  # If there's only one person in town; s/he trusts no
                           # one and must be the judge! The trust[] must be empty in this case.

        # The judge must be trusted by every other townsperson
        trusted_judge_candidates = {pair[1] for pair in trust}

        # The judge isn't allowed to trust anyone. This means the judge
        # can't appear in 0th position of any pair.
        people_who_trust = {pair[0] for pair in trust}

        # Filter anyone who trusts from the judge candidates pool
        trusted_judge_candidates = trusted_judge_candidates - (people_who_trust & trusted_judge_candidates)
        if len(trusted_judge_candidates) == 0:
            return -1
        elif len(trusted_judge_candidates) == 1:
            print(trusted_judge_candidates)
            judge_candidate = list(trusted_judge_candidates)[0]

            # Now check: Does every single townsperson trust the judge candidate?
            trust_pairs = [pair for pair in trust if pair[1]==judge_candidate]
            if len(trust_pairs) == N-1:
                return judge_candidate
            else:
                return -1

        print("@@@ Unhandled scenario - We shouldn't be able to get this far in the algo.. @@@")
        return -1


class Test(unittest.TestCase):
    cases = [
        (1, [], 1),  # If there's only person in the town, s/he must be the judge. 
        (5, [[1,5], [2,5], [3,5], [4,5]], 5),
        (9, [[1,5], [2,5], [3,5], [4,5]], -1),
        (2, [[1,2]], 2),
        (3, [[1,3], [2,3]], 3),
        (3, [[1,3], [2,3], [3,1]], -1),
        (3, [[1,2], [2,3]], -1),
        (4, [[1,3], [1,4], [2,3], [2,4], [4,3]], 3)
    ]
    s = Solution()

    def test0(self):
        for N, trust, expected in self.cases:
            result = self.s.findJudge(N, trust)
            print(f"{N} | {trust} | {result} | {expected}")
            print("---")
            self.assertEqual(result, expected)


unittest.main()
