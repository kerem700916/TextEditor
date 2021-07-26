#importing libraries
import enchant, sys, os
from termcolor import colored

#clearing the output file
with open("text_editor.txt", 'a') as f:
    f.truncate(0)

#the dict
dictionary = enchant.Dict('en_Us')

#reading the file
input_file = 'text.txt'
try:
    file = open(input_file, 'r')
    content = file.read()
except FileNotFoundError:
    print('file not found')
    sys.exit(0)

#variables
text_editor_content = []
wrong_word = 0

#rewrites the text
def re_write():
    for string in content:
        if string == ' ':
            string = '\n'
        else:
            pass 
        text_editor_content.append(string)

    file2 = open('text_editor.txt', 'a')

    for string in text_editor_content:
        file2.write(string)

#checks the text
def check():
    global wrong_word
    file2 = open('text_editor.txt', 'r')
    while True:
        line = file2.readline()
        if not line:
            break 
        else:
            new_line_list = []
            for string in line:
                if string == '\n':
                    pass
                else:
                    new_line_list.append(string)
            line = ''
            for string in new_line_list:
                line = line + string
            if dictionary.check(line) is False:
                print('\ntake a look at ' + colored(line, 'red'))
                print('\nhere are some suggestions:\n')
                for suggestion in dictionary.suggest(line):
                    print(suggestion)
                print('\n\n')
                wrong_word += 1
            else:
                pass

#running the main program
re_write()
check()

#one more operation
if wrong_word == 1:
    print('\n\nthere is ' + str(wrong_word) + ' mistake\n\n')
else:
    print('\n\nthere are ' + str(wrong_word) + ' mistakes\n\n')

#quiting the code
quit()
