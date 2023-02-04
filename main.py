from file2 import Choices

def askUser(prompt):
    prompt.display()
    userAnswer = input("Your answer: ") 
    print(prompt.checkAnswer(userAnswer))


def quiz():
    first_question = Choices()
    first_question.setQuestion("112 x 3")
    first_question.addChoice("326", False)
    first_question.addChoice("336", True)
    first_question.addChoice("347", False)
    first_question.addChoice("356", False)

    second_question = Choices()
    second_question.setQuestion("12 x 17")
    second_question.addChoice("304", False)
    second_question.addChoice("214", False)
    second_question.addChoice("204", True)
    second_question.addChoice("224", False)

    third_question = Choices()
    third_question.setQuestion("55 x 14")
    third_question.addChoice("870", False)
    third_question.addChoice("760", False)
    third_question.addChoice("770", True)
    third_question.addChoice("670", False)

    fourth_question = Choices()
    fourth_question.setQuestion("39 x 12")
    fourth_question.addChoice("468", True)
    fourth_question.addChoice("478", False)
    fourth_question.addChoice("498", False)
    fourth_question.addChoice("508", False)

    fifth_question = Choices()
    fifth_question.setQuestion("11 x 38")
    fifth_question.addChoice("418", True)
    fifth_question.addChoice("528", False)
    fifth_question.addChoice("518", False)
    fifth_question.addChoice("508", False)

    askUser(first_question)
    askUser(second_question)
    askUser(third_question)
    askUser(fourth_question)
    askUser(fifth_question)


quiz()
