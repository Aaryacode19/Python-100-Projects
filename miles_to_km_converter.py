from tkinter import *
def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")
window = Tk()
window.title("Miles to km converter")
window.config(padx=20, pady=20)


miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

calc_button = Button(text="calculate", command=miles_to_km)
calc_button.grid(column=1, row=2)
