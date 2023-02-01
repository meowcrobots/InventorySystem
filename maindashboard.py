import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Inventory System")
root.geometry("800x600")

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
add_button = tk.Button(top_frame, text="Add")
add_button.pack(side="left", padx=10)

edit_button = tk.Button(top_frame, text="Edit")
edit_button.pack(side="left", padx=10)

delete_button = tk.Button(top_frame, text="Delete")
delete_button.pack(side="left", padx=10)

#frame for records
list_frame = tk.Frame(root)
list_frame.pack(fill="both", expand=True, padx=20, pady=20)

#Table for records
product_list = ttk.Treeview(list_frame, columns=("number", "name", "category", "stocks", "price", "availability", "packaging"), show="headings")
product_list.pack(fill="both", expand=True)

product_list.column("number", width=100, anchor="center")
product_list.column("name", width=200, anchor="center")
product_list.column("category", width=100, anchor="center")
product_list.column("stocks", width=100, anchor="center")
product_list.column("price", width=100, anchor="center")
product_list.column("availability", width=100, anchor="center")
product_list.column("packaging", width=100, anchor="center")

product_list.heading("number", text="Item No.")
product_list.heading("name", text="Item Name")
product_list.heading("category", text="Category")
product_list.heading("stocks", text="Stocks")
product_list.heading("price", text="Price")
product_list.heading("availability", text="Availability")
product_list.heading("packaging", text="Packaging")

#sample records
for i in range(1, 6):
    product_list.insert("", tk.END, values=("ProductID{}".format(i), "Name {}".format(i), "Category {}".format(i), i * 10, i * 100, "Available", "Packaging {}".format(i)))

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
