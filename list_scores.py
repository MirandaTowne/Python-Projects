# Name: Miranda Towne
# Date: Jan. 26, 2020
# Assigment: Programming Assignment 4
# Course: SEC290 20228 B1 Spring 2020
# Description: A Menu Drive Interface


menu = """
1: Enter to exit
2: Display scores
3: Add a score to list
4: Display highest and lowest score

"""

# List of floating point numbers
scores = [85.3, 85.2, 21.99]
done = False

while not done:
    print(menu)
    selection = input('Please enter a selection between 1 and 4: ')

    if selection == '1':
        done = True
        print('\nThank you for using the score engine.')
        break
    elif selection == '2':
        scores.sort(reverse = True)
        print('\nScores recorded so far:\n',' '.join(['{:.2f}'.format(score) for score in scores]))
    elif selection == '3':
        new_score = float(input('\nPlease enter a score between 0.0 and 100.0: '))
        if new_score < 0:
            print('That score is too low.')
        elif new_score > 100:
            print('That score is too high.')
        else:
            scores.append(new_score)
            print('Score added to list')
    elif selection == '4':
        scores.sort(reverse = True)
        print('\nThe scores range from {:.2f} to {:.2f}.'.format(scores[0], scores[len(scores) -1]))
    else:
        print('\nThat selection is invalid. Please enter a selection between 1 to 4.')
        
