import tkinter as tk

def meters_to_feet():
    """Convert the value from meters to feet and display the result."""
    meters = ent_length.get()
    feet = float(meters) * 3.28084
    lbl_result["text"] = f"{round(feet, 2)} feet"

def feet_to_meters():
    """Convert the value from feet to meters and display the result."""
    feet = ent_length.get()
    meters = float(feet) / 3.28084
    lbl_result["text"] = f"{round(meters, 2)} meters"

# Set up the window
window = tk.Tk()
window.title("Length Converter")
window.resizable(width=False, height=False)

# Create the input frame with an Entry widget and label
frm_entry = tk.Frame(master=window)
ent_length = tk.Entry(master=frm_entry, width=10)
lbl_unit = tk.Label(master=frm_entry, text="meters")

# Layout the Entry and Label in frm_entry using grid
ent_length.grid(row=0, column=0, sticky="e")
lbl_unit.grid(row=0, column=1, sticky="w")

# Create the conversion Buttons and result display Label
btn_to_feet = tk.Button(
    master=window,
    text="Convert to Feet",
    command=meters_to_feet
)
btn_to_meters = tk.Button(
    master=window,
    text="Convert to Meters",
    command=feet_to_meters
)
lbl_result = tk.Label(master=window, text="Result")

# Layout the widgets using grid
frm_entry.grid(row=0, column=0, padx=10)
btn_to_feet.grid(row=1, column=0, pady=5)
btn_to_meters.grid(row=2, column=0, pady=5)
lbl_result.grid
