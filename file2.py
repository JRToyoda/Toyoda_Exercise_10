class Question:
    def __init__(self):
        self.question = ""
        self.answer = ""

    def setQuestion(self, questionText):
        self.question = questionText + "?"

    def setAnswer(self, questionAnswer):
        self.answer = questionAnswer

    def checkAnswer(self, userAnswer):
        return userAnswer == self.answer

    def display(self):
        print(self.question)


class Choices(Question):
    def __init__(self):
        super().__init__()
        self.choices = []

    def addChoice(self, choice, correct):
        self.choices.append(choice)
        if correct:
            answer = str(len(self.choices))
            self.setAnswer(answer)

    def display(self):
        super().display()

        for i in range(len(self.choices)):
            position = i + 1
            print("%d: %s" % (position, self.choices[i]))
