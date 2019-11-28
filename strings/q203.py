from base.question import *

class Str203(Question):

    description = "203) Validate Balanced Parentheses."

    def __init__(self):
        # s = "()(){(())"     # Should return false
        # s = ""              # Should return true
        # s = "([{}])()"      # Should return true
        # s = "[()]{}"        # Should return true
        # s = "({[)]"         # Should return false
        # s = "({[)}]"        # Should return false
        # s = "((()))"        # Should return true
        # s = "([)]"          # Should fail
        # s = "(){[()]}([([])]){}"        # Should succeed
        s = "((){[()]}([([])]){}"        # Should fail

        print(f"Original string: {s}\n")
        s = list(s)  # Strings are immutable so we need to explode s into a list
        self.check_if_balanced(s)


    def check_if_balanced(self, s):
        fail_flag = False
        close_order = [] # Holds the order they need to be closed

        for i in range(len(s)):
            print(f"String s this iteration {i+1}: {''.join(s[:i])}")
            print(f"Close_order this iteration {i+1}: {''.join(close_order)}")
            if '(' == s[i]:
                close_order.append(')')
            elif '[' == s[i]:
                close_order.append(']')
            elif '{' == s[i]:
                close_order.append('}')
            elif len(close_order)!= 0 and close_order[-1] == s[i]:
                close_order.pop()
            else:
                print("Unmatched char found! Fail immediately!")
                fail_flag = True
                break

        # print(f"Open order: {''.join(open_order)}")
        print(f"\nClose order: {''.join(close_order)}")
        if 0 == len(close_order) and not fail_flag:
            print("Success!")
        else:
            print("Fail!")


    # def __init__(self):
    #     # s = "()(){(())"     # Should return false
    #     # s = ""              # Should return true
    #     # s = "([{}])()"      # Should return true
    #     # s = "[()]{}"        # Should return true
    #     # s = "({[)]"         # Should return false
    #     # s = "({[)}]"          # Should return false
    #     # s = "((()))"        # Should return true
    #     s = "([)]"
    #
    #     print(f"Original string: {s}\n")
    #
    #     s_orig = s   # Make a backup of s
    #
    #     s = list(s)  # Strings are immutable so we need to explode s into a list
    #     fail_flag = False
    #     p_count = 0
    #
    #     for i in range(len(s)):
    #         print(f"This iteration {i+1}: {''.join(s)}")
    #         if '(' == s[i]:
    #             search_char = ')'
    #         elif '[' == s[i]:
    #             search_char = ']'
    #         elif '{' == s[i]:
    #             search_char = '}'
    #         elif 'p' == s[i]:
    #             continue
    #         elif ')' == s[i] or '}' == s[i] or ']' == s[i]:
    #             fail_flag = True
    #             break
    #
    #         p_index = self.find_first_instance(s, search_char)
    #         if p_index < 0:
    #             fail_flag = True
    #             break
    #         else:
    #             s[i] = 'p'
    #             s[p_index] = 'p'
    #             p_count += 2
    #
    #         # If all characters have been examined, we can quit the loop
    #         if p_count == len(s):
    #             break
    #
    #
    #     print(f"\nFinal: {''.join(s)}")
    #     if fail_flag or p_count != len(s):
    #         print("Fail!")
    #     else:
    #         print("Success!")
    #
    #
    # # Return the index of the first occurence of char in s
    # # Else, return -1
    # def find_first_instance(self, s, search_char):
    #     for i in range(len(s)):
    #         if s[i] == search_char:
    #             return i
    #     return -1
