# Library imports
import pyautogui as py
import webbrowser as web
import datetime
from time import sleep

# arrays (people, messages, unusableMessages)

# NAME, DAY OF THE MONTH, PHONE NUMBER
people=[ 
    [ 
        [ "Person1", 25, 1234567890 ], 
        [ "Person2", 13, 3456789012 ],
        [ "Person3", 21, 2345678901 ]
    ],

    [
        [ "Person4", 15, 1234567890 ], 
        [ "Person5", 23, 3456789012 ],
        [ "Person6", 11, 2345678901 ]

    ], 

    [ 

    ], 

    [

    ], 

    [ 

    ], 

    [ 

    ], 

    [ 

    ], 

    [ 

    ], 

    [ 

    ], 

    [ 

    ],

    [ 

    ], 

    [ 

    ] 

]

messages=["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

unusableMessages=[]

#Variable definition

current_date = datetime.datetime.now()

# Extract the current day and month
#current_day = current_date.day

current_day = 11

#current_month = current_date.month

current_month = 2

# date checker and message selecter functionality (will call the sendMessage function if there is a match between todays date and a birthday)
#There has to be a while loop that checks for the existance of another person that has the same birthday as another one (or other many)

for i, threeD in enumerate(people, start=1):
    if i == current_month:
        for j, twoD in enumerate(threeD):
            for k, element in enumerate(twoD):
                if element == current_day:
                    print(twoD)

# Message selecter (Random)

# Unusable messages checker function (check that there are at most 3 messages in array, will contain the)
def unusableChecker():
    pass

# Whatsapp message sender function
def sendMessage(phone, message):

    url = 'https://web.whatsapp.com/send?phone={}'.format(phone)

    web.open(url)
    
    sleep(30)

    py.typewrite(message)

    py.press(enter)

'''Step 1: Check that there is a mathching birthday for todays date. If there is no birthday then end the algorithm. If there is a birthday, go to step 2
    Step 2: Store the name and phone number of the person in variables.
    Step 3: Select a random message from the list
    Step 4: Use the unusableChecker function to check if the message is available. If it is not available, go back to step 2. If it is available, go to step 5
    Step 5: Complete the message with the name of the person
    Step 6: pass the phone number and selected message to the sendMessage function
    Step 7: Send the message :)'''

