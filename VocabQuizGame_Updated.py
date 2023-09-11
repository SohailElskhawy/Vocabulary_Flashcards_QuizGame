import tkinter as tk
import sqlite3
import os
import random

os.chdir(r"C:\Users\sohai\OneDrive\Desktop\All About Programming\Python Projects\Projects For Training\FlashCardsDatabase")

class VocabQuizGame:
    def __init__(self,root):
        self.root = root
        self.root['background'] = 'powder blue'
        self.root.geometry('1200x400')
        self.root.title("VocabQuizGame")
        
        self.correct_points = 0
        self.wrong_points = 0
        self.correct_label = tk.Label(root, text=f'Correct Answers : {self.correct_points}', bg='powder blue', font=(10))
        self.correct_label.place(x=1000, y=250)
        self.wrong_label = tk.Label(root, text=f'Wrong Answers : {self.wrong_points}', bg='powder blue', font=(10))
        self.wrong_label.place(x=1000, y=300)
        
        self.start_button = tk.Button(root,text='Start Game',command=self.start,font=(5))
        self.start_button.place(x=550,y=250)
        self.db = sqlite3.connect('flashcards.db')
        self.cr = self.db.cursor()
    
    def start(self):
        self.cr.execute('select * from FlashCards')
        self.words = self.cr.fetchall()
        self.next_question()
        self.start_button.destroy() 
    
    def next_question(self):
        self.clear_question()
        self.word = random.choice(self.words)
        self.question = self.word[1]
        self.answer = self.word[0]
        self.question_label = tk.Label(root,text=f'___?___ : {self.question}',bg='powder blue',font=(10))
        self.question_label.place(x=50,y=70)
        
        choices = [self.answer]
        
        while len(choices) < 4:
            choice = random.choice(self.words)[0]
            if choice!= self.answer and choice not in choices:
                choices.append(choice)
        
        random.shuffle(choices)
        
        self.choice_buttons = []
        
        for i, choice in enumerate(choices):
            choice_button = tk.Button(root,text=f'- {choice}',command=lambda ans =choice : self.check_answer(ans),font=(10))
            choice_button.place(x = 70,y= 150 + i *50)
            self.choice_buttons.append(choice_button)
    
    def clear_question(self):
        if hasattr(self,'question_label'):
            self.question_label.destroy()
        
        if hasattr(self,'choice_buttons'):
            for button in self.choice_buttons:
                button.destroy()
    
    def check_answer(self,selected_answer):
        if selected_answer == self.answer:
            self.correct_points +=1
        else:
            self.wrong_points += 1 
            print(self.answer + " : " + self.question)

        self.update_points()
        self.next_question()

    def update_points(self):
        self.correct_label.config(text=f'Correct Answers : {self.correct_points}')
        self.wrong_label.config(text=f'Wrong Answers : {self.wrong_points}')
    
    def run(self):
        self.root.mainloop()
        self.db.close()

if __name__ == '__main__':
    root =tk.Tk()
    app = VocabQuizGame(root)
    app.run()