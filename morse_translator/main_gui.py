import tkinter as tk
import re
from morse import morse, reverse_morse

def convert_to_morse():
    word = text_bar.get().lower()
    word = re.sub(r"[^a-z0-9 ]", "", word)
    output = [morse.get(x, " ") for x in word]
    result_label.config(text="".join(output), font=("Comic Sans MS", 14))  # Display the output with a decorative font

def convert_to_english():
    word = text_bar.get().lower()
    word = re.sub(r"[^.= ]", "", word)
    output = [reverse_morse.get(x, " ") for x in word]
    result_label.config(text="".join(output), font=("Comic Sans MS", 14))  # Display the output with a decorative font

def main():
    global text_bar, result_label  # Declare text_bar and result_label as global variables
    # Create the main window
    window = tk.Tk()
    window.geometry("800x500")  # Set window size

    # Create a text bar
    text_bar = tk.Entry(window)
    text_bar.pack(pady=20)

    # Create the first button
    button1 = tk.Button(window, text="Convert to Morse", command=convert_to_morse)
    button1.pack(pady=10)

    # Create the second button
    button2 = tk.Button(window, text="Convert to English", command=convert_to_english)
    button2.pack(pady=10)

    # Create a label to display the output
    result_label = tk.Label(window, text="", wraplength=700, justify="left", font=("Comic Sans MS", 14))
    result_label.pack(pady=20)

    # Start the main loop
    window.mainloop()

if __name__ == "__main__":
    main()
