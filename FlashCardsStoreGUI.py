from tkinter import *
import sqlite3
import os

os.chdir(r'C:\Users\sohai\OneDrive\Desktop\All About Programming\Python Projects\Projects For Training\FlashCardsDatabase')

# Setup Window
root = Tk()
root.title("Flash Cards")
root['background'] = '#d3ffce'


# Fetch Data from data base
def connect_to_data():
    global db
    db = sqlite3.connect('flashcards.db')
    global cr
    cr = db.cursor()
    cr.execute('select * from FlashCards')
    global words_list
    words_list = cr.fetchall()

connect_to_data()
#Setup Buttons And Labels 

word_label = Label(root,bg="#d3ffce",fg="black",font=('Oswald Light',20))
word_label.grid(row=1,column=1,columnspan=3)

w_label = Label(root,bg="#d3ffce",fg="black",text="Word:",font=('Ubuntu',10))
word_entry = Entry(root,font=('Ubuntu',15))

word_entry.grid(row=2,column=2)
w_label.grid(row=2,column=1)

d_label = Label(root,bg="#d3ffce",fg="black",text="Defination For Word:",font=('Ubuntu',10))
def_entry = Entry(root,font=('Ubuntu',15))
def_entry.grid(row=3,column=2)
d_label.grid(row=3,column=1)

s_label = Label(root,bg="#d3ffce",fg="black",text="Sentence For Word:",font=('Ubuntu',10))
sen_entry = Entry(root,font=('Ubuntu',15))
sen_entry.grid(row=4,column=2)
s_label.grid(row=4,column=1)

def add_word():
    my_word = word_entry.get()
    my_def = def_entry.get()
    my_sent = sen_entry.get()
    data = (my_word,my_def,my_sent)
    cr.execute("insert or ignore into FlashCards values(?,?,?)", data)
    db.commit()
    db.close()
    connect_to_data()
    root.update()


add_button = Button(root,width=10,font=('Ubuntu',15),bg="#d3ffce",text="Add",command=add_word)
add_button.grid(row=5,column=2)



def next_b():
    global selected_word
    if selected_word > len(words_list)-1:
        selected_word = 0
        root.update()
        word_label.config(text=f"{words_list[selected_word][0]}\n{words_list[selected_word][1]}\n{words_list[selected_word][2]}")
    else:
        selected_word +=1
        root.update()
        word_label.config(text=f"{words_list[selected_word][0]}\n{words_list[selected_word][1]}\n{words_list[selected_word][2]}")


def pervious():
    global selected_word
    if selected_word > len(words_list):
        selected_word = 0
        root.update()
        word_label.config(text=f"{words_list[selected_word][0]}\n{words_list[selected_word][1]}\n{words_list[selected_word][2]}")
    else:
        selected_word -=1
        root.update()
        word_label.config(text=f"{words_list[selected_word][0]}\n{words_list[selected_word][1]}\n{words_list[selected_word][2]}")

next_but = Button(root,text=">>",width=5,font=(10),bg='#d3ffce',command=next_b)
next_but.grid(row=6,column=3)

per_but = Button(root,text="<<",width=5,font=(10),bg='#d3ffce',command=pervious)
per_but.grid(row=6,column=1)

def exit_prog():
    db.commit()
    db.close()
    root.destroy()

close_but = Button(root,text="Exit Program",width=10,font=(5),bg='#d3ffce',command=exit_prog)
close_but.grid(row=7,column=2)
# Putting First Word in word_label
global selected_word
selected_word = 0
word_label.config(text=f"{words_list[selected_word][0]}\n{words_list[selected_word][1]}\n{words_list[selected_word][2]}")



root.mainloop()
