# Name: Miranda Towne
# Description: Create a list to hold to do tasks

to_do_list2 = []
finished = False
while not finished:
    task = input('Enter a task fo your to-do list.  Press <enter> when done: ')
    if len(task) == 0:
        finished = True
    else:
        to_do_list2.append(task)
        print('Task added.')

# Display the to-do list.
print()
print('Your To-Do List:')
print('-' * 16)
for task in to_do_list2:
    print(task)
