# Library imports
import datetime
import random
import os
import json
import sys
import pyautogui as py
import webbrowser as web
from time import sleep

#Load recent messages sent
def load_recent_message_indices():
    if os.path.exists('recent_message_indices.json'):
        with open('recent_message_indices.json', 'r') as file:
            content = file.read()
            if content.strip(): #Check if the file is not empty
                return json.loads(content)
    return []

#Save the updated used message indices list
def save_recent_message_indices(indices):
    with open('recent_message_indices.json', 'w') as file:
        json.dump(indices, file)

recent_message_indices = load_recent_message_indices()

#Choose a message and check if it is available
def unusable_checker():
    global recent_message_indices
    available_indices = [i for i in range(15) if i not in recent_message_indices]

    if not available_indices:
        recent_message_indices.clear()
        available_indices = list(range(15))

    message_index = random.choice(available_indices)

    if len(recent_message_indices) >= 4:
        recent_message_indices.clear()
    recent_message_indices.append(message_index)

    save_recent_message_indices(recent_message_indices)
    print("Recent message indices:", recent_message_indices) #Debugging
    return message_index

# Whatsapp message sender function
def send_message(phone, message):

    url = 'https://web.whatsapp.com/send?phone={}'.format(phone)
    web.open_new_tab(url)
    sleep(10)
    py.typewrite(message)
    py.press('enter')
    sleep(15)

# arrays (people, messages, birthdays_today)

# Each element in the outer most array represents the month of the year.
# Inside, write the name, day of the month and phone number of each person.
people=[ 
    [ 
        [ 'Person1', 25, '1234567890' ], 
        [ 'Person2', 13, '3456789012' ],
        [ 'Person3', 21, '2345678901' ]
    ],

    [
        [ 'Person4', 15, '1234567890' ], 
        [ 'Person5', 11, '3456789012' ],
        [ 'Person6', 11, '2345678901' ]

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
        [ 'Person7', 15, '1234567890' ], 
        [ 'Person8', 10, '1234567890' ],
        [ 'Person9', 20, '1234567890' ]

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

# Custom messages that can be sent
messages=['{} Hello', '{} Hola', '{} How', '{} Como', '{} Are', '{} Estas', '{} You', '{} Tu', '{} On', '{} En', '{} This', '{} Este', '{} Day', '{} Dia', '{} ?']


birthdays_today=[]

#Variable definition

current_date = datetime.datetime.now()

# Extract the current day and month
current_day = current_date.day


current_month = current_date.month

# Get all of the birthdays of today
for i, threeD in enumerate(people, start=1):
    if i == current_month:
        for j, twoD in enumerate(threeD):
            for k, element in enumerate(twoD):
                if element == current_day:
                    birthdays_today.append(twoD)

#Check if there are any birthdays today
if birthdays_today:
    for i, people in enumerate(birthdays_today):
        name=people[0]
        phone=people[2]
        message=messages[unusable_checker()].format(name)
        send_message(phone, message)
        

else: sys.exit()

