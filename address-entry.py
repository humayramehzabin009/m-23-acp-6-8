from tkinter import *

# Function to calculate interest
def calculate_interest():
    try:
        # Retrieve input values
        principal = float(ent_principal.get())
        rate = float(ent_rate.get())
        time = float(ent_time.get())

        # Simple Interest formula: SI = (P * R * T) / 100
        interest = (principal * rate * time) / 100

        # Display the result
        lbl_result["text"] = f"Interest: ₹{round(interest, 2)}"
    except ValueError:
        lbl_result["text"] = "Invalid input! Please enter numeric values."

# Set up the main window
window = Tk()
window.title("Address Entry & Interest Calculator")
window.geometry("400x400")
window.resizable(False, False)

# Create input fields and labels
Label(window, text="Name:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
ent_name = Entry(window, width=30)
ent_name.grid(row=0, column=1, padx=10, pady=10)

Label(window, text="Address:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
ent_address = Entry(window, width=30)
ent_address.grid(row=1, column=1, padx=10, pady=10)

Label(window, text="Principal Amount (₹):").grid(row=2, column=0, padx=10, pady=10, sticky="w")
ent_principal = Entry(window, width=30)
ent_principal.grid(row=2, column=1, padx=10, pady=10)

Label(window, text="Rate of Interest (%):").grid(row=3, column=0, padx=10, pady=10, sticky="w")
ent_rate = Entry(window, width=30)
ent_rate.grid(row=3, column=1, padx=10, pady=10)

Label(window, text="Time (Years):").grid(row=4, column=0, padx=10, pady=10, sticky="w")
ent_time = Entry(window, width=30)
ent_time.grid(row=4, column=1, padx=10, pady=10)

# Create a Calculate button
btn_calculate = Button(window, text="Calculate Interest", command=calculate_interest)
btn_calculate.grid(row=5, column=0, columnspan=2, pady=20)

# Result label
lbl_result = Label(window, text="Interest: ₹0.00", font=("Arial", 12, "bold"))
lbl_result.grid(row=6, column=0, columnspan=2, pady=10)

# Run the application
window.mainloop()
