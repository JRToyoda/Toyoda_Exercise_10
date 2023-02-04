class Question:
    def __init__(self):
        self._question = ""
        self._answer = ""

    def setQuestion(self, questionText):
        self._question = questionText + "?\n----------------"

    def setAnswer(self, questionAnswer):
        self._answer = questionAnswer

    def checkAnswer(self, userAnswer):
        return userAnswer == self._answer

    def display(self):
        print(self._question)


class Choices(Question):
    def __init__(self):
        super().__init__()
        self._choices = []

    def addChoice(self, choice, correctChoice):
        self._choices.append(choice)
        if correctChoice:
            answerPosition = str(len(self._choices))
            self.setAnswer(answerPosition)

    def display(self):
        super().display()

        for i in range(len(self._choices)):
            position = i + 1
            print("%d: %s" % (position, self._choices[i]))