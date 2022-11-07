import time
import collections


class TrueFalse:

    def __init__(self, path_q="Questions.csv",):
        self.path_q = path_q
        self.question = self.read_question(self.path_q)

    def read_question(self, path_q):
        Questions = collections.namedtuple(
            "Questions", ["question", "reply", "apology"])
        sorted_question = []
        with open(path_q) as question:
            for q in question:
                q = q.split(";")
                s = sorted_question.append(Questions(q[0],q[1],q[2]))
        print(sorted_question[0].question)
        
        # print(question(sorted_question))


if __name__ == "__main__":
    test = TrueFalse("Questions.csv")
