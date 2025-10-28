# Quiz App by @panwarcodes/github
import sys

# Questions for quiz_app
questions = {  
    "Is the sun a star?": True,
    "Is 5 greater than 10?": False,
    "Does Python support object-oriented programming?": True,
    "Is 100 an even number?": True,
    "Is the Earth flat?": False,
    "Is 'hello' a string?": True,
    "Can a list in Python store different data types?": True,
    "Is 7 divisible by 2?": False,
    "Is water a liquid at room temperature?": True,
    "Is the capital of France London?": False,
}

# Question asker and score storage
def question_asker():
    store_correct = 0
    for question in questions.keys():        
        answer = input(question + ": ")
        print()
        if (str(answer) == "quit"):
            sys.exit()
        elif (answer.capitalize()) == str(questions[question]):
            store_correct += 1
        else:
            pass
    print(f"Your score: {store_correct * 10}%.\nIn which {store_correct} were correct out of {len(questions)}.")

# Welcome message
print("-------This is a interactive Quiz App---------")
print("You have to answer whether the given statement")
print("is true or false. (You can exit by answering quit)")
print()
question_asker()

    