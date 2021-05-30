import tkinter
import main

main = tkinter.Tk()
main.mainloop()
main.title('corona GUI')
frame1 = Frame(main)
entry1 = Entry(frame1)
btn1 = Button(frame1, command = main(True))