#Importing the tkinter module
import tkinter as tk
#Importing the messagebox module from tkinter
from tkinter import messagebox
#Importing the random module
import random

# Create a function to generate a random flashcard
def get_random_flashcard(flashcards):
    # Choose a random French word
    french_word = random.choice(list(flashcards.keys()))
    # Return the French word and its English translation
    return french_word, flashcards[french_word]

# Flashcard data as a dictionary
flashcards = {
    'blue': 'bleu',
    'green': 'vert',
    'red': 'rouge',
    'black': 'noir',
    'white': 'blanc',
    'yellow': 'jaune',
    'purple': 'violet',
    'orange': 'orange',
    'pink': 'rose',
    'brown': 'marron'
}
# Create a class for the flashcard application
class FlashcardApp:
    # Initialize the application
    def __init__(self, master, flashcards):
        # Store the master window
        self.master = master
        # Store the flashcards dictionary
        self.flashcards = flashcards
        # Initialize the current flashcard
        self.current_flashcard = None
        # Set the window title and size
        self.master.title("French Flashcards")
        self.master.geometry("300x200")
        # Create the widgets
        self.french_label = tk.Label(master, text="", font=("Arial", 24))
        self.french_label.pack(pady=20)
        # Create the buttons
        self.next_button = tk.Button(master, text="Next", command=self.next_flashcard)
        self.next_button.pack()
        # Create the main window
        self.show_translation_button = tk.Button(master, text="Show Translation", command=self.show_translation)
        self.show_translation_button.pack()
        # Display the first flashcard
        self.next_flashcard()
    # Create a function to display the next flashcard
    def next_flashcard(self):
        # Get a random flashcard
        french_word, english_translation = get_random_flashcard(self.flashcards)
        # Display the French word
        self.current_flashcard = (french_word, english_translation)
        # Display the French word
        self.french_label.config(text=french_word)
    # Create a function to show the translation
    def show_translation(self):
        if self.current_flashcard is not None:
            messagebox.showinfo("Translation", self.current_flashcard[1])

# Create the main window
root = tk.Tk()
app = FlashcardApp(root, flashcards)

# Run the application
root.mainloop()