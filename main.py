from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data_dict={}

#Ler arquivo CSV
try:
    data = pandas.read_csv("data/Words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/english_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


#Funções

def know_word():
    data_dict.remove(current_card)
    data = pandas.DataFrame(data_dict)
    data.to_csv("data/Words_to_learn.csv",index=False)
    nex_card()

def nex_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(label, text=f"English", font=("Arial", 40, "italic"),fill="black")
    canvas.itemconfig(label2, text=f"{current_card['English']}",font=("Arial", 60, "bold"),fill="black")
    canvas.itemconfig(img,image=old_img)
    window.after(3000, flip_card)
def flip_card():
    canvas.itemconfig(img, image=new_image)
    canvas.itemconfig(label, text=f"Português", font=("Arial", 40, "italic"),fill = "white")
    canvas.itemconfig(label2, text=f"{current_card['Português']}", font=("Arial", 60, "bold"),fill = "white")

#Front-End

window = Tk()
window.title("Flashy Card")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,flip_card)

canvas = Canvas(width=800, height=526)
old_img = PhotoImage(file= "images/card_front.png")
new_image = PhotoImage(file="images/card_back.png")
img = canvas.create_image(400,263, image=old_img)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0,row=0,columnspan = 2)
label = canvas.create_text(400,150, text="", font=("Arial",40,"italic"))
label2 = canvas.create_text(400,250, text="", font=("Arial",60,"bold"))

#images
my_image= PhotoImage(file= "images/right.png")
my_image2 = PhotoImage(file="images/wrong.png")

#buttons
button_right = Button(image=my_image,command= know_word, highlightthickness=0)
button_right.grid(column=1,row=1,)

button_wrong = Button(image=my_image2,command= nex_card, highlightthickness=0)
button_wrong.grid(column=0,row=1)

nex_card()

window.mainloop()