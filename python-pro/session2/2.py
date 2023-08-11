from tkinter import *

root = Tk()
root.title("My Project")
root.geometry("400x500")
frame = Frame(root, width=100, height=100)
frame.grid()
textInput = Entry(frame, font=("Segoe UI", 20))
textInput.grid(row=1, column=0)
label = Label(frame, font=("Segoe UI Display", 20))
label.grid(row=0, column=0, pady=10)
def sayHello():
#	print(f"Hello {textInput.get()}!!")
	label.config(text=f"Hello {textInput.get()}!!")

showText = Button(frame, text="Show Your Text", font=("Segoe UI", 20), command=sayHello)
showText.grid(row=2, column=0, padx=10, pady=50)

root.mainloop()
