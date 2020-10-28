'''
EDUCATION TERMINAL
'''

import custom
import time
import os

'''
startup
'''
#custom.checkinternet()

'''
Variables
'''
helptext = """
- Quit
- Help
- Clear
- Set-Timetable
"""




'''
Functions
'''
def timetable():
    setupdone = False

    if setupdone == False:

        #Monday
        setupdone = True
        mondayp1 = input('Whats your Monday P1 class? ')
        mondayp2 = input('Whats your Monday P2 class? ') 
        mondayp3 = input('Whats your Monday P3 class? ')
        mondayp4 = input('Whats your Monday P4 class? ')
        mondayp5 = input('Whats your Monday P5 class? ')
        mondayp6 = input('Whats your Monday P6 class? ')

        #tuesday
        tuesdayp1 = input('Whats your Tuesday P1 class? ')
        tuesdayp2 = input('Whats your Tuesday P2 class? ') 
        tuesdayp3 = input('Whats your Tuesday P3 class? ')
        tuesdayp4 = input('Whats your Tuesday P4 class? ')
        tuesdayp5 = input('Whats your Tuesday P5 class? ')
        tuesdayp6 = input('Whats your Tuesday P6 class? ')

        #Wednesday
        wednesdayp1 = input('Whats your Wednesday P1 class? ')
        wednesdayp2 = input('Whats your Wednesday P2 class? ') 
        wednesdayp3 = input('Whats your Wednesday P3 class? ')
        wednesdayp4 = input('Whats your Wednesday P4 class? ')
        wednesdayp5 = input('Whats your Wednesday P5 class? ')
        wednesdayp6 = input('Whats your Wednesday P6 class? ')

        #Thursday
        thursdayp1 = input('Whats your Thursday P1 class? ')
        thursdayp2 = input('Whats your Thursday P2 class? ') 
        thursdayp3 = input('Whats your Thursday P3 class? ')
        thursdayp4 = input('Whats your Thursday P4 class? ')
        thursdayp5 = input('Whats your Thursday P5 class? ')
        thursdayp6 = input('Whats your Thursday P6 class? ')

        #Friday
        fridayp1 = input('Whats your Friday P1 class? ')
        fridayp2 = input('Whats your Friday P2 class? ') 
        fridayp3 = input('Whats your Friday P3 class? ')
        fridayp4 = input('Whats your Friday P4 class? ')
        fridayp5 = input('Whats your Friday P5 class? ')
        fridayp6 = input('Whats your Friday P6 class? ')

    request = input('What Period Do you need to know?')
    


 















'''
Defining Terminal
'''
def terminal():
    userinput = input("/> ")
    userinput = userinput.lower()
    userinput = userinput.strip()

    ##################
    # Commands  Here #
    ##################
    if userinput == 'quit':
        quit()

    if userinput == 'help':
        print(helptext)

    if userinput == 'clear':
        os.system("clear")

    if userinput == 'timetable':
        timetable()




    else:
        print("ERROR Unrecognized Command")

'''
Run a terminal
'''
while True:
    terminal()
