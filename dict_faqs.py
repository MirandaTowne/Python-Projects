# Name: Miranda Towne
# Description: Dictionary of FAQ's


faqs_Dictionary = {}


def display():
    if len(faqs_Dictionary) > 0:
        print("=" * 27)
        print("Frequently Asked Questions:")
        print("=" * 27)
        for key, value in faqs_Dictionary.items():
            print(f'Question:{key}')
            print(f'Answer:{value}')
    else:
        print("Dictionary is Empty")


def addFAQs():
    while True:
        question = input("Enter your Question : ")
        keysList = faqs_Dictionary.keys()
        status = False
        matchedKey = question
        for key in keysList:
            if key.lower() == question.lower():
                matchedKey = key
                status = True
        if status:
            print("Question already exists")
            option = input("Do you want to rephrase the question(yes/no) : ")
            if option.lower() == "yes":
                continue
            else:
                matchedKey = question
        answer = input("Enter your Answer : ")
        faqs_Dictionary[matchedKey] = answer
        print("Question added successfully")
        break


def deleteFAQs():
    if len(faqs_Dictionary) > 0:
        question = input("Enter your question to delete : ")
        keysList = faqs_Dictionary.keys()
        for key in keysList:
            if key.lower() == question.lower():
                status = True
        if status:
            del faqs_Dictionary[question]
            print("Question is deleted")
        else:
            print("Question not found")
    else:
        print("Dictionary is Empty")


def quitProgram():
    print("Program Terminated")


def switcher_choice(argument):
    switcher = {
        1: display,
        2: addFAQs,
        3: deleteFAQs,
        4: quitProgram
    }
    func = switcher.get(argument, lambda: 'Invalid')
    return func()


if __name__ == "__main__":
    choice = ''
    while choice != 4:  # Loop continuously
        print("=" * 27)
        print("Frequently Asked Questions")
        print("=" * 27)
        print("\n1 Display FAQ's\n2 Add FAQ's\n3 Delete FAQ's\n4 Quit")
        choice = int(input("\nEnter Your Choice : "))
        switcher_choice(choice)
