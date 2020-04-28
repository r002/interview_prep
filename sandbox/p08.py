# 1. Extract second largest number
# 2. Find difference between two lists

import unittest
from collections import Counter

def extract_lg(l:list)->int:
    l = list(set(l))
    if len(l) < 2:
        return False
    else:
        l.sort()
        return l[-2]


def find_diff_set(gen_lst:list, rem_lst:list)->list:
    gen_lst[:] = list(set(gen_lst))
    gen_lst[:] = [item for item in gen_lst if item not in rem_lst]
    return gen_lst


def find_diff(gen_lst:list, rem_lst:list)->list:
    for item in rem_lst:
        if item in gen_lst:
            gen_lst.remove(item)
    return gen_lst


class Test(unittest.TestCase):
    '''Test Cases'''
    t00 = [
            ([1, 2, 3], 2),
            ([1, 2, 2, 4, 5], 4),
            ([], False)
    ]
    t01 = [
            ([1,2,3,4,5], [1,3,5], [2,4]),
            ([1,2,3,3,4,5], [1,3,5], [2,4]),
    ]
    t02 = [
            ([1,2,3,3,3,3,4,5], [9,1,3,3,5], [2,3,3,4])
    ]

    def test_q0(self):
        for test_case, result in self.t00:
            actual = extract_lg(test_case)
            self.assertEqual(actual, result)

    def test_q1(self):
        for gen_lst, rem_lst, result in self.t01:
            actual = find_diff_set(gen_lst, rem_lst)
            self.assertEqual(actual, result)

    def test_q2(self):
        for gen_lst, rem_lst, result in self.t02:
            actual = find_diff(gen_lst, rem_lst)
            self.assertEqual(actual, result)


unittest.main()
