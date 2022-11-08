import collections


class TrueFalse:

    def __init__(self, path_q="Questions.csv",):

        self.path_q = path_q
        self.question = self.read_question(self.path_q)

    def read_question(self, path_q: str) -> list:

        Questions = collections.namedtuple(
            "Questions", ["question", "reply", "apology"])
        sorted_question = []
        with open(path_q) as question:
            for quest in question:
                quest = quest.split(";")
                sorted_question.append(
                    Questions(quest[0], quest[1], quest[2]))
        return sorted_question


if __name__ == "__main__":
    test = TrueFalse("Questions.csv")
