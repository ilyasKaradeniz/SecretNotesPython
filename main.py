import time
from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image
import crypto_module
import threading
window = Tk()
window.minsize(700,700)
window.title("Secret Notes")
window.config(bg="#ced4da", padx=30, pady=30)

enc_only_list = []
# functions-------------
def encrypt():
    title = title_input.get()
    message = content_input.get("1.0",END)
    password = key_input.get()
    if title == "" or message == "" or password == "":
        messagebox.showinfo(title="Eksik bilgi", message="Şifreleme için tüm alanlar zorunlu")
    else:
        encrypted_message = crypto_module.encrypt_note(message, password)
        db_file =open("db.txt", "a")
        db_file.write(title+"\n")
        db_file.write(encrypted_message.decode("utf-8")+"\n")
        successful()
        add_to_list()

def decrypt():
    title = title_input.get()
    message = content_input.get("1.0", END)
    password = key_input.get()
    try:
        decrypted_message = crypto_module.decrypt_note(message, password)
        content_input.delete('1.0', END)
        content_input.insert(1.0,decrypted_message)
    except:
        messagebox.showinfo(title="Hatalı bilgi", message="Eksik veya hatalı bilgi")

def add_to_list():
    data_listbox.delete('0', 'end')
    global enc_only_list
    with open('db.txt','r') as db_file:
        full_list = [line.strip() for line in db_file]
        enc_only_list = []
        for i in range(len(full_list)):
            if i % 2 != 0:
                enc_only_list.append(full_list[i])
            else:
                data_listbox.insert(END, full_list[i])

def decrypt_from_list():
    selection = data_listbox.curselection()
    content_input.delete('1.0', END)
    content_input.insert(1.0, enc_only_list[int(''.join(map(str, selection)))])

def successful():
    save_button["text"]="Encrypted Successfully"
    save_button["background"] = "#2a9d8f"
    def get_ready():
        save_button["text"] = "Encrypt & Save"
        save_button["background"] = btn_bg
    timer=threading.Timer(3.0,get_ready)
    timer.start()


#user interface UI
# #UI variables----------------------------
FONT = ("Arial", 10, "bold")
main_bg = "#ced4da"
main_fg = "#4a4e69"
btn_bg = "#4a4e69"
btn_fg = "#ffffff"
ent_bg = "#edf2f4"
ent_fg = "#4a4e69"
# TODO: image "label"
top_image = Image.open("topsecret.png")
img = ImageTk.PhotoImage(top_image.resize((200, 85)))
image_label = Label(image=img, borderwidth=0)
image_label.image = img
image_label.place(x=60, y=10)

# TODO: title label "label""
title_label = Label(text="Title: ",bg=main_bg, fg=main_fg, font=FONT)
title_label.place(x=0, y=110)

# TODO: Title "entry"
title_input = Entry(width=50, bg=ent_bg, fg=ent_fg, borderwidth=0)
title_input.place(x=0, y=135)

# TODO: content label "label"
content_label = Label(text="Text for encryption: ", bg=main_bg, fg=main_fg, font=FONT)
content_label.place(x=0, y=170)

# TODO: Content "text"
content_input = Text(width=38, height=20, bg=ent_bg, fg=ent_fg, borderwidth=0)
content_input.place(x=0, y=195)

# TODO: key label "label"
key_label = Label(text="Enter key: ",bg=main_bg, fg=main_fg, font=FONT)
key_label.place(x=0, y=530)

# TODO: key "entry"
key_input = Entry(width=50, bg=ent_bg, fg=ent_fg, borderwidth=0)
key_input.place(x=0, y=556)

# TODO: save & encrypt "button"
save_button = Button(text="Encrypt & Save", command=encrypt, width=20, bg=btn_bg, fg=btn_fg, borderwidth=0,pady=7)
save_button.place(x=0, y=600)

# TODO: decrypt "button"
dec_button = Button(text="Decrypt", command=decrypt, width=20, bg=btn_bg, fg=btn_fg, borderwidth=0,pady=7)
dec_button.place(x=160, y=600)

# TODO: encrypted datas label "label"
data_list_label = Label(text="Encrypted datas: ", fg=main_fg,bg=main_bg, font=FONT)
data_list_label.place(x=350, y=0)

# TODO: encrypted datas "listbox"
data_listbox = Listbox(width=48, height=34, bg=ent_bg, fg=ent_fg, borderwidth=0)
data_listbox.place(x=350, y=30)

# TODO: decrypt from list "button"
list_dec_button = Button(text="Decrypt from list", command=decrypt_from_list, width=40, bg=btn_bg, fg=btn_fg, borderwidth=0,pady=7)
list_dec_button.place(x=350, y=600)

# TODO: refresh list "button"
refresh_list_button = Button(text="Refresh list", command=add_to_list, width=10, bg=btn_bg, fg=btn_fg, borderwidth=0, pady=3)
refresh_list_button.place(x=563, y=0)


add_to_list()

window.mainloop()