import tkinter as tk
from tkinter import filedialog


def openfile():
    file_path = tk.filedialog.askopenfilename(title="Select a File")
    with open(file_path, 'r') as f:
        content = f.read()
        text_box.delete(1.0, tk.END)
        text_box.insert(tk.END, content)


def savefile():
    content = text_box.get(1.0, tk.END)
    file_path = filedialog.asksaveasfilename(title="Save As", defaultextension=".txt", filetypes=[("Text files", "*.txt")])

    if file_path:
        with open(file_path, 'w') as file:
            file.write(content)



window = tk.Tk()
window.title("My Notepad")

file_frm = tk.Frame(master=window)
file_frm.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

editor_frm = tk.Frame(master=window)
editor_frm.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

open_btn = tk.Button(master=file_frm, text='Open', width=10, command=openfile)
open_btn.grid(row=0, padx=10, pady=10, ipadx=5, ipady=5)


save_btn = tk.Button(master=file_frm, text='Save As', width=10, command=savefile)
save_btn.grid(row=1, padx=10, pady=10, ipadx=5, ipady=5)


text_box = tk.Text(master=editor_frm)
text_box.pack()


window.mainloop()

