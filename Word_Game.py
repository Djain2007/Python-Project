import tkinter as tk
from tkinter import messagebox
import random


WORD_LIST = [
    "APPLE", "CRANE", "TABLE", "PLANE", "HELLO", "LIGHT" 
]
MAX_GUESSES = 8
WORD_LENGTH = 5


COLOR_GREEN = "#1ABC9C"   
COLOR_YELLOW = "#F1C40F"
COLOR_GRAY = "#BDC3C7" 
COLOR_DEFAULT = "#ECF0F1"


def get_simple_feedback(secret_word, guess):
    
    colors = [COLOR_GRAY] * WORD_LENGTH
    
    for i in range(WORD_LENGTH):
        if i < len(guess):
            if guess[i] == secret_word[i]:
                colors[i] = COLOR_GREEN  
            elif guess[i] in secret_word:
                colors[i] = COLOR_YELLOW 
            
    return colors


class SimpleWordleApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Wordle")
        self.geometry("350x500") 
        self.resizable(False, False)
        self.config(bg="#FFFFFF")
        
       
        self.secret_word = random.choice(WORD_LIST).upper()
        self.current_row = 0
        self.cell_labels = [[None] * WORD_LENGTH for _ in range(MAX_GUESSES)]
        
        self.create_widgets()
        
    def create_widgets(self):

        
        
        tk.Label(self, text="WORDLE LITE", font=('Verdana', 18, 'bold'), bg="#FFFFFF").pack(pady=10)
        
       
        self.info_label = tk.Label(self, text="Guess a 5-letter word!", font=('Arial', 10), bg="#FFFFFF")
        self.info_label.pack(pady=5)
        
      
        grid_frame = tk.Frame(self, bg="#FFFFFF")
        grid_frame.pack(pady=10)
        
        for r in range(MAX_GUESSES):
            for c in range(WORD_LENGTH):
                cell = tk.Label(grid_frame, text="", width=3, height=1, 
                                bg=COLOR_DEFAULT, fg="black",
                                font=('Arial', 16, 'bold'), relief="raised", bd=1)
                cell.grid(row=r, column=c, padx=2, pady=2) 
                self.cell_labels[r][c] = cell 

        
        input_frame = tk.Frame(self, bg="#FFFFFF")
        input_frame.pack(pady=15)
        
        self.input_entry = tk.Entry(input_frame, font=('Arial', 14), justify='center', width=6)
        self.input_entry.pack(side=tk.LEFT, padx=5)
        
        tk.Button(input_frame, text="Guess!", command=self.handle_guess, 
                  font=('Arial', 12, 'bold'), bg="#3498DB", fg="white").pack(side=tk.LEFT, padx=5) 
        
        self.input_entry.focus_set()

    def handle_guess(self):
        
        guess = self.input_entry.get().strip().upper()
        
        if len(guess) != WORD_LENGTH:
            self.info_label.config(text=f"Word must be {WORD_LENGTH} letters!", fg="red")
            return
            
        self.info_label.config(text="") 
        
        colors = get_simple_feedback(self.secret_word, guess)
        
        for c in range(WORD_LENGTH):
            cell = self.cell_labels[self.current_row][c]
            cell.config(text=guess[c], bg=colors[c], fg="black" if colors[c] == COLOR_GRAY or colors[c] == COLOR_DEFAULT else "white")
        
        if guess == self.secret_word:
            messagebox.showinfo("Wordle", f"🎉 You Win! The word was '{self.secret_word}'!")
            self.end_game()
            return

        self.current_row += 1
        self.input_entry.delete(0, tk.END)
        
        if self.current_row == MAX_GUESSES:
            messagebox.showinfo("Wordle", f"😔 Game Over! The word was '{self.secret_word}'.")
            self.end_game()
            return
            
    def end_game(self):

        self.input_entry.config(state='disabled')
        
if __name__ == "__main__":
    app = SimpleWordleApp()

    app.mainloop()
