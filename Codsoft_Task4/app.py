from tkinter import *
from PIL import Image, ImageTk
from random import randint
from tkinter import messagebox

#MAIN WINDOW SETTINGS
root = Tk()
root.title("Rock Scissor Paper")
root.configure(background="#2B2D2F")

width=root.winfo_screenwidth()
height=root.winfo_screenheight()

root.geometry("{0}x{1}+0+0".format(width,height))

#PICTURES
rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))
rbtn=ImageTk.PhotoImage(Image.open("rbtn.png"))
pbtn=ImageTk.PhotoImage(Image.open("pbtn.png"))
sbtn=ImageTk.PhotoImage(Image.open("sbtn.png"))
logo=ImageTk.PhotoImage(Image.open("logo.png"))


l=Label(root,image=logo,bg="#2B2D2F").place(x=5,y=1)

#LABELS FOR IDENTIFYING COMPUTER AND USER
cmp= Label(root, font=50, text="COMPUTER",bg="#2B2D2F", fg="white").place(x=500, y=100)
u= Label(root, font=50, text="USER", bg="#2B2D2F", fg="white").place(x=955, y=100)

#INITIAL CONDITION - TIE - BEFORE GAME BEGINS
comp_label = Label(root, image=scissor_img_comp, bg="#2B2D2F")
user_label = Label(root, image=scissor_img, bg="#2B2D2F")
comp_label.place(x=450, y=180)
user_label.place(x=880, y=180)

#PLAY AGAIN + DISPLAY RESULT
def show_message_box(text):
    result = messagebox.askquestion("Game Over", text + "\n\nDo you want to Play Again?")
    if result == 'yes':
        pass
    else:
         root.destroy()


#GAME LOGIC
def checkWin(player, computer):
    if player == computer:
        show_message_box_with_delay("It's a tie!!!")
    elif player == "rock":
        if computer == "paper":
            show_message_box_with_delay("You lose")
        else:
            show_message_box_with_delay("You win")
    elif player == "paper":
        if computer == "scissor":
            show_message_box_with_delay("You lose")
        else:
            show_message_box_with_delay("You win")
    elif player == "scissor":
        if computer == "rock":
            show_message_box_with_delay("You lose")
        else:
            show_message_box_with_delay("You win")

def show_message_box_with_delay(message):
    root.after(250, lambda: show_message_box(message))


#COMPUTER SELECTION + DISPLAY CHOICE
choices = ["rock", "paper", "scissor"]
def updateChoice(x):
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)


#DISPLAY USER CHOICE
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)
    checkWin(x, compChoice)

#USER INPUT
rock = Button(root,  image=rbtn, bg="#2B2D2F",cursor="hand2",bd=0, command=lambda: updateChoice("rock")).place(x=1200, y=170)
paper = Button(root,  image=pbtn,bg="#2B2D2F", cursor="hand2",bd=0,command=lambda: updateChoice("paper")).place(x=1200, y=260)
scissor = Button(root,  image=sbtn, bg="#2B2D2F", cursor="hand2",bd=0, command=lambda: updateChoice("scissor")).place(x=1200, y=350)

t=Label(root,text="Copyright @ Nostalgia. All rights reserved.",font=16,fg="white",bg="#2B2D2F").place(x=2,y=700)

root.mainloop()