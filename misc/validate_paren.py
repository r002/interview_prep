# Michael's solution! Haha.
# Wed - Nov 27, 2019

#s = "()(){(())"     # Should return false
#s = ""              # Should return true
#s = "([{}])()"      # Should return true
# s = "[()]{}"        # Should return true
# s = "({[)]"         # Should return false
# s = "({[)}]"        # Should return false
#s = "((()))"        # Should return true
#s = "([)]"          # Should fail
#s = "(){[()]}([([])]){}"        # Should succeed
#s = "((){[()]}([([])]){}"        # Should fail
#s ="[([]"

def get_target_end_char(start_char):
  if start_char == "(":
    return ")"
  if start_char == "{":
    return "}"
  if start_char == "[":
    return "]"

  return None



def derp(seq):
  # in recursion, the order of base cases matter a lot-- so if you shift the 2nd to last one up, tests fail

  # remove all solved pairs
  seq_new = seq.replace("()","").replace("[]","").replace("{}","")

  if (len(seq_new) == 0):
    return True

  if get_target_end_char(seq_new[0]) is None:
    return False

  target_end_index = seq_new.rfind(get_target_end_char(seq_new[0]))
  # cant find target end
  if target_end_index == -1:
    return False

  if (len(seq_new) == 2):
    return True

  if len(seq_new)%2 == 1:
    return False

  this_seq = seq_new[1:target_end_index]
  next_seq = seq_new[target_end_index + 1:]

  return derp(this_seq) and derp(next_seq)

def test_cases():
  t = [
        ("()(){(())",False),
        ("",True),
        ("([{}])()",True),
        ("[()]{}",True),
        ("({[)]", False),
        ("({[)}]", False),
        ("((()))", True),
        ("([)]",False),
        ("(){[()]}([([])]){}",True),
        ("((){[()]}([([])]){}",False),
        ("[([]",False)
      ]

  pass_all = True

  for x in range(0,len(t)):
    test = t[x][0]
    method_result = derp(test)
    passed_test = (method_result == t[x][1])

    col_pad = 30

    test_str = f"test: \"{test}\"".ljust(col_pad)
    method_result_str = f"Expected: {method_result}".ljust(col_pad)
    passed_test_str = f"passed_test: {passed_test}".ljust(col_pad)
    print(f"{test_str} | {method_result_str} | {passed_test_str}")

    if pass_all != False:
      pass_all = passed_test

  print(f"\nDID I PASS COACH?!?!?!? {pass_all}")

test_cases()
