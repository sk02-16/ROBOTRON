from tkinter import *
import calendar

# function to display calendar
def DisplayCalendar():
    newRoot = Tk()
    newRoot.title('Calendar Screen')
    newRoot.config(bg='#F0EFEF')
    newRoot.geometry('700x700')
    actualyear = int(yearEntry.get())
    calendarContent = calendar.calendar(actualyear)
    lblNew = Label(newRoot, text=calendarContent, font='Arial 12 bold', bg='#F0EFEF', fg='#585858')
    lblNew.grid(row=0, column=0, padx=30, pady=30)
    newRoot.mainloop()


# designing first window
root = Tk()
root.config(bg='#585858')
root.title('Calendar App')
root.geometry("400x400")

header = Label(root, text='CALENDAR', bg='#F0EFEF', fg='#585858', font=('Helvetica', 32, 'bold'))
header.grid(row=0, column=0, padx=25, pady=25)

lbl = Label(root, text='Enter the year: ', bg='#F0EFEF', fg='#585858', font=('Helvetica', 12))
lbl.grid(row=1, column=0, padx=25)

yearEntry = Entry(root, width=5, font=('Helvetica', 12))
yearEntry.grid(row=2, column=0, padx=25, pady=10)

showcalendar = Button(root, text='Show Calendar', bg='#F0EFEF', fg='#585858', font=('Helvetica', 12, 'bold'),
                      command=DisplayCalendar)
showcalendar.grid(row=3, column=0, padx=25)

exitButton = Button(root, text='Exit', bg='#F0EFEF', fg='#585858', font=('Helvetica', 12), command=root.destroy)
exitButton.grid(row=4, column=0, padx=25)

root.mainloop()
