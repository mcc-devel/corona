from tkinter import *
import main

root = Tk()
root.title('corona GUI')
frame1 = Frame(root)
frame1.pack(side = TOP, fill = BOTH, expand = 1)
entry1 = Entry(frame1)
entry1.pack(side = LEFT, fill = X, expand = 1)
btn1 = Button(frame1, text = 'Check', command = main.main(True))
btn1.pack(side = RIGHT)
root.mainloop()
