from base.question import *

class Algo101(Question):

    description = "101) Find the first ten numbers of the Fibonocci Sequence."

    def __init__(self):
        rs = [0, 1]
        iterations = 10
        # Eg. 0 1 1 2 3 5 8 13 21 34

        # rs = self.solve_iteratively(rs, iterations)
        # print(f"Fib seq (iterative): {rs}")

        rs = self.solve_recursively(rs, iterations)
        print(f"Fib seq (recursive): {rs}")

    def solve_recursively(self, rs, iterations):
        # Base case - Exit condition:
        if len(rs) == iterations:
            print(f"Finished! {rs}")
        else:
            fib_num = rs[-1] + rs[-2]
            print(f"fib num: {fib_num}")
            rs.append(fib_num)
            self.solve_recursively(rs, iterations)

        return rs


    def solve_iteratively(self, rs, iterations):
        for i in range(iterations-2):
            next_num = rs[-1] + rs[-2]
            rs.append(next_num)

        return rs
