import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3


# Window
root = Tk()
root.resizable(0, 0)
root.geometry("950x600")
root.title("Faculty Record")

# Create DB here
# con.connect something something
conn = sqlite3.connect('Records.db')
c = conn.cursor()

# Functions


def save():
    # Get the inputted data in the GUI
    faculty_number = txt_fnum.get()
    faculty_name = txt_fname.get()
    faculty_status = cmb_status.get()

    # 0 = Computer Science Department, 1 = Information System,
    # 2 = Information Technology
    if(rd_grp.get() == 0):
        faculty_department = "Computer Science"
    elif (rd_grp.get() == 1):
        faculty_department = "Information System"
    else:
        faculty_department = "Information Technology"

    # Takes all selected subjects, else writes 0
    faculty_subjects = []
    faculty_subjects.append(cb_prog.cget(
        "text") if var_prog.get() == 1 else 0)
    faculty_subjects.append(cb_dbase.cget(
        "text") if var_dbase.get() == 1 else 0)
    faculty_subjects.append(cb_dtcom.cget(
        "text") if var_dtcom.get() == 1 else 0)
    faculty_subjects.append(cb_thesis.cget(
        "text") if var_thesis.get() == 1 else 0)
    faculty_subjects.append(cb_compdes.cget(
        "text") if var_compdes.get() == 1 else 0)
    faculty_subjects.append(cb_softeng.cget(
        "text") if var_softeng.get() == 1 else 0)

    # Retains subjects that are not = 0, not selected
    faculty_subjects = ', '.join(
        item for item in faculty_subjects if item != 0)

    # FOR CHECKING: PRINTS VALUES TO BE SAVED
    # data = {"number": faculty_number,
    #         "name": faculty_name,
    #         "status": faculty_status,
    #         "department": faculty_department,
    #         "subjects": faculty_subjects}
    #
    # print("Save data: ", data)

    c.execute("INSERT INTO Records VALUES (?, ?, ?, ?, ?)",
             (faculty_number, faculty_name, faculty_status, faculty_department, faculty_subjects))
    conn.commit()

def edit():
    # Get the inputted data in the GUI
    faculty_number = txt_fnum.get()
    faculty_name = txt_fname.get()
    faculty_status = cmb_status.get()

    # 0 = Computer Science Department, 1 = Information System,
    # 2 = Information Technology
    if(rd_grp.get() == 0):
        faculty_department = "Computer Science"
    elif (rd_grp.get() == 1):
        faculty_department = "Information System"
    else:
        faculty_department = "Information Technology"

    # Takes all selected subjects, else writes 0
    faculty_subjects = []
    faculty_subjects.append(cb_prog.cget(
        "text") if var_prog.get() == 1 else 0)
    faculty_subjects.append(cb_dbase.cget(
        "text") if var_dbase.get() == 1 else 0)
    faculty_subjects.append(cb_dtcom.cget(
        "text") if var_dtcom.get() == 1 else 0)
    faculty_subjects.append(cb_thesis.cget(
        "text") if var_thesis.get() == 1 else 0)
    faculty_subjects.append(cb_compdes.cget(
        "text") if var_compdes.get() == 1 else 0)
    faculty_subjects.append(cb_softeng.cget(
        "text") if var_softeng.get() == 1 else 0)

    # Retains subjects that are not = 0, not selected
    faculty_subjects = ', '.join(
        item for item in faculty_subjects if item != 0)

    input_data = {"number": faculty_number,
                  "name": faculty_name,
                  "status": faculty_status,
                  "department": faculty_department,
                  "subjects": faculty_subjects}

    print("Edit data: ", input_data)
    selected = tbl_view.focus()
    selected_data = tbl_view.item(selected)["values"]
    editable_index = int(selected_data[0])-1

    c.execute('''UPDATE Records SET
        numuber = ?,
        name = ?,
        status = ?,
        department = ?,
        subjects = ?
        WHERE numuber = ? AND name = ?
        ''', (faculty_number, faculty_name, faculty_status, faculty_department, faculty_subjects, selected_data[0], selected_data[1]))

    conn.commit()



def delete():

    selected = tbl_view.focus()
    selected_data = tbl_view.item(selected)["values"]

    print("Deleted item data: ", selected_data)

    query = "DELETE FROM Records WHERE numuber = ? AND name = ?"
    c.execute(query,(selected_data[0],selected_data[1],))
    conn.commit()


def view():

    # Writes the records to the GUI
    records = c.execute("SELECT * FROM Records")

    for item in tbl_view.get_children():
        tbl_view.delete(item)

    for record in records:
        tbl_view.insert('', tk.END, values=record)



def search():
    # To change with records from DB, filter first using filter data
    # Get the inputted data in the GUI
    faculty_number = txt_fnum.get()
    faculty_name = txt_fname.get()
    faculty_status = cmb_status.get()

    # 0 = Computer Science Department, 1 = Information System,
    # 2 = Information Technology
    if(rd_grp.get() == 0):
        faculty_department = "Computer Science"
    elif (rd_grp.get() == 1):
        faculty_department = "Information System"
    else:
        faculty_department = "Information Technology"

    # Takes all selected subjects, else writes 0
    faculty_subjects = []
    faculty_subjects.append(cb_prog.cget(
        "text") if var_prog.get() == 1 else 0)
    faculty_subjects.append(cb_dbase.cget(
        "text") if var_dbase.get() == 1 else 0)
    faculty_subjects.append(cb_dtcom.cget(
        "text") if var_dtcom.get() == 1 else 0)
    faculty_subjects.append(cb_thesis.cget(
        "text") if var_thesis.get() == 1 else 0)
    faculty_subjects.append(cb_compdes.cget(
        "text") if var_compdes.get() == 1 else 0)
    faculty_subjects.append(cb_softeng.cget(
        "text") if var_softeng.get() == 1 else 0)

    # Retains subjects that are not = 0, not selected
    faculty_subjects = [
        item for item in faculty_subjects if item != 0]

    # Use as filter data
    data = {"number": faculty_number,
            "name": faculty_name,
            "status": faculty_status,
            "department": faculty_department,
            "subjects": faculty_subjects}

    print("Search data: ", data)


    for item in tbl_view.get_children():
        tbl_view.delete(item)

    c.execute("SELECT * FROM Records WHERE numuber = ? AND name = ?", (faculty_number, faculty_name))
    searchable_data = c.fetchall()
    tbl_view.insert('', tk.END, values=searchable_data[0])

    # Writes the records to the GUI
    # for record in records:





# Labels
lbl_fnum = Label(root, text="Faculty Number:", font=("Segoe UI", 11), pady=8)
lbl_fnum.grid(row=0, column=0, sticky="w")

lbl_fname = Label(root, text="Faculty Name:", font=("Segoe UI", 11), pady=8)
lbl_fname.grid(row=1, column=0, sticky="w")

lbl_fstatus = Label(root, text="Faculty Status:",
                    font=("Segoe UI", 11), pady=8)
lbl_fstatus.grid(row=2, column=0, sticky="w")

lbl_dept = Label(root, text="Department:", font=("Segoe UI", 11), pady=8)
lbl_dept.grid(row=4, column=0, sticky="w")

lbl_sub = Label(root, text="Subjects Taught:", font=("Segoe UI", 11), pady=8)
lbl_sub.grid(row=5, column=0, sticky="w")

lbl_frec = Label(root, text="Faculty Record:", font=("Segoe UI", 11), pady=8)
lbl_frec.grid(row=8, column=0, sticky="w")

# TextFields
txt_fnum = Entry(root, font=("Segoe UI", 11), width=20, bg="white")
txt_fnum.grid(row=0, column=1, pady=8)

txt_fname = Entry(root, font=("Segoe UI", 11), width=20, bg="white")
txt_fname.grid(row=1, column=1, pady=8)

# Buttons
btn_search = Button(root, text="Search", font=(
    "Segoe UI", 10), width=10, bg="white", command=search)
btn_search.grid(row=0, column=2)

btn_save = Button(root, text="Save", font=(
    "Segoe UI", 10), width=10, bg="white", command=save)
btn_save.grid(row=0, column=3)

btn_edit = Button(root, text="Edit", font=(
    "Segoe UI", 10), width=10, bg="white", command=edit)
btn_edit.grid(row=1, column=3)

btn_delete = Button(root, text="Delete", font=(
    "Segoe UI", 10), width=10, bg="white", command=delete)
btn_delete.grid(row=2, column=3)

btn_view = Button(root, text="View", font=(
    "Segoe UI", 11), width=10, bg="white", command=view)
btn_view.grid(row=11, column=1)

btnClose = Button(root, text="Close", font=(
    "Segoe UI", 11), width=10, bg="white", command=exit)
btnClose.grid(row=11, column=2)

# ComboBox
current = tk.StringVar()
cmb_status = ttk.Combobox(font=("Segoe UI", 11),
                          width=18, textvariable=current)
cmb_status['values'] = ('Full-Time', 'Part-Time')
cmb_status.current(0)
cmb_status.grid(row=2, column=1)

# RadioButton
dept = ['Computer Science', 'Information System', 'Information Technology']
rd_grp = IntVar()
for index in range(len(dept)):
    rd_dept = Radiobutton(font=("Segoe UI", 10),
                          text=dept[index], variable=rd_grp, value=index)
    rd_dept.grid(row=4, column=index+1, sticky="w")

# Checkboxes
var_prog = IntVar()
cb_prog = Checkbutton(root, text="Programming", font=(
    "Segoe UI", 11), variable=var_prog, onvalue=1, offvalue=0)
cb_prog.grid(row=5, column=1, sticky="w")

var_dbase = IntVar()
cb_dbase = Checkbutton(root, text="Database", font=(
    "Segoe UI", 11), variable=var_dbase, onvalue=1, offvalue=0)
cb_dbase.grid(row=5, column=2, sticky="w")

var_dtcom = IntVar()
cb_dtcom = Checkbutton(root, text="Data Communication", font=(
    "Segoe UI", 11), variable=var_dtcom, onvalue=1, offvalue=0)
cb_dtcom.grid(row=5, column=3, sticky="w")

var_thesis = IntVar()
cb_thesis = Checkbutton(root, text="Thesis", font=(
    "Segoe UI", 11), variable=var_thesis, onvalue=1, offvalue=0)
cb_thesis.grid(row=6, column=1, sticky="w")

var_compdes = IntVar()
cb_compdes = Checkbutton(root, text="Compiler Design", font=(
    "Segoe UI", 11), variable=var_compdes, onvalue=1, offvalue=0)
cb_compdes.grid(row=6, column=2, sticky="w")

var_softeng = IntVar()
cb_softeng = Checkbutton(root, text="Software Engineering", font=(
    "Segoe UI", 11), variable=var_softeng, onvalue=1, offvalue=0)
cb_softeng.grid(row=6, column=3, sticky="w")

# Table for Faculty Record
tbl_column = ('fnum', 'fname', 'status', 'dept', 'subjects')
tbl_view = ttk.Treeview(columns=tbl_column, show='headings')

tbl_view.column("fnum", anchor=CENTER, stretch=NO, width=100)
tbl_view.heading('fnum', text='Faculty Number')

tbl_view.column("fname", anchor=CENTER, stretch=NO, width=200)
tbl_view.heading('fname', text='Faculty Name')

tbl_view.column("status", anchor=CENTER, stretch=NO, width=100)
tbl_view.heading('status', text='Faculty Status')

tbl_view.column("dept", anchor=CENTER, stretch=NO, width=150)
tbl_view.heading('dept', text='Department')

tbl_view.column("subjects", anchor=CENTER, stretch=NO, width=250)
tbl_view.heading('subjects', text='Subjects Taught')

tbl_view.grid(row=8, column=1, columnspan="3", sticky='w')

# Scrollbar for the table
sbar = ttk.Scrollbar(orient=tk.HORIZONTAL, command=tbl_view.xview)
tbl_view.configure(xscroll=sbar.set)
sbar.grid(row=9, column=1, columnspan=3, sticky='we')

# Blank Spaces
lbl_blank1 = Label(root, text=" ").grid(row=3, column=0)
lbl_blank2 = Label(root, text=" ").grid(row=7, column=0)
lbl_blank3 = Label(root, text=" ").grid(row=10, column=0)

root.mainloop()

conn.commit()

conn.close()
