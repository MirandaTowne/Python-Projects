# Name: Miranda Towne
# Description: Creating a menu that gives user 3 choices

# Empty list
grade = []
done = False
new_grade = ''

# Menu options 
menu = """

Grade Book

    0: Exit
    1: Display a sorted list of grades
    2: Add a grade to the list

"""

# Display menu at start of a while loop
while not done:
    print(menu)
    # Ask for users choice
    option = int(input('\nPlease enter an option: '))

    # Respond to users choice
    if option == 0:
        done = True
        print("Good bye!")
    elif option == 1:
        grade.sort
        print(grade)
    elif option  == 2:
        new_grade = input('\nPlease add a new grade to the list: ')
        grade.append(new_grade)
        print("\nGrade added to the list")
        print(grade)
