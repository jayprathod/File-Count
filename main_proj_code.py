import os
from tkinter import *
import tkinter as grd
from tkinter import filedialog

my_wb = grd.Tk()

imgic= PhotoImage(file='1.png')
my_wb.iconphoto(False, imgic)

my_wb['bg'] = '#121212'

#getting screen width and height of display
width = my_wb.winfo_screenwidth()
height = my_wb.winfo_screenheight()

#setting tkinter window size
my_wb.geometry("%dx%d" % (width, height))

my_wb.title("Garudam")
my_dir = ''

find_fl_nm = []
st_nt_found = []

lb1_fl_nt_fnd_fnl = grd.Label(my_wb, background="#121212")
lb1_fl_nt_fnd_fnl.grid(row=5, column=0, pady=10)

lb1_fl_nt_fnd_fnl1 = grd.Label(my_wb, background="#121212") # lbl title 2--------------------
lb1_fl_nt_fnd_fnl1.grid(row=5, column=1, pady=10)

def my_func():
    my_dir = filedialog.askdirectory()
    fnl_dir = my_dir.replace('/', '//')

    path = fnl_dir
    dir_list = os.listdir(path)

    print("Files and directories in '", path, "' :")

    strt = int(num1_entry.get())
    endd = int(num2_entry.get())
    c_name = num3_entry.get()
    c_lst_name = num4_entry.get()

    # ------------------------------------------------------------------------------------------


    scrollbar = Scrollbar(my_wb, orient="vertical")
    scrollbar1 = Scrollbar(my_wb, orient="vertical")

    listbox1 = Listbox(my_wb, height=11, width=22, bg="grey", activestyle='none', font="Helvetica", fg="#f4fdff",
                       borderwidth=0, selectbackground="#07575b", selectforeground="#f4fdff")

    for j in range(strt, endd + 1):
        fl_fnl = c_name + str(j) + c_lst_name
        find_fl_nm.append(fl_fnl)
        if fl_fnl not in dir_list:
            print("not found in the folder " + fl_fnl)
            st_nt_found.append(fl_fnl)
    len_st_nt_found = len(st_nt_found)
    for lbox_i in range(0, len_st_nt_found):
        list_nt_found = st_nt_found[lbox_i]
        xx1 = list_nt_found
        print(list_nt_found)
        listbox1.insert(lbox_i, xx1)

    listbox1.grid(row=6, column=0, columnspan=2)
    listbox1.config(yscrollcommand=scrollbar1.set)

    scrollbar1.config(command=listbox1.yview)
    scrollbar1.grid(row=6, column=1, sticky='ns')


    # --------------------------list box--------------------------


    len_st_nt_found = len(st_nt_found)
    if len_st_nt_found == 0:
        print("All file in folder. \n")
        lb1_fl_nt_fnd_1 = "All file in folder. \n"
        lb1_fl_nt_fnd_fnl = grd.Label(my_wb, text=lb1_fl_nt_fnd_1, fg="#a3a3a3", font=('GlorifyDEMO', 11),
                                      background="#121212")
        lb1_fl_nt_fnd_fnl.grid(row=5, column=0, columnspan=2)

    else:
        print(str(len(st_nt_found)) + " files not found. \n")
        lb1_fl_nt_fnd_2 = str(len(st_nt_found)) + " files not found. \n"
        lb1_fl_nt_fnd_fnl = grd.Label(my_wb, text=lb1_fl_nt_fnd_2, fg="#a3a3a3", font=('GlorifyDEMO', 11),
                                      background="#121212") # lbl title 1--------------
        lb1_fl_nt_fnd_fnl.grid(row=5, column=0, columnspan=2)

    # -------------------------------------------------------------------------------------------------------
    # ---------- Extra File In Folder ------------
    listbox2 = Listbox(my_wb, height=11, width=22, bg="grey", activestyle='none', font="Helvetica", fg="#f4fdff",
                       borderwidth=0, selectbackground="#07575b", selectforeground="#f4fdff")

    ex_file_remv_in_fld = []
    for i in dir_list:
        if i not in find_fl_nm:
            ex_file_remv_in_fld.append(i)

    print(ex_file_remv_in_fld)
    print(str(len(ex_file_remv_in_fld)) + " File is extra in Folder.\n")
    ext_fl_lbl = str(len(ex_file_remv_in_fld)) + " File is extra in Folder.\n"
    lb1_fl_nt_fnd_fnl1 = grd.Label(my_wb, text=ext_fl_lbl, fg="#a3a3a3", font=('GlorifyDEMO', 11),
                                   background="#121212") # lbl title 2--------------------
    lb1_fl_nt_fnd_fnl1.grid(row=5, column=2)

    ex_fld_rem = len(ex_file_remv_in_fld)

    for lbox_j in range(0, ex_fld_rem):
        ex_in_fld = ex_file_remv_in_fld[lbox_j]
        xx2 = ex_in_fld
        print(ex_file_remv_in_fld)
        listbox2.insert(lbox_j, xx2)
    listbox2.grid(row=6, column=2)
    listbox2.config(yscrollcommand=scrollbar.set)


    scrollbar.config(command=listbox2.yview)
    scrollbar.grid(row=6, column=3, sticky='ns')

    # ---------------------------------------------------------------------------------------------------------
    # ------------- Folder In Done File ------------

    fld_dn_fl = []
    for k in dir_list:
        if k in find_fl_nm:
            fld_dn_fl.append(k)

    print(fld_dn_fl)
    print(str(len(fld_dn_fl)) + " File Is Done In Folder")

    def delete():
        print("Reset All Value")
        listbox1.delete(0, END)
        listbox2.delete(0, END)

        lb1_fl_nt_fnd_fnl.after(100, lambda: lb1_fl_nt_fnd_fnl.destroy())
        # lb1_fl_nt_fnd_fnl.config(text="")
        lb1_fl_nt_fnd_fnl1.after(100, lambda: lb1_fl_nt_fnd_fnl1.destroy())
        st_nt_found.clear()

        find_fl_nm.clear()



    # def my_resets():
        for widget in my_wb.winfo_children():
            if isinstance(widget, grd.Entry):  # If this is an Entry widget class
                widget.delete(0, 'end')  # delete all entries


    # Add a Button to Edit and Delete the Listbox Item
    grd.Button(my_wb, text="RESET", command=delete, fg="white", font=22,
               background="#5600E8", borderwidth=2, relief="flat",
               activebackground="#5600E8").grid(row=7, column=0, pady=10, columnspan=2)

    num1_entry.focus_set()
    # ---------------------------------------------------------------------------------------------------------
    # ------------- Folder In Done File ENDED ------------

# ------------- ENTER BUTOON CAN FOCUS -----------------
def nm1_to_nm2(event=None):
    num2_entry.focus_set()
    print("pressed enter")

def nm2_to_nm3(event=None):
    num3_entry.focus_set()
    print("pressed enter")

def nm3_to_nm4(event=None):
    num4_entry.focus_set()
    print("pressed enter")

def nm3_to_b1(event=None):
    b1.focus_set()
    print("pressed enter")

# ------------- UP DOWN BUTOON CAN FOCUS -----------------

def nm2_to_nm1_tab(event=None):
    num1_entry.focus_set()
    print("pressed enter")

def nm3_to_nm2_tab(event=None):
    num2_entry.focus_set()
    print("pressed enter")

def nm4_to_nm3_tab(event=None):
    num3_entry.focus_set()
    print("pressed enter")

def b1_to_nm4_tab(event=None):
    num4_entry.focus_set()
    print("pressed enter")



num1_label = grd.Label(my_wb, text="Number 1 :", background='#1F1F1F', fg="#a3a3a3", font=('GlorifyDEMO',13))
num1_label.config(highlightthickness=2, highlightbackground="#5B5959")
num1_entry = grd.Entry(my_wb, background='#1F1F1F', fg="#7F39FB", width=20, font=('GlorifyDEMO',15),justify=CENTER)
num1_entry.config(highlightthickness=2, highlightbackground="#5B5959", insertbackground='grey')

num1_entry.bind("<Return>", nm1_to_nm2)
num1_entry.bind("<Down>", nm1_to_nm2)

num2_label = grd.Label(my_wb, text="Number 2 :", background='#1F1F1F', fg="#a3a3a3", font=('GlorifyDEMO',13))
num2_label.config(highlightthickness=2, highlightbackground="#5B5959")
num2_entry = grd.Entry(my_wb, background='#1F1F1F', fg="#7F39FB", width=20, font=('GlorifyDEMO',15),justify=CENTER)
num2_entry.config(highlightthickness=2, highlightbackground="#5B5959", insertbackground='grey')

num2_entry.bind("<Return>", nm2_to_nm3)
num2_entry.bind("<Down>", nm2_to_nm3)
num2_entry.bind("<Up>", nm2_to_nm1_tab)

num3_label = grd.Label(my_wb, text="COMMON NAME : ", background='#1F1F1F', fg="#a3a3a3", font=('GlorifyDEMO',11))
num3_label.config(highlightthickness=2, highlightbackground="#5B5959")
num3_entry = grd.Entry(my_wb, background='#1F1F1F', fg="#7F39FB", width=20, font=('GlorifyDEMO',15),justify=CENTER)
num3_entry.config(highlightthickness=2, highlightbackground="#5B5959", insertbackground='grey')

num3_entry.bind("<Return>", nm3_to_nm4)
num3_entry.bind("<Down>", nm3_to_nm4)
num3_entry.bind("<Up>", nm3_to_nm2_tab)

num4_label = grd.Label(my_wb, text="COMMON LAST NAME :", background='#1F1F1F', fg="#a3a3a3", font=('GlorifyDEMO',11))
num4_label.config(highlightthickness=2, highlightbackground="#5B5959")
num4_entry = grd.Entry(my_wb, background='#1F1F1F', fg="#7F39FB", width=20, font=('GlorifyDEMO',15),justify=CENTER)
num4_entry.config(highlightthickness=2, highlightbackground="#5B5959", insertbackground='grey')

num4_entry.bind("<Return>", nm3_to_b1)
num4_entry.bind("<Down>", nm3_to_b1)
num4_entry.bind("<Up>", nm4_to_nm3_tab)


# layout the widgets
num1_label.grid(row=0, column=0, sticky="e", padx=15, pady=20, ipady=5, ipadx=50)
num1_entry.grid(row=0, column=1, ipady=4)
num2_label.grid(row=1, column=0, sticky="e", padx=15, pady=20, ipady=5, ipadx=50)
num2_entry.grid(row=1, column=1, ipady=4)
num3_label.grid(row=2, column=0, sticky="e", padx=15, pady=20, ipady=5, ipadx=26)
num3_entry.grid(row=2, column=1, ipady=4)
num4_label.grid(row=3, column=0, sticky="e", padx=15, pady=20, ipady=5, ipadx=9)
num4_entry.grid(row=3, column=1, ipady=4)

b1 = grd.Button(my_wb, text='Selet Folder', command=lambda: my_func(), width=35 , fg="white", font=22,
                background="#5600E8", borderwidth=2, relief="flat", activebackground="#5600E8")
b1.grid(row=4, column=0, padx=10, pady=20,columnspan=2)

b1.bind("<Up>", b1_to_nm4_tab)

#--------------CURSOR SET -------------
num1_entry.focus_set()

my_wb.mainloop()
