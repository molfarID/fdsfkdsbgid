import collections
import random


class TrueFalse:

    def __init__(self, path_q="Questions.csv", sproby=3):

        self.path_q = path_q
        self.sproby = sproby
        self.question = self.read_question(self.path_q)
        self.len_quest = len(self.question)
        self.questions = []
        self.number_question = 0
        self.true_quest = 0

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

    def give_question(self):
        self.questions = []
        if len(self.question) >= 1:
            self.number_question += 1
            self.questions.append(self.question.pop(
                random.randint(0, len(self.question)-1)))

            return f"{self.number_question}. {self.questions[0].question} [ {self.true_quest} /  {self.sproby} ]"
        return "No questions."

    def result_reply(self, reply):
        if self.sproby == 0:
            return f"You LOSE! Yours true reply : \
                {self.true_quest} / {self.len_quest}]"
        if reply.lower() == self.questions[0].reply.lower():
            self.true_quest += 1
            return "Це правильна відповідь! Вітаю!"
        self.sproby -= 1
        return "Це не правильна відповідь! Не вітаю)"


if __name__ == "__main__":
    test = TrueFalse("Questions.csv")
    print(test.give_question())
