from tkinter import *

root = Tk()

root.geometry("333x470")
root.title("Calculator")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 30 bold")
screen.pack(fill=X, ipadx=8, padx=3, pady=3)



def click(event):
	global scvalue
	text = event.widget.cget("text")
	print(text)

	if text == "=":
		if scvalue.get().isdigit():
			value = int(scvalue.get())

		else:
			value = eval(screen.get())


		scvalue.set(value)
		screen.update()
	elif text == "c":
		scvalue.set("")
		screen.update()

	else:
		scvalue.set(scvalue.get() + text)

#creating the buttons (1)


f = Frame(root, bg="grey")

b = Button(f, text="1", font="lucida 30 bold", padx=2, pady=2)
b.pack(side=LEFT)
b.bind("<Button-1>", click)
f.pack()

#2

b = Button(f, text="2", font="lucida 30 bold", padx=2, pady=2)
b.pack(side=LEFT)
b.bind("<Button-1>", click)
f.pack()

b = Button(f, text="3", font="lucida 30 bold", padx=2, pady=2)
b.pack(side=LEFT)
b.bind("<Button-1>", click)
f.pack()






f = Frame(root, bg="grey")

b = Button(f, text="4", font="lucida 30 bold", padx=2, pady=2)
b.pack(side=LEFT)
b.bind("<Button-1>", click)
f.pack()

#2

b = Button(f, text="5", font="lucida 30 bold", padx=2, pady=2)
b.pack(side=LEFT)
b.bind("<Button-1>", click)
f.pack()

b = Button(f, text="6", font="lucida 30 bold", padx=2, pady=2)
b.pack(side=LEFT)
b.bind("<Button-1>", click)
f.pack()



f = Frame(root, bg="grey")

b = Button(f, text="7", font="lucida 30 bold", padx=2, pady=2)
b.pack(side=LEFT)
b.bind("<Button-1>", click)
f.pack()

#2

b = Button(f, text="8", font="lucida 30 bold", padx=2, pady=2)
b.pack(side=LEFT)
b.bind("<Button-1>", click)
f.pack()

b = Button(f, text="9", font="lucida 30 bold", padx=2, pady=2)
b.pack(side=LEFT)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="grey")

b = Button(f, text="c", font="lucida 30 bold", padx=1, pady=1)
b.pack(side=LEFT)
b.bind("<Button-1>", click)
f.pack()

#2

b = Button(f, text="-", font="lucida 30 bold", padx=2, pady=2)
b.pack(side=LEFT)
b.bind("<Button-1>", click)
f.pack()

b = Button(f, text="+", font="lucida 30 bold", padx=2, pady=2)
b.pack(side=LEFT)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="grey")

b = Button(f, text="*", font="lucida 30 bold", padx=2, pady=2)
b.pack(side=LEFT)
b.bind("<Button-1>", click)
f.pack()

#2

b = Button(f, text="0", font="lucida 30 bold", padx=2, pady=2)
b.pack(side=LEFT)
b.bind("<Button-1>", click)
f.pack()

b = Button(f, text="=", font="lucida 30 bold", padx=2, pady=2)
b.pack(side=LEFT)
b.bind("<Button-1>", click)
f.pack()


root.mainloop()