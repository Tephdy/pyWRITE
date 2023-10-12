# modules
import tkinter as ttk
import ttkbootstrap as ttb
from ttkbootstrap import Style

def show_hide():
    add_btn_var.get()

    if text_frame.winfo_viewable():
        text_frame.pack_forget()
        add_btn_var.set("ADD NOTES")
    else:
        text_frame.pack()
        add_btn_var.set("BACK")
        text_area.delete("1.0", "end")

def cancel_btn():
    text_frame.pack_forget()
    add_btn_var.set("ADD NOTES")
    text_area.delete("1.0","end")

def add_task():
    task_value=text_area.get("1.0", "end-1c")
    # print(task_value)
    task.append(task_value)
    task.reverse()
    print(task)
    text_area.delete("1.0","end")
    text_frame.pack_forget()
    add_btn_var.set("ADD NOTES")


task=[]

# window
window=ttb.Window()
window.geometry('500x800')
window.title("PYWRITE")
window.resizable(False, False)
style=Style(theme="darkly")

# main_frame
main_frame=ttb.Frame(window)
main_frame.pack(expand=True, fill='both', ipadx=10, ipady=10)

# header_frame
header_frame=ttb.Frame(main_frame)
header_frame.pack(fill='x', padx=10, pady=10)

# header_title_label
header_title_label=ttb.Label(header_frame, text="PYWRITE", font="Calibre 14 bold")
header_title_label.pack(side="left")

# add_btn
add_btn_var=ttk.StringVar()
add_btn_var.set("ADD NOTES")
add_btn=ttb.Button(header_frame, width=13, style="success", command=show_hide, textvariable=add_btn_var)
add_btn.pack(side="right")

# header_separator
header_separator=ttb.Separator(main_frame, style="default")
header_separator.pack(fill='x')
#

# text_frame
text_frame=ttb.Frame(main_frame)
# text_frame.pack(fill='both')

# text_frame_label
text_frame_label=ttb.Label(text_frame, text="ADD NOTES")
text_frame_label.pack()

# text_area
text_area=ttb.Text(text_frame)
text_area.pack(ipadx=20, ipady=20)

# text_area_control
text_area_control=ttb.Frame(text_frame)
text_area_control.pack(fill='both', expand=True, padx=5, pady=5)
text_area_control.columnconfigure((0, 1), weight=2)

# save_btn
save_btn=ttb.Button(text_area_control, text="SAVE", style="success", command=add_task)
save_btn.grid(row=0, column=0, sticky="ew")

# cancel_btn
cancel_btn=ttb.Button(text_area_control, text="CANCEL", style="danger", command=cancel_btn)
cancel_btn.grid(row=0, column=1, sticky="ew")

for widget in text_area_control.winfo_children():
    widget.grid_configure(padx=3, pady=3)

# run
window.mainloop()