from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button, messagebox
from tkcalendar import DateEntry
from datetime import datetime
from reports_manager import ReportsManager

window = Tk()

window.title("Reports Manager")
window.config(padx=30, pady=30)

logo = PhotoImage(file="report.png")
canvas = Canvas(width=160, height=150)
canvas.create_image(90, 75, image=logo)
canvas.grid(row=0, column=1)


def get_input():
    reports_manager = ReportsManager(login_entry.get(), password_entry.get(), start_cal.get_date(), end_cal.get_date())
    reports_manager.generate_reports()

# Login 
login_label = Label(text="Login: ")
login_label.grid(row=1, column=0)
login_entry = Entry(width=25)
login_entry.grid(row=1, column=1)

# Password 
password_label = Label(text="Password:")
password_label.grid(row=2, column=0)
password_entry = Entry(width=25)
password_entry.grid(row=2, column=1)

start_time_label = Label(text="Start time:")
start_time_label.grid(row=3, column=0)
current_date = datetime.now()
start_cal = DateEntry(window, width=22, year=current_date.year, month=current_date.month, day=current_date.day, 
background='darkblue', foreground='white', borderwidth=2)
start_cal.grid(row=3, column=1)


end_time_label = Label(text="End time:")
end_time_label.grid(row=4, column=0)
end_cal = DateEntry(window, width=22, year=current_date.year, month=current_date.month, day=current_date.day, 
background='darkblue', foreground='white', borderwidth=2)
end_cal.grid(row=4, column=1)

generate_reports_button = Button(text="Generate Reports", command=get_input)
generate_reports_button.grid(row=5, column=1)
generate_reports_button.config(padx=5, pady=5)
window.mainloop()