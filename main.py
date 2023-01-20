import tkinter as tk
from tkinter import *
from tkinter import ttk
import faculty_db as fdb
from tkinter.messagebox import showinfo

departments = ["Computer Science", "Information System", "Information Technology"]

# show text info
def show_info():
    print("faculty num:", faculty_num_var.get())
    print("faculty name:", faculty_name_var.get())
    print("faculty status:", faculty_status_var.get())
    print("faculty department:", faculty_department_var.get())
    print("programming:", programming_var.get())
    print("database:", database_var.get())
    print("data communication:", data_communication_var.get())
    print("thesis:", thesis_var.get())
    print("compiler design:", compiler_design_var.get())
    print("software engineering:", software_engineering_var.get())
    print("")
    print(fdb.search(faculty_num_var.get()))
    pass 

# clear entries
def clear_entries():
    faculty_num_var.set(0)
    faculty_name_var.set('')
    faculty_status_var.set('')
    faculty_department_var.set(-1)
    programming_var.set(0)
    database_var.set(0)
    data_communication_var.set(0)
    thesis_var.set(0)
    compiler_design_var.set(0)
    software_engineering_var.set(0)
    tree.delete(*tree.get_children())

# save info (insert)
def save():
    entries = dict()
    entries['faculty_num'] = faculty_num_var.get()
    entries['faculty_name'] = faculty_name_var.get().strip()
    entries['faculty_status'] = faculty_status_var.get().strip()
    entries['faculty_department'] = faculty_department_var.get()
    entries['programming'] = programming_var.get()
    entries['database'] = database_var.get()
    entries['data_communication'] = data_communication_var.get()
    entries['thesis'] = thesis_var.get()
    entries['compiler_design'] = compiler_design_var.get()
    entries['software_engineering'] = software_engineering_var.get()

    # negative faculty number
    if entries['faculty_num'] <= 0:
        showinfo("Error", "Faculty number must be greater than 0.")
        return None
    # empty faculty name
    elif entries['faculty_name'] == '':
        showinfo("Error", "Faculty name must not be empty.")
        return None
    # empty faculty status
    elif entries['faculty_status'] == '':
        showinfo("Error", "Faculty status must not be empty.")
        return None
    # empty faculty department
    elif entries['faculty_department'] < 0:
        showinfo("Error", "Faculty department must not be empty.")
        return None
    # faculty number exists
    elif fdb.search(entries['faculty_num']):
        showinfo("Error", "Faculty number already exists.")
        return None

    # save entry 
    fdb.save(entries)
    showinfo("Success", "Faculty record successfully inserted.")
    clear_entries()

    return entries

# edit entry (update)
def edit():
    entries = dict()
    entries['faculty_num'] = faculty_num_var.get()
    entries['faculty_name'] = faculty_name_var.get().strip()
    entries['faculty_status'] = faculty_status_var.get().strip()
    entries['faculty_department'] = faculty_department_var.get()
    entries['programming'] = programming_var.get()
    entries['database'] = database_var.get()
    entries['data_communication'] = data_communication_var.get()
    entries['thesis'] = thesis_var.get()
    entries['compiler_design'] = compiler_design_var.get()
    entries['software_engineering'] = software_engineering_var.get()

    # negative faculty number
    if entries['faculty_num'] <= 0:
        showinfo("Error", "Faculty number must be greater than 0.")
        return None
    # empty faculty name
    elif entries['faculty_name'] == '':
        showinfo("Error", "Faculty name must not be empty.")
        return None
    # empty faculty status
    elif entries['faculty_status'] == '':
        showinfo("Error", "Faculty status must not be empty.")
        return None
    # empty faculty department
    elif entries['faculty_department'] < 0:
        showinfo("Error", "Faculty department must not be empty.")
        return None
    # faculty number not exists
    elif not fdb.search(entries['faculty_num']):
        showinfo("Error", "Faculty number does not exists.")
        return None

    # save entry 
    fdb.edit(entries)
    showinfo("Success", "Faculty record successfully updated.")
    clear_entries()

    return entries

# delete entry 
def delete():
    entries = fdb.search(faculty_num_var.get())
    if entries:
        fdb.delete(faculty_num_var.get())
        showinfo("Success", "Faculty record deleted.")
    else:
        showinfo("Error", "Faculty number does not exist.")
    clear_entries()
    
# search and show entries
def search_show():
    entries = fdb.search(faculty_num_var.get())
    if entries:
        entry = entries[0]
        faculty_num_var.set(entry[0])
        faculty_name_var.set(entry[1])
        faculty_status_var.set(entry[2])
        faculty_department_var.set(entry[3])
        programming_var.set(entry[4])
        database_var.set(entry[5])
        data_communication_var.set(entry[6])
        thesis_var.set(entry[7])
        compiler_design_var.set(entry[8])
        software_engineering_var.set(entry[9])
    else:
        showinfo("Error", "Faculty number does not exist.")
        clear_entries()

# view entries
def view():
    entries = dict()
    entries['faculty_num'] = faculty_num_var.get()
    entries['faculty_name'] = faculty_name_var.get().strip()
    entries['faculty_status'] = faculty_status_var.get().strip()
    entries['faculty_department'] = faculty_department_var.get()
    entries['programming'] = programming_var.get()
    entries['database'] = database_var.get()
    entries['data_communication'] = data_communication_var.get()
    entries['thesis'] = thesis_var.get()
    entries['compiler_design'] = compiler_design_var.get()
    entries['software_engineering'] = software_engineering_var.get()

    result = fdb.view(entries)

    tree.delete(*tree.get_children())
    contacts = []

    for r in result:
        # display entries in treeview
        subjects = []
        if r[4] == 1:
            subjects.append("Programming")
        if r[5] == 1:
            subjects.append("Database")
        if r[6] == 1:
            subjects.append("Data Communication")
        if r[7] == 1:
            subjects.append("Thesis")
        if r[8] == 1:
            subjects.append("Compiler Design")
        if r[9] == 1:
            subjects.append("Software Engineering")        
        contacts.append((f'{r[0]}', f'{r[1]}', f'{r[2]}', f'{departments[r[3]]}', f'{", ".join(subjects)}'))

    for contact in contacts:
        tree.insert('', tk.END, values=contact)
    print(result)

# display entries by clicking on treeview
def selectItem(a):
    curItem = tree.focus()
    faculty_number = tree.item(curItem)['values'][0]
    faculty_num_var.set(faculty_number)
    search_show()

# initialize Tk
window = Tk()
window.geometry("650x650")
window.title("PUP Faculty Database")

#Faculty Var
faculty_num_var = IntVar()
faculty_name_var = StringVar()
faculty_status_var = StringVar()
faculty_department_var = IntVar()
programming_var = IntVar()
database_var = IntVar()
data_communication_var = IntVar()
thesis_var = IntVar()
compiler_design_var = IntVar()
software_engineering_var = IntVar()


icon = PhotoImage(file='PUPLogo.png')
window.iconphoto(True, icon)

#Top-section
topframe = Frame(window, bd=5, padx=10, pady=10)
topframe.grid(row=0, column=0, sticky="w")

#Faculty Labels
facultyNumLabel = Label(topframe, text="Faculty Number:", font=("Arial", 12), pady=10).grid(row=0, column=0, sticky="w")
facultyNameLabel = Label(topframe, text="Faculty Name:", font=("Arial", 12), pady=10).grid(row=1, column=0, sticky="w")
facultyStatusLabel = Label(topframe, text="Faculty Status:", font=("Arial", 12), pady=10).grid(row=2, column=0, sticky="w")

#Faculty Entries
facultyNumEntry = Entry(topframe, font=("Arial", 15), textvariable=faculty_num_var).grid(row=0, column=1, padx=10)
facultyNameEntry = Entry(topframe, font=("Arial", 15), textvariable=faculty_name_var).grid(row=1, column=1)

#Faculty Combobox
facultyEntryCombobox = ttk.Combobox(topframe, font=("Arial", 15), width=18, textvariable=faculty_status_var)
facultyEntryCombobox['values'] = ('Regular', 'Full-Time', 'Part-Time')
facultyEntryCombobox.grid(row=2, column=1)

#Main Buttons
searchButton = Button(topframe, text="Search", font=("Arial", 10), width=15, command=search_show).grid(row=0, column=2)
saveButton = Button(topframe, text="Save", font=("Arial", 10), width=15, command=save).grid(row=0, column=3)
clearButton = Button(topframe, text="Clear", font=("Arial", 10), width=15, command=clear_entries).grid(row=1, column=2)
editButton = Button(topframe, text="Edit", font=("Arial", 10), width=15, command=edit).grid(row=1, column=3)
deleteButton = Button(topframe, text="Delete", font=("Arial", 10), width=15, command=delete).grid(row=2, column=3)


#Middle-section
midframe = Frame(window, bd=5, padx=10, pady=10)
midframe.grid(row=1, column=0, sticky="w")

#Dept and Subjects Labels
departmentLabel = Label(midframe, text="Department:", font=("Arial", 12), pady=10).grid(row=0, column=0, sticky="w")
subjectsLabel = Label(midframe, text="Subjects Taught:", font=("Arial", 12), pady=10).grid(row=1, column=0, sticky="w")

#Radio-buttons
departments = ["Computer Science", "Information System", "Information Technology"]
for index in range(len(departments)):
    radiobutton = Radiobutton(midframe,
                              text=departments[index],
                              variable=faculty_department_var, #groups radiobuttons together
                              value=index, #assigns each radiobutton a different value
                              font=("Arial", 10),
                              )
    radiobutton.grid(row=0, column=index+1, sticky="w")

#Check-buttons
programming_checkbutton = Checkbutton(midframe,
                           text="Programming",
                           font=("Arial", 10),
                           variable=programming_var,
                           onvalue=1,
                           offvalue=0,
                           ).grid(row=1, column=1, sticky="w")

database_checkbutton = Checkbutton(midframe,
                           text="Database",
                           font=("Arial", 10),
                           variable=database_var,
                           onvalue=1,
                           offvalue=0,
                           ).grid(row=1, column=2, sticky="w")

datacomm_checkbutton = Checkbutton(midframe,
                           text="Data Communication",
                           font=("Arial", 10),
                           variable=data_communication_var,
                           onvalue=1,
                           offvalue=0,
                           ).grid(row=1, column=3, sticky="w")

thesis_checkbutton = Checkbutton(midframe,
                           text="Thesis",
                           font=("Arial", 10),
                           variable=thesis_var,
                           onvalue=1,
                           offvalue=0,
                           ).grid(row=2, column=1, sticky="w")

compdes_checkbutton = Checkbutton(midframe,
                           text="Compiler Design",
                           font=("Arial", 10),
                           variable=compiler_design_var,
                           onvalue=1,
                           offvalue=0,
                           ).grid(row=2, column=2, sticky="w")

softengr_checkbutton = Checkbutton(midframe,
                           text="Software Engineering",
                           font=("Arial", 10),
                           variable=software_engineering_var,
                           onvalue=1,
                           offvalue=0,
                           ).grid(row=2, column=3, sticky="w")


#Bottom-section
botframe = Frame(window, bd=5, padx=10, pady=10)
botframe.grid(row=2, column=0, sticky="w")

#Faculty Record Label
facultyRecordLabel = Label(botframe, text="Faculty Record:", font=("Arial", 12), padx=10).grid(row=0, column=0, sticky="w")

#View Record
columns = ('faculty_number', 'faculty_name', 'faculty_status', 'dept', 'subjects')
tree = ttk.Treeview(botframe, columns=columns, show='headings')
tree.column("faculty_number",anchor=CENTER, stretch=NO, width=100)
tree.heading('faculty_number', text='Faculty Number')
tree.column("faculty_name",anchor=CENTER, stretch=NO, width=200)
tree.heading('faculty_name', text='Faculty Name')
tree.column("faculty_status",anchor=CENTER, stretch=NO, width=100)
tree.heading('faculty_status', text='Faculty Status')
tree.column("dept",anchor=CENTER, stretch=NO, width=150)
tree.heading('dept', text='Department')
tree.column("subjects",anchor=CENTER, stretch=NO, width=600)
tree.heading('subjects', text='Subjects Taught')
tree.bind('<ButtonRelease-1>', selectItem)

tree.grid(row=0, column=2, columnspan="3", sticky='nsew')

scrollbar2 = ttk.Scrollbar(botframe, orient=tk.HORIZONTAL, command=tree.xview)
tree.configure(xscroll=scrollbar2.set)
scrollbar2.grid(row=1, column=1, columnspan=4, sticky='we')

#View and Close Buttons
viewButton = Button(botframe, text="View", font=("Arial", 10), width=15, command=view).grid(row=2, column=2, sticky="w")
closeButton = Button(botframe, text="Close", font=("Arial", 10), width=15, command=window.destroy).grid(row=2, column=4, sticky="e")

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

botframe.columnconfigure(0, weight=0)
botframe.columnconfigure(1, weight=1)
botframe.columnconfigure(2, weight=1)
botframe.columnconfigure(3, weight=3)
botframe.columnconfigure(4, weight=3)
botframe.columnconfigure(5, weight=1)
botframe.rowconfigure(1, weight=1)

clear_entries()
window.mainloop()


