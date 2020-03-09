# Name: Miranda Towne
# Description: GradeBook with class and objects

# Define gradebook class
class GradeBook():
    
    # Consturctor with the self parameter.
    def __init__(self):
        self.final_exam_grade = 0
        self.quiz_grades = [] # Empty quiz list
        self.assignment_grades = [] # Empty assignment list

    def quizScore(self, score:float):
        self.quiz_grades.append(score)
        return 

    def assignmentScore(self, score:float):
        self.assignment_grades.append(score)
        return 

    def finalExamScore(self, score:float):
        self.final_exam_grade = score
        return 
    
    def currentAverage(self):
        quizScores = 0
        assignmentScores = 0
        for score in self.quiz_grades: quizScores += score
        for score in self.assignment_grades: assignmentScores += score

        average = 0.4 * self.final_exam_grade + 0.3 * quizScores + 0.3 * assignmentScores
        return average


    
# Menu 
menu = """

Grade Book

        0: Exit
        1: Enter assignment grade
        2: Enter quiz grade
        3: Enter final exam grade
        4: Display current grade average
"""

gradeBook = GradeBook()
done = False

while not done:
    print(menu)
    selection = int(input("Please enter  a choice: "))
    if selection == 0:
        done = True
        print("\nThank you for using the Grade Book.")
        break
    elif selection == 1:
        score = float(input("Enter assignment grade: "))
        gradeBook.assignmentScore(score)
    elif selection == 2:
        score = float(input("Enter quiz grade: "))
        gradeBook.quizScore(score)
    elif selection == 3:
        score = float(input("Enter final exam grade: "))
        gradeBook.finalExamScore(score)
    elif selection == 4:
        average = gradeBook.currentAverage()
        print("Current average: {:.2f}".format(average))
        
        
        
