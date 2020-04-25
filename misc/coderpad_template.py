import pandas as pd

class InterviewQuestion(object):
    welcome_message = "Hello there!"
    temp = None

    def __init__(self):
        self.temp = 1
        test_cases = [
            (1, True),
            (0, False),
            (1, True)
        ]

        all_pass = True
        df = pd.DataFrame(columns=['Test','Expected','Result','Test_Pass'])
        i = 0
        for test in test_cases:
            rs = self.run_test(test[0])
            test_pass = rs == test[1]
            df.loc[i] = [test[0], test[1], rs, test_pass]
            if test_pass == False : all_pass = False
            i += 1
        print(df)
        print(f"\nTest Suite Result: {all_pass}")


    def run_test(self, num):
        if num is 1:
            return True
        else:
            return False



iq = InterviewQuestion()
