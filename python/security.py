import tkinter as tk

window = tk.Tk()
window.minsize(450, 200)
window.title('Sweet Security')

status = tk.Label(window, text='Status: ')
status.place(relx=0.2, rely=0.5, anchor=tk.CENTER)

window.mainloop()