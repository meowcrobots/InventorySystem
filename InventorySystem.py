import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import sqlite3

root = Tk()
root.title("Inventory System")
root.geometry("1200x600")

conn = sqlite3.connect('Records.db')
c = conn.cursor()

# frame for the search box and buttons
top_frame = tk.Frame(root)
top_frame.pack(fill="x", padx=20, pady=20)

# search box
search_box = tk.Entry(top_frame, width=50)
search_box.pack(side="left", padx=10, fill="x", expand=True)


# add, edit, and delete buttons

# add function
def add_product():
    # function to add a new product to the inventory

    def submit():
        # function to submit the new product details to the table

        product_id = entry_product_id.get()
        name = entry_name.get()
        stocks = entry_stocks.get()
        price = entry_price.get()
        avails = cmb_avail.get()

        # 0-XS, 1-S, 2-M, 3-L, 4-XL
        if (rd_grp.get() == 0):
            cl_size = "XS"
        elif (rd_grp.get() == 1):
            cl_size = "S"
        elif (rd_grp.get() == 2):
            cl_size = "M"
        elif (rd_grp.get() == 3):
            cl_size = "L"
        else:
            cl_size = "XL"

        cl_category = []
        cl_category.append(cb_male.cget("text") if var_male.get() == 1 else 0)
        cl_category.append(cb_fem.cget("text") if var_fem.get() == 1 else 0)
        cl_category.append(cb_uni.cget("text") if var_uni.get() == 1 else 0)
        cl_category.append(cb_shirt.cget("text") if var_shirt.get() == 1 else 0)
        cl_category.append(cb_pants.cget("text") if var_pants.get() == 1 else 0)
        cl_category.append(cb_lsleeve.cget("text") if var_lsleeve.get() == 1 else 0)

        cl_category = ', '.join(item for item in cl_category if item != 0)

        # pangcheck nung nassave na data
        data = {"number": product_id,
                "name": name,
                "stock": stocks,
                "price": price,
                "availability": avails,
                "size:": cl_size,
                "category": cl_category}

        print("Save data: ", data)
        val = product_id
        result = c.execute("""SELECT PID
               FROM inventory
               WHERE PID = ?;""", (val,))
        ans = result.fetchall()
        print(type(ans))

        if len(ans) == 0:
            print('this a pass')
        else:
            print("Product ID is taken")
            messagebox.showerror("Error", "Product ID already exists")
            return
        c.execute("INSERT INTO Inventory VALUES (?, ?, ?, ?, ?, ?, ?)",
                  (product_id, name, avails, stocks, price, cl_size, cl_category))



        conn.commit()
        view()
        add_window.destroy()
        root.deiconify()


    root.withdraw()
    add_window = Toplevel(root)
    add_window.title("Inventory System")
    add_window.geometry("900x400")

    # tile
    title = tk.Label(add_window, text="ADD PRODUCT", font=("Times New Roman", 12))
    title.pack(pady=20, fill="x")
    title.config(anchor="center")

    # frame for the entry widgets
    add_frame = tk.Frame(add_window)
    add_frame.pack(fill="both", expand=True, padx=2, pady=2)

    # column 1 = product_id
    label_product_id = tk.Label(add_frame, font=("Segoe UI", 11), text="Product ID:", pady=8)
    label_product_id.grid(row=0, column=0, sticky="w")

    entry_product_id = tk.Entry(add_frame, font=("Segoe UI", 11))
    entry_product_id.grid(row=0, column=1, padx=22, sticky="w")

    # column 2 = name
    label_name = tk.Label(add_frame, font=("Segoe UI", 11), text="Product Name:", pady=8)
    label_name.grid(row=1, column=0, sticky="w")

    entry_name = tk.Entry(add_frame, font=("Segoe UI", 11))
    entry_name.grid(row=1, column=1, padx=22, sticky="w")

    # Column 3 = Availability
    label_availability = tk.Label(add_frame, font=("Segoe UI", 11), text="Fabric:", pady=8)
    label_availability.grid(row=2, column=0, sticky="w")

    current = tk.StringVar()
    cmb_avail = ttk.Combobox(add_frame, font=("Segoe UI", 10),
                             width=20, textvariable=current)
    cmb_avail['values'] = ('Silk', 'Cotton', 'Wool', 'Linen', 'Worsted')
    cmb_avail.current(0)
    cmb_avail.grid(row=2, column=1, padx=22, sticky="w")

    # column 4 stocks
    label_stocks = tk.Label(add_frame, font=("Segoe UI", 11), text="Stocks:", pady=8)
    label_stocks.grid(row=3, column=0, sticky="w")

    entry_stocks = tk.Entry(add_frame, font=("Segoe UI", 11))
    entry_stocks.grid(row=3, column=1, padx=22, sticky="w")

    # column 5 = price
    label_price = tk.Label(add_frame, font=("Segoe UI", 11), text="Price:", pady=8)
    label_price.grid(row=4, column=0, sticky="w")

    entry_price = tk.Entry(add_frame, font=("Segoe UI", 11))
    entry_price.grid(row=4, column=1, padx=22, sticky="w")

    # column 6 = size
    label_packaging = tk.Label(add_frame, font=("Segoe UI", 11), text="Size:", pady=8)
    label_packaging.grid(row=5, column=0, sticky="w")

    sizes = ['XS', 'S', 'M', 'L               ', 'XL']
    rd_grp = IntVar()
    for index in range(len(sizes)):
        rd_size = Radiobutton(add_frame, font=("Segoe UI", 11), text=sizes[index], variable=rd_grp, value=index)
        rd_size.grid(row=5, column=1 + index, sticky="w")

    # column 7 = category
    label_category = tk.Label(add_frame, font=("Segoe UI", 11), text="Category:", pady=8)
    label_category.grid(row=6, column=0, sticky="w")

    var_male = IntVar()
    cb_male = tk.Checkbutton(add_frame, font=("Segoe UI", 10), text="Male", variable=var_male, onvalue=1, offvalue=0)
    cb_male.grid(row=6, column=1, padx=2, sticky="w")

    var_fem = IntVar()
    cb_fem = tk.Checkbutton(add_frame, font=("Segoe UI", 10), text="Female", variable=var_fem, onvalue=1, offvalue=0)
    cb_fem.grid(row=6, column=2, sticky="w")

    var_uni = IntVar()
    cb_uni = tk.Checkbutton(add_frame, font=("Segoe UI", 10), text="Unisex", variable=var_uni, onvalue=1, offvalue=0)
    cb_uni.grid(row=6, column=3, sticky="w")

    var_shirt = IntVar()
    cb_shirt = tk.Checkbutton(add_frame, font=("Segoe UI", 10), text="Shirt", variable=var_shirt, onvalue=1, offvalue=0)
    cb_shirt.grid(row=7, column=1, sticky="w")

    var_pants = IntVar()
    cb_pants = tk.Checkbutton(add_frame, font=("Segoe UI", 10), text="Pants", variable=var_pants, onvalue=1, offvalue=0)
    cb_pants.grid(row=7, column=2, sticky="w")

    var_lsleeve = IntVar()
    cb_lsleeve = tk.Checkbutton(add_frame, font=("Segoe UI", 10), text="Long Sleeved", variable=var_lsleeve, onvalue=1,
                                offvalue=0)
    cb_lsleeve.grid(row=7, column=3, sticky="w")

    # Add, Back, and close buttons

    # frame for the Add button
    button_frame = tk.Frame(add_frame)
    button_frame.grid(row=1, column=2, padx=25, pady=2)

    add_button = tk.Button(button_frame, text="  Add   ", font=("Segoe UI", 10),
                           width=10, bg="white", command=submit)
    add_button.pack(side="left", pady=2)

    # frame for back button
    def back():
        add_window.destroy()
        root.deiconify()

    button_frame = tk.Frame(add_frame)
    button_frame.grid(row=2, column=2, padx=10, pady=2)

    back_button = tk.Button(button_frame, text="  Back  ", font=("Segoe UI", 10),
                            width=10, bg="white", command=back)
    back_button.pack(side="bottom", pady=2)

    # frame for Close button
    button_frame = tk.Frame(add_frame)
    button_frame.grid(row=3, column=2, padx=50, pady=2)

    close_button = tk.Button(button_frame, text=" Close ", font=("Segoe UI", 10),
                             width=10, bg="white", command=root.quit)
    close_button.pack(side="right", pady=2)


add_button = tk.Button(top_frame, text="Add", font=("Segoe UI", 10), width=10, bg="white", command=add_product)
add_button.pack(side="left", padx=10)


# Edit function
def edit_product():
    # function to edit the details of an existing product in the inventory
    selected_item = tbl_view.selection()

    if selected_item:
        values = tbl_view.item(selected_item[0], "values")
        print(f"Selected values: {values}")
    else:
        print("No item selected")
        messagebox.showerror("Error", "Please select a product to edit")
        return

    def submit():
        # function to submit the updated product details to the table

        product_id = entry_product_id.get()
        name = entry_name.get()
        stocks = entry_stocks.get()
        avails = entry_price.get()
        price = cmb_avail.get()

        # 0-XS, 1-S, 2-M, 3-L, 4-XL
        if (rd_grp.get() == 0):
            cl_size = "XS"
        elif (rd_grp.get() == 1):
            cl_size = "S"
        elif (rd_grp.get() == 2):
            cl_size = "M"
        elif (rd_grp.get() == 3):
            cl_size = "L"
        else:
            cl_size = "XL"

        cl_category = []
        cl_category.append(cb_male.cget("text") if var_male.get() == 1 else 0)
        cl_category.append(cb_fem.cget("text") if var_fem.get() == 1 else 0)
        cl_category.append(cb_uni.cget("text") if var_uni.get() == 1 else 0)
        cl_category.append(cb_shirt.cget("text") if var_shirt.get() == 1 else 0)
        cl_category.append(cb_pants.cget("text") if var_pants.get() == 1 else 0)
        cl_category.append(cb_lsleeve.cget("text") if var_lsleeve.get() == 1 else 0)

        cl_category = ', '.join(item for item in cl_category if item != 0)

        # pangcheck nung inedit na data
        data = {"number": product_id,
                "name": name,
                "stock": stocks,
                "price": price,
                "availability": avails,
                "size:": cl_size,
                "category": cl_category}

        print("Edit data: ", data)

        selected = tbl_view.focus()
        selected_data = tbl_view.item(selected)["values"]
        c.execute('''UPDATE Inventory SET
               PID = ?,
               name = ?,
               stocks = ?,
               price = ?,
               avail = ?,
               size = ?,
               category = ?
               WHERE PID = ? AND name = ?
               ''', (product_id, name, avails, stocks, price, cl_size, cl_category, selected_data[0], selected_data[1]))
        conn.commit()
        view()
        edit_window.destroy()
        root.deiconify()

    root.withdraw()
    edit_window = tk.Toplevel(root)
    edit_window.title("Inventory System")
    edit_window.geometry("900x400")

    # tile
    title = tk.Label(edit_window, text="EDIT PRODUCT", font=("Times New Roman", 12))
    title.pack(pady=20, fill="x")
    title.config(anchor="center")

    # frame for the entry widgets
    add_frame = tk.Frame(edit_window)
    add_frame.pack(fill="both", expand=True, padx=2, pady=2)

    # column 1 = product_id
    label_product_id = tk.Label(add_frame, font=("Segoe UI", 11), text="Product ID:", pady=8)
    label_product_id.grid(row=0, column=0, sticky="w")

    entry_product_id = tk.Entry(add_frame, font=("Segoe UI", 11))
    entry_product_id.grid(row=0, column=1, padx=22, sticky="w")
    entry_product_id.insert(0, tbl_view.item(selected_item)["values"][0])

    # column 2 = name
    label_name = tk.Label(add_frame, font=("Segoe UI", 11), text="Product Name:", pady=8)
    label_name.grid(row=1, column=0, sticky="w")

    entry_name = tk.Entry(add_frame, font=("Segoe UI", 11))
    entry_name.grid(row=1, column=1, padx=22, sticky="w")
    entry_name.insert(0, tbl_view.item(selected_item)["values"][1])

    # Column 3 = Availability
    label_availability = tk.Label(add_frame, font=("Segoe UI", 11), text="Fabric:", pady=8)
    label_availability.grid(row=2, column=0, sticky="w")

    current = tk.StringVar()
    cmb_avail = ttk.Combobox(add_frame, font=("Segoe UI", 10),
                             width=20)
    cmb_avail['values'] = ('Silk', 'Cotton', 'Linen', 'Wool', 'Worsted')
    cmb_avail.grid(row=2, column=1, padx=22, sticky="w")
    cmb_avail.set(tbl_view.item(selected_item)["values"][2])

    # column 4 stocks
    label_stocks = tk.Label(add_frame, font=("Segoe UI", 11), text="Stocks:", pady=8)
    label_stocks.grid(row=3, column=0, sticky="w")

    entry_stocks = tk.Entry(add_frame, font=("Segoe UI", 11))
    entry_stocks.grid(row=3, column=1, padx=22, sticky="w")
    entry_stocks.insert(0, tbl_view.item(selected_item)["values"][3])

    # column 5 = price
    label_price = tk.Label(add_frame, font=("Segoe UI", 11), text="Price:", pady=8)
    label_price.grid(row=4, column=0, sticky="w")

    entry_price = tk.Entry(add_frame, font=("Segoe UI", 11))
    entry_price.grid(row=4, column=1, padx=22, sticky="w")
    entry_price.insert(0, tbl_view.item(selected_item)["values"][4])

    # column 6 = size
    label_packaging = tk.Label(add_frame, font=("Segoe UI", 11), text="Size:", pady=8)
    label_packaging.grid(row=5, column=0, sticky="w")

    sizes = ['XS', 'S', 'M', 'L ', 'XL']
    rd_grp = IntVar()
    for index in range(len(sizes)):
        rd_size = Radiobutton(add_frame, font=("Segoe UI", 11), text=sizes[index], variable=rd_grp, value=index)
        rd_size.grid(row=5, column=1 + index, sticky="w")
        # rd_grp.set(tbl_view.item(selected_item)["values"][5])

    # column 7 = category
    label_category = tk.Label(add_frame, font=("Segoe UI", 11), text="Category:", pady=8)
    label_category.grid(row=6, column=0, sticky="w")

    var_male = IntVar()
    cb_male = tk.Checkbutton(add_frame, font=("Segoe UI", 10), text="Male", variable=var_male, onvalue=1, offvalue=0)
    cb_male.grid(row=6, column=1, padx=2, sticky="w")
    # var_male.set(tbl_view.item(selected_item)["values"][6])

    var_fem = IntVar()
    cb_fem = tk.Checkbutton(add_frame, font=("Segoe UI", 10), text="Female", variable=var_fem, onvalue=1, offvalue=0)
    cb_fem.grid(row=6, column=2, sticky="w")
    # var_fem.set(tbl_view.item(selected_item)["values"][6])

    var_uni = IntVar()
    cb_uni = tk.Checkbutton(add_frame, font=("Segoe UI", 10), text="Unisex", variable=var_uni, onvalue=1, offvalue=0)
    cb_uni.grid(row=6, column=3, sticky="w")
    # var_uni.set(tbl_view.item(selected_item)["values"][6])

    var_shirt = IntVar()
    cb_shirt = tk.Checkbutton(add_frame, font=("Segoe UI", 10), text="Shirt", variable=var_shirt, onvalue=1, offvalue=0)
    cb_shirt.grid(row=7, column=1, sticky="w")
    # var_shirt.set(tbl_view.item(selected_item)["values"][6])

    var_pants = IntVar()
    cb_pants = tk.Checkbutton(add_frame, font=("Segoe UI", 10), text="Pants", variable=var_pants, onvalue=1, offvalue=0)
    cb_pants.grid(row=7, column=2, sticky="w")
    # var_pants.set(tbl_view.item(selected_item)["values"][6])

    var_lsleeve = IntVar()
    cb_lsleeve = tk.Checkbutton(add_frame, font=("Segoe UI", 10), text="Long Sleeved", variable=var_lsleeve, onvalue=1,
                                offvalue=0)
    cb_lsleeve.grid(row=7, column=3, sticky="w")
    # var_lsleeve.set(tbl_view.item(selected_item)["values"][6])

    # Save, Back, and close buttons

    # frame for the Add button
    button_frame = tk.Frame(add_frame)
    button_frame.grid(row=1, column=2, padx=50, pady=2)

    save_button = tk.Button(button_frame, text="  Save  ", font=("Segoe UI", 10), width=10, bg="white", command=submit)
    save_button.pack(side="left", pady=2)

    # frame for back button
    def back():
        edit_window.destroy()
        root.deiconify()

    button_frame = tk.Frame(add_frame)
    button_frame.grid(row=2, column=2, padx=10, pady=2)

    back_button = tk.Button(button_frame, text="  Back  ", font=("Segoe UI", 10),
                            width=10, bg="white", command=back)
    back_button.pack(side="bottom", pady=2)

    # frame for Close button
    button_frame = tk.Frame(add_frame)
    button_frame.grid(row=3, column=2, padx=50, pady=2)

    close_button = tk.Button(button_frame, text=" Close ", font=("Segoe UI", 10),
                             width=10, bg="white", command=root.quit)
    close_button.pack(side="right", pady=2)


# call the function to open the edit window
edit_button = tk.Button(top_frame, text="Edit", font=("Segoe UI", 10), width=10, bg="white", command=edit_product)
edit_button.pack(side="left", padx=10)


# delete function
def delete_product():
    selected = tbl_view.focus()
    selected_data = tbl_view.item(selected)["values"]

    print("Deleted item data: ", selected_data)
    selected_item = tbl_view.selection()
    if selected_item:
        result = messagebox.askyesno("Inventory System", "Are you sure you want to delete the selected item?")
        if result:
            tbl_view.delete(selected_item)
    else:
        messagebox.showerror("Inventory System", "Please select an item to delete.")
    query = "DELETE FROM Inventory WHERE PID = ? AND name = ?"
    c.execute(query, (selected_data[0], selected_data[1]))
    conn.commit()


delete_button = tk.Button(top_frame, text="Delete", font=("Segoe UI", 10), width=10, bg="white", command=delete_product)
delete_button.pack(side="left", padx=10)


def search():
    # get entry from search box then hanapin yung entry sa database
    searchID = search_box.get();

    # Get a certain value from the TreeView

    target_item = None
    for item in tbl_view.get_children():
        val = tbl_view.item(item, "val")
        if val[0] == searchID:
            target_item = item
            break

    if target_item:
        val = tbl_view.item(target_item, "values")
        print(f"Values for item {target_item}: {val}")
    else:
        print("Target item not found")

    for item in tbl_view.get_children():
        tbl_view.delete(item)

    c.execute("SELECT * FROM Inventory WHERE PID = ?", (searchID))
    searchable_data = c.fetchall()
    tbl_view.insert('', tk.END, values=searchable_data[0])


# search button
search_button = tk.Button(top_frame, text="Search", font=("Segoe UI", 10), width=10, bg="white", command=search)
search_button.pack(side="left", padx=10)

# frame for records
list_frame = tk.Frame(root)
list_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Table for records
tbl_column = ('prodID', 'prodName', 'prodAvail', 'prodStocks', 'prodPrice', 'prodSize', 'prodCat')
tbl_view = ttk.Treeview(list_frame, columns=tbl_column, show='headings')

tbl_view.column("prodID", anchor=CENTER, stretch=NO, width=200)
tbl_view.heading("prodID", text="Product ID")

tbl_view.column("prodName", anchor=CENTER, stretch=NO, width=250)
tbl_view.heading("prodName", text="Product Name")

tbl_view.column("prodAvail", anchor=CENTER, stretch=NO, width=150)
tbl_view.heading("prodAvail", text="Fabric")

tbl_view.column("prodStocks", anchor=CENTER, stretch=NO, width=150)
tbl_view.heading("prodStocks", text="Stocks")

tbl_view.column("prodPrice", anchor=CENTER, stretch=NO, width=200)
tbl_view.heading("prodPrice", text="Price")

tbl_view.column("prodSize", anchor=CENTER, stretch=NO, width=150)
tbl_view.heading("prodSize", text="Size")

tbl_view.column("prodCat", anchor=CENTER, stretch=NO, width=350)
tbl_view.heading("prodCat", text="Category")


# # sample records
# records = []  # Get actual records from DB
# for n in range(1, 5):  # To be removed(?)
#     records.append((f'ProdID{n}', f'ProdName{n}', f'Available',
#                     f'{n}', f'150', f'L', f'Unisex, Pants'))
#
# # Writes the records to the GUI
# for record in records:
#     tbl_view.insert('', tk.END, values=record)


def view():
    # Writes the records to the GUI
    records = c.execute("SELECT * FROM Inventory")

    for item in tbl_view.get_children():
        tbl_view.delete(item)

    for record in records:
        tbl_view.insert('', tk.END, values=record)


view()
tbl_view.pack(fill="both", expand=True)

# scrollbar
sbar = ttk.Scrollbar(list_frame, orient=tk.HORIZONTAL, command=tbl_view.xview)
tbl_view.configure(xscroll=sbar.set)
sbar.pack(fill="both")

# frame for the View Graph and Close buttons
bottom_frame = tk.Frame(root)
bottom_frame.pack(fill="x", padx=20, pady=20)

# buttons
view_graph_button = tk.Button(bottom_frame, text="View Graph", font=("Segoe UI", 10), width=10, bg="white")
view_graph_button.pack(side="left", padx=10)

close_button = tk.Button(bottom_frame, text="Close", font=("Segoe UI", 10), width=10, bg="white", command=root.quit)
close_button.pack(side="left", padx=10)

root.mainloop()
