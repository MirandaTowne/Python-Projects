# Name: Miranda Towne
# Description: Convert letters to Morse Code


# Determine which letter was entered and display Morse Code string.
def text_to_morse(letter):
    if letter == "A":
        code = ".-"
    elif letter == "B":
        code = "-..."
    elif letter == "C":
        code = "-.-."
    elif letter == "D":
        code = "-.."
    elif letter == "E":
        code = "."
    elif letter == "F":
        code = "..-."
    elif letter == "G":
        code = "--."
    elif letter == "H":
        code = "...."
    elif letter == "J":
        code = ".---"
    elif letter == "K":
        code = "-.-"
    elif letter == "L":
        code = ".-.."
    elif letter == "M":
        code = "--"
    elif letter == "N":
        code = "-."
    elif letter == "O":
        code = "---"
    elif letter == "P":
        code = ".--."
    elif letter == "Q":
        code = "--.-"
    elif letter == "R":
        code = ".-."
    elif letter == "S":
        code = "..."
    elif letter == "T":
        code = "-"
    elif letter == "U":
        code = "..-"
    elif letter == "V":
        code = "...-"
    elif letter == "W":
        code = ".--"
    elif letter == "X":
        code = "-..-"
    elif letter == "Y":
        code = "-.--"
    elif letter == "Z":
        code = "--.."
    else:
        print("Unknown")
    return code
for letter in range(4):
    letter = (input("Please enter an upper case letter to convert to Morse code: "))
    code = text_to_morse(letter)
    print("Your code for {} is {}.".format(letter,code))

