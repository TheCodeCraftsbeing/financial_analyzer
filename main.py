# main.py
import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
from tkcalendar import DateEntry
from modules.data_input import load_from_file
from modules.data_processing import generate_summaries, get_subcategories, add_subcategory, delete_subcategory
from modules.insights import subcategory_insights
from modules.visualization import combined_pie_chart

# Function to add a transaction
def add_transaction():
    date = entry_date.get()
    description = entry_description.get()
    category = entry_category.get()
    subcategory = entry_subcategory.get()
    amount = entry_amount.get()

    if not (date and description and category and subcategory and amount):
        messagebox.showerror("Input Error", "All fields are required.")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Input Error", "Amount must be a number.")
        return

    # Adjust amount based on category
    if category == "expense":
        amount = -abs(amount)  # Ensure amount is negative for expenses
    elif category == "income":
        amount = abs(amount)   # Ensure amount is positive for income

    with open("data/transactions.csv", "a") as file:
        file.write(f"{date},{description},{category},{subcategory},{amount}\n")

    messagebox.showinfo("Success", "Transaction added successfully.")
    clear_entries()

def clear_entries():
    entry_date.delete(0, tk.END)
    entry_description.delete(0, tk.END)
    #entry_category.delete(0, tk.END)
    #entry_subcategory.delete(0, tk.END)
    entry_amount.delete(0, tk.END)

def update_subcategories(event):
    selected_category = entry_category.get()
    subcategories = get_subcategories(selected_category)
    entry_subcategory.config(values=subcategories)
    entry_subcategory.set(subcategories[0] if subcategories else "")

def add_new_subcategory():
    new_subcategory = simpledialog.askstring("New Subcategory", "Enter new subcategory name:")
    if new_subcategory:
        if add_subcategory(entry_category.get(), new_subcategory):
            messagebox.showinfo("Success", f"Subcategory '{new_subcategory}' added successfully.")
            update_subcategories(None)  # Update subcategory dropdown
        else:
            messagebox.showerror("Error", f"Subcategory '{new_subcategory}' already exists under category '{entry_category.get()}'. Try a different name.")

def delete_existing_subcategory():
    subcategory_to_delete = entry_subcategory.get()
    if subcategory_to_delete:
        delete_subcategory(entry_category.get(), subcategory_to_delete)
        messagebox.showinfo("Success", f"Subcategory '{subcategory_to_delete}' deleted successfully.")
        update_subcategories(None)  # Update subcategory dropdown

def analyze_data():
    data = load_from_file("data/transactions.csv")
    monthly_summary, weekly_summary = generate_summaries(data)
    print("Monthly Summary:")
    print(monthly_summary)
    print("Weekly Summary:")
    print(weekly_summary)
    subcategory_insights(data)
    combined_pie_chart(data)

# Create the main window
root = tk.Tk()
root.title("Financial Analyzer")

# Create and place widgets for input
tk.Label(root, text="Date (DD-MM-YYYY)").grid(row=0, column=0)
entry_date = DateEntry(root, date_pattern='dd-mm-yyyy')
entry_date.grid(row=0, column=1)

tk.Label(root, text="Description").grid(row=1, column=0)
entry_description = tk.Entry(root)
entry_description.grid(row=1, column=1)

tk.Label(root, text="Category").grid(row=2, column=0)
entry_category = tk.StringVar(value="expense")
category_dropdown = ttk.Combobox(root, textvariable=entry_category, values=["expense", "income"])
category_dropdown.grid(row=2, column=1)
category_dropdown.bind("<<ComboboxSelected>>", update_subcategories)

tk.Label(root, text="Subcategory").grid(row=3, column=0)
entry_subcategory = ttk.Combobox(root, values=[], state="readonly")
entry_subcategory.grid(row=3, column=1)

tk.Label(root, text="Amount").grid(row=4, column=0)
entry_amount = tk.Entry(root)
entry_amount.grid(row=4, column=1)

tk.Button(root, text="Add Transaction", command=add_transaction).grid(row=5, column=0, columnspan=2)
tk.Button(root, text="Analyze Data", command=analyze_data).grid(row=6, column=0, columnspan=2)
tk.Button(root, text="Clear Entry", command=clear_entries).grid(row=7, column=0, columnspan=2)
tk.Button(root, text="Add New Subcategory", command=add_new_subcategory).grid(row=8, column=0, columnspan=2)
tk.Button(root, text="Delete Subcategory", command=delete_existing_subcategory).grid(row=9, column=0, columnspan=2)

# Start the main loop
root.mainloop()
