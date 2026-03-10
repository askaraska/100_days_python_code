from tkinter import *


def mile_to_km():
    km = round(float(miles_input.get()) * 1.609)
    kilometer_result_label.config(text=f"{km}")

#creating the window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=120)
window.config(padx=20, pady=20)

# Miles input
# miles_input = Entry()
miles_input = Entry(width=8, justify="center")
miles_input.grid(column=1, row=0)

# create label
miles_label = Label(text="Miles", font=("Arial", 14))
miles_label.grid(column=2, row=0)

# Is equal to label
is_equal_label = Label(text="is equal to", font=("Arial", 14))
is_equal_label.grid(column=0, row=1)

# Result label/kilo label
kilometer_result_label = Label(text="0", font=("Arial", 14))
kilometer_result_label.grid(column=1, row=1)

# KM label
km_label = Label(text="Km", font=("Arial", 14))
km_label.grid(column=2, row=1)

# Calculate button
calculate_button = Button(text="Calculate", command=mile_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()