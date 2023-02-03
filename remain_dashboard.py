import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *

root = tk.Tk()
root.title("Inventory System")
root.geometry("1200x600")

#frame for the search box and buttons
top_frame = tk.Frame(root)
top_frame.pack(fill="x", padx=20, pady=20)

#search box
search_box = tk.Entry(top_frame, width=50)
search_box.pack(side="left", padx=10, fill="x", expand=True)

#search button
search_button = tk.Button(top_frame, text="Search")
search_button.pack(side="left", padx=10)


#add, edit, and delete buttons

#add function
def add_product():
    # function to add a new product to the inventory

    def submit():
        # function to submit the new product details to the table

        product_id = entry_product_id.get()
        name = entry_name.get()
        availability = entry_availability.get()
        stocks = entry_stocks.get()
        price = entry_price.get()
        packaging = packaging_var.get()
        category = category_var.get()

        product_list.insert("", tk.END, values=(product_id, name, availability, stocks, price, packaging, category))
        
        add_window.destroy()
        root.deiconify()

    root.withdraw()
    add_window = tk.Toplevel(root)
    add_window.title("Inventory System")
    add_window.geometry("750x325")
    
    #tile
    title = tk.Label(add_window, text="ADD PRODUCT", font=("Times New Roman", 12))
    title.pack(pady=20, fill="x")
    title.config(anchor="center")

    #frame for the entry widgets
    add_frame = tk.Frame(add_window)
    add_frame.pack(fill="both", expand=True, padx=2, pady=2)

    #column 1 = product_id
    label_product_id = tk.Label(add_frame, text="Product ID:")
    label_product_id.grid(row=0, column=0, padx=10, sticky="w")

    entry_product_id = tk.Entry(add_frame)
    entry_product_id.grid(row=0, column=1, padx=10, sticky="ew")

    #column 2 = name
    label_name = tk.Label(add_frame, text="Product Name:")
    label_name.grid(row=1, column=0, padx=10, sticky="w")

    entry_name = tk.Entry(add_frame)
    entry_name.grid(row=1, column=1, padx=10, sticky="ew")

    # Column 3 = Availability
    label_availability = tk.Label(add_frame, text="Availability:")
    label_availability.grid(row=2, column=0, padx=10, sticky="w")

    entry_availability = ttk.Combobox(add_frame, values=["Available", "Not Available"])
    entry_availability.grid(row=2, column=1, padx=10, sticky="ew")

    #column 4 stocks
    label_stocks = tk.Label(add_frame, text="Stocks:")
    label_stocks.grid(row=3, column=0, padx=10, sticky="w")

    entry_stocks = tk.Entry(add_frame)
    entry_stocks.grid(row=3, column=1, padx=10, sticky="ew")

    #column 5 = price
    label_price = tk.Label(add_frame, text="Price:")
    label_price.grid(row=4, column=0, padx=10, sticky="w")

    entry_price = tk.Entry(add_frame)
    entry_price.grid(row=4, column=1, padx=10, sticky="ew")

    #column 6 = packaging
    label_packaging = tk.Label(add_frame, text="Packaging:")
    label_packaging.grid(row=5, column=0, padx=10, sticky="w")

    packaging_var = tk.StringVar(value="none")

    entry_packaging = tk.Radiobutton(add_frame, text="Fragile", variable=packaging_var, value="Fragile")
    entry_packaging.grid(row=5, column=1, padx=2, sticky="w")

    entry_packaging = tk.Radiobutton(add_frame, text="Non-fragile", variable=packaging_var, value="Non-fragile")
    entry_packaging.grid(row=5, column=1, padx=90, sticky="w")

    #column 7 = category
    label_category = tk.Label(add_frame, text="Category:")
    label_category.grid(row=6, column=0, padx=10, sticky="w")

    category_var = tk.StringVar()

    entry_category = tk.Checkbutton(add_frame, text="Category 1", variable=category_var, onvalue="Category 1", offvalue="")
    entry_category.grid(row=6, column=1, padx=2, pady=5, sticky="w")

    entry_category = tk.Checkbutton(add_frame, text="Category 2", variable=category_var, onvalue="Category 2", offvalue="")
    entry_category.grid(row=6, column=1, padx=110, sticky="w")

    entry_category = tk.Checkbutton(add_frame, text="Category 3", variable=category_var, onvalue="Category 3", offvalue="")
    entry_category.grid(row=6, column=1, padx=220, sticky="w")
    
    entry_category = tk.Checkbutton(add_frame, text="Category 4", variable=category_var, onvalue="Category 4", offvalue="")
    entry_category.grid(row=7, column=1, padx=2, sticky="w")

    entry_category = tk.Checkbutton(add_frame, text="Category 5", variable=category_var, onvalue="Category 5", offvalue="")
    entry_category.grid(row=7, column=1, padx=110, sticky="w")

    entry_category = tk.Checkbutton(add_frame, text="Category 6", variable=category_var, onvalue="Category 6", offvalue="")
    entry_category.grid(row=7, column=1, padx=220, sticky="w")

    #Add, Back, and close buttons

    #frame for the Add button
    button_frame = tk.Frame(add_frame)
    button_frame.grid(row=1, column=2, padx=50, pady=2)
    
    add_button = tk.Button(button_frame, text="  Add   ", command=submit)
    add_button.pack(side="left", pady=2)

    #frame for back button
    def back():
        add_window.destroy()
        root.deiconify()
    button_frame = tk.Frame(add_frame)
    button_frame.grid(row=2, column=2, padx=10, pady=2)

    back_button = tk.Button(button_frame, text="  Back  ", command=back)
    back_button.pack(side="bottom", pady=2)

    #frame for Close button
    button_frame = tk.Frame(add_frame)
    button_frame.grid(row=3, column=2, padx=50, pady=2)

    close_button = tk.Button(button_frame, text=" Close ", command=root.quit)
    close_button.pack(side="right", pady=2)

add_button = tk.Button(top_frame, text="Add", command=add_product)
add_button.pack(side="left", padx=10)

#Edit function
def edit_product():
    # function to edit the details of an existing product in the inventory

    def submit():
        # function to submit the updated product details to the table

        selected_item = product_list.selection()[0]
        product_list.item(selected_item, values=(entry_product_id.get(),
                                                  entry_name.get(),
                                                  entry_availability.get(),
                                                  entry_stocks.get(),
                                                  entry_price.get(),
                                                  packaging_var.get(),
                                                  category_var.get()))
        edit_window.destroy()
        root.deiconify()

    try:
        selected_item = product_list.selection()[0]
    except IndexError:
        messagebox.showerror("Error", "Please select a product to edit")
        return

    root.withdraw()
    edit_window = tk.Toplevel(root)
    edit_window.title("Inventory System")
    edit_window.geometry("750x325")

    #tile
    title = tk.Label(edit_window, text="EDIT PRODUCT", font=("Times New Roman", 12))
    title.pack(pady=20, fill="x")
    title.config(anchor="center")

    #frame for the entry widgets
    add_frame = tk.Frame(edit_window)
    add_frame.pack(fill="both", expand=True, padx=2, pady=2)

    #column 1 = product_id
    label_product_id = tk.Label(add_frame, text="Product ID:")
    label_product_id.grid(row=0, column=0, padx=10, sticky="w")

    entry_product_id = tk.Entry(add_frame)
    entry_product_id.grid(row=0, column=1, padx=10, sticky="ew")
    entry_product_id.insert(0, product_list.item(selected_item)["values"][0])

    #column 2 = name
    label_name = tk.Label(add_frame, text="Product Name:")
    label_name.grid(row=1, column=0, padx=10, sticky="w")

    entry_name = tk.Entry(add_frame)
    entry_name.grid(row=1, column=1, padx=10, sticky="ew")
    entry_name.insert(0, product_list.item(selected_item)["values"][1])

    # Column 3 = Availability
    label_availability = tk.Label(add_frame, text="Availability:")
    label_availability.grid(row=2, column=0, padx=10, sticky="w")

    entry_availability = ttk.Combobox(add_frame, values=["Available", "Not Available"])
    entry_availability.grid(row=2, column=1, padx=10, sticky="ew")
    entry_availability.set(product_list.item(selected_item)["values"][2])

    #column 4 stocks
    label_stocks = tk.Label(add_frame, text="Stocks:")
    label_stocks.grid(row=3, column=0, padx=10, sticky="w")


    entry_stocks = tk.Entry(add_frame)
    entry_stocks.grid(row=3, column=1, padx=10, sticky="ew")
    entry_stocks.insert(0, product_list.item(selected_item)["values"][3])

    #column 5 price
    label_price = tk.Label(add_frame, text="Price:")
    label_price.grid(row=4, column=0, padx=10, sticky="w")

    entry_price = tk.Entry(add_frame)
    entry_price.grid(row=4, column=1, padx=10, sticky="ew")
    entry_price.insert(0, product_list.item(selected_item)["values"][4])

    #column 6 packaging
    label_packaging = tk.Label(add_frame, text="Packaging:")
    label_packaging.grid(row=5, column=0, padx=10, sticky="w")

    packaging_var = tk.StringVar(value="none")

    entry_packaging = tk.Radiobutton(add_frame, text="Fragile", variable=packaging_var, value="Fragile")
    entry_packaging.grid(row=5, column=1, padx=2, sticky="w")
    packaging_var.set(product_list.item(selected_item)["values"][5])

    entry_packaging = tk.Radiobutton(add_frame, text="Non-fragile", variable=packaging_var, value="Non-fragile")
    entry_packaging.grid(row=5, column=1, padx=90, sticky="w")
    packaging_var.set(product_list.item(selected_item)["values"][5])

    #column 7 category
    label_category = tk.Label(add_frame, text="Category:")
    label_category.grid(row=6, column=0, padx=10, sticky="w")

    category_var = tk.StringVar()

    entry_category = tk.Checkbutton(add_frame, text="Category 1", variable=category_var, onvalue="Category 1", offvalue="")
    entry_category.grid(row=6, column=1, padx=2, pady=5, sticky="w")
    category_var.set(product_list.item(selected_item)["values"][6])

    entry_category = tk.Checkbutton(add_frame, text="Category 2", variable=category_var, onvalue="Category 2", offvalue="")
    entry_category.grid(row=6, column=1, padx=110, sticky="w")
    category_var.set(product_list.item(selected_item)["values"][6])

    entry_category = tk.Checkbutton(add_frame, text="Category 3", variable=category_var, onvalue="Category 3", offvalue="")
    entry_category.grid(row=6, column=1, padx=220, sticky="w")
    category_var.set(product_list.item(selected_item)["values"][6])

    entry_category = tk.Checkbutton(add_frame, text="Category 4", variable=category_var, onvalue="Category 4", offvalue="")
    entry_category.grid(row=7, column=1, padx=2, sticky="w")
    category_var.set(product_list.item(selected_item)["values"][6])

    entry_category = tk.Checkbutton(add_frame, text="Category 5", variable=category_var, onvalue="Category 5", offvalue="")
    entry_category.grid(row=7, column=1, padx=110, sticky="w")
    category_var.set(product_list.item(selected_item)["values"][6])

    entry_category = tk.Checkbutton(add_frame, text="Category 6", variable=category_var, onvalue="Category 6", offvalue="")
    entry_category.grid(row=7, column=1, padx=220, sticky="w")
    category_var.set(product_list.item(selected_item)["values"][6])

    #Save, Back, and close buttons

    #frame for the Add button
    button_frame = tk.Frame(add_frame)
    button_frame.grid(row=1, column=2, padx=50, pady=2)
    
    save_button = tk.Button(button_frame, text="  Save  ", command=submit)
    save_button.pack(side="left", pady=2)

    #frame for back button
    def back():
        edit_window.destroy()
        root.deiconify()
    button_frame = tk.Frame(add_frame)
    button_frame.grid(row=2, column=2, padx=10, pady=2)

    back_button = tk.Button(button_frame, text="  Back  ", command=back)
    back_button.pack(side="bottom", pady=2)

    #frame for Close button
    button_frame = tk.Frame(add_frame)
    button_frame.grid(row=3, column=2, padx=50, pady=2)

    close_button = tk.Button(button_frame, text=" Close ", command=root.quit)
    close_button.pack(side="right", pady=2)

#call the function to open the edit window
edit_button = tk.Button(top_frame, text="Edit", command=edit_product)
edit_button.pack(side="left", padx=10)


#delete function 
def delete_product():
    selected_item = product_list.selection()
    if selected_item:
        result = messagebox.askyesno("Inventory System", "Are you sure you want to delete the selected item?")
        if result:
            product_list.delete(selected_item)
    else:
        messagebox.showerror("Inventory System", "Please select an item to delete.")


delete_button = tk.Button(top_frame, text="Delete", command=delete_product)
delete_button.pack(side="left", padx=10)

#frame for records
list_frame = tk.Frame(root)
list_frame.pack(fill="both", expand=True, padx=20, pady=20)

#Table for records
product_list = ttk.Treeview(list_frame, columns=("number", "name", "availability", "stocks", "price", "packaging", "category"), show="headings")
product_list.pack(fill="both", expand=True)

product_list.column("number", width=100, anchor="center")
product_list.column("name", width=200, anchor="center")
product_list.column("availability", width=100, anchor="center")
product_list.column("stocks", width=100, anchor="center")
product_list.column("price", width=100, anchor="center")
product_list.column("packaging", width=100, anchor="center")
product_list.column("category", width=100, anchor="center")

product_list.heading("number", text="Item No.")
product_list.heading("name", text="Item Name")
product_list.heading("availability", text="Availability")
product_list.heading("stocks", text="Stocks")
product_list.heading("price", text="Price")
product_list.heading("packaging", text="Packaging")
product_list.heading("category", text="Category")

#sample records
for i in range(1, 6):
    product_list.insert("", tk.END, values=("ProductID{}".format(i), "Name {}".format(i), "Available", i * 10, i * 100, "Packaging {}".format(i), "Category {}".format(i)))

#scrollbar
scrollbar = ttk.Scrollbar(list_frame, orient="horizontal")
scrollbar.config(command=product_list.yview)
scrollbar.pack(side="right", fill="y")

#frame for the View Graph and Close buttons
bottom_frame = tk.Frame(root)
bottom_frame.pack(fill="x", padx=20, pady=20)

#buttons
view_graph_button = tk.Button(bottom_frame, text="View Graph")
view_graph_button.pack(side="left", padx=10)

close_button = tk.Button(bottom_frame, text="Close", command=root.quit)
close_button.pack(side="left", padx=10)

root.mainloop()
