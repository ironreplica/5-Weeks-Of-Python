from tkinter import *
from tkinter import messagebox
import random
import pandas as pd
import csv

# Flash Card App, flip flash cards to quickly learn JavaScript Concepts (built in python).
# 7/15/2024 Trevor Childs

# * Global Variables
curItem = []
curIndex = 0
drawPile = []
discardPile = []

# * Function for flipping the card
def flipCard():
    curTitle = curItem[0]
    curDescription = curItem[1]
    canvas.itemconfig(card_bg, image=card_back_img)
    canvas.itemconfig(card_title, text='Definition', fill='white')
    canvas.itemconfig(card_description, text=curDescription, fill='white')
    canvas.itemconfig(draw_count, text= f'DrawPile : {len(drawPile)}', fill='white')


# * Function for getting a random item from the dictionary
def randomItem():
    global curItem
    global curIndex

    # ! Pull from the draw pile and remove from the pile when it is marked correct
    curIndex = random.randrange(len(drawPile))
    curItem = drawPile[curIndex]

# * Function for skipping or moving to the next card
def nextCard():
    global flip_timer
    randomItem()
    window.after_cancel(flip_timer)
    # Config the GUI
    canvas.itemconfig(card_title, text='Concept', fill='black')
    canvas.itemconfig(card_description, text=curItem[0], fill='black')
    canvas.itemconfig(card_bg, image=card_front_img)
    canvas.itemconfig(draw_count, text= f'DrawPile : {len(drawPile)}', fill='black')
    # Get the next random item
    flip_timer = window.after(5000, func=flipCard)

# * Called when there is a correct card
def correctCard():
    if(len(drawPile) <= 1):
        messagebox.showinfo('Victory!', 'Good job! You finished all the flashcards!')
        window.destroy()
    drawPile.pop(curIndex)
    nextCard()

# * Reading the data - Initialization
try:
    data_file = pd.read_csv('data/concepts.csv')
    data_dict = data_file.to_dict('split')

except FileNotFoundError:
    messagebox.showerror('Error', 'FileNotFoundError, cannot find the .csv file.')
except:
    print('An unknown error occurred')
else:
    dict_len = len(data_dict['index']) # Getting the length of the dictionary
    dict_cols = data_dict['columns'] # Getting the column names and count
    dict_data = data_dict['data'] # Getting the data for the columns
    drawPile = dict_data
    randomItem()

#https://tooeletech.udemy.com/course/100-days-of-code/learn/lecture/20944524#overview

# UI Setup
BACKGROUND_COLOR = '#B1DDC6'
window = Tk()
window.title('Flash Card JavaScript Concepts')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# * Timer for flipping the card over
flip_timer = window.after(3500, func=flipCard)

# Canvas Setup
canvas = Canvas(width=800,height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_img = PhotoImage(file='images/card_back.png')
card_front_img = PhotoImage(file='images/card_front.png')
card_bg = canvas.create_image( 400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text='Concept', font=('Ariel', 40, 'bold'))
card_description = canvas.create_text(400, 263, width=750, text=curItem[0], font=('Ariel', 30, 'italic'), justify='center')
draw_count = canvas.create_text(400, 480, width=750, text=f'DrawPile : {len(drawPile)}', font=('Ariel', 20, 'bold'))
canvas.grid(row=0,column=0, columnspan=2)

# Unknown button (❌)
unknown_image = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=unknown_image, highlightthickness=0, command=nextCard)
unknown_button.grid(row=1,column=0)

# Known button (✅)
known_image = PhotoImage(file='images/right.png')
known_button = Button(image=known_image, highlightthickness=0, command=correctCard)
known_button.grid(row=1, column=1)



window.mainloop()



