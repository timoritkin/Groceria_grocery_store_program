import tkinter as tk


def insert_text():
    text = text_entry.get()  # Get the text from the entry
    # Calculate the middle column of the current line
    print(text_widget.winfo_width())
    middle= 20
    current_line = int(text_widget.index("insert").split(".")[0])
    # middle_column = len(text_widget.get(f"{current_line}.0", "insert")) // 2



    # Insert the text into the Text widget
    text_widget.insert(middle, text + "\n")


# Create the main application window
root = tk.Tk()
root.title("Insert Text in the Middle of a Row")

# Create a Text widget
text_widget = tk.Text(root, height=10, width=40)
text_widget.pack()

# Create an Entry widget for input
text_entry = tk.Entry(root, width=40)
text_entry.pack()

# Create a button for the insertion action
insert_button = tk.Button(root, text="Insert Text", command=insert_text)
insert_button.pack()

# Start the Tkinter event loop
root.mainloop()
