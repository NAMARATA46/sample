from tkinter import *
from tkinter import messagebox
import base64

def decrypt():
    password = code.get()
    
    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("Decryption")
        screen1.geometry("400x250")
        screen1.configure(bg="#f7d9b1")  # Skin tone background
        
        message = text1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt_text = base64_bytes.decode("ascii")
        
        Label(screen1, text="DECRYPT", font=("Segoe UI", 20, "bold"), fg="#2e2e2e", bg="#f7d9b1").pack(pady=10)
        text2 = Text(screen1, font=("Calibri", 10), bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.pack(padx=10, pady=5, fill=BOTH, expand=True)
        
        text2.insert(END, decrypt_text)
    elif password == "":
        messagebox.showerror("Decryption", "Input Password")
    elif password != "1234":
        messagebox.showerror("Decryption", "Invalid Key")

def encrypt():
    password = code.get()
    
    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x250")
        screen1.configure(bg="#f3bdb1")  # Skin tone background
        
        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt_text = base64_bytes.decode("ascii")
        
        Label(screen1, text="ENCRYPT", font=("Segoe UI", 20, "bold"), fg="#2e2e2e", bg="#f3bdb1").pack(pady=10)
        text2 = Text(screen1, font=("Calibri", 10), bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.pack(padx=10, pady=5, fill=BOTH, expand=True)
        
        text2.insert(END, encrypt_text)
    elif password == "":
        messagebox.showerror("Encryption", "Input Password")
    elif password != "1234":
        messagebox.showerror("Encryption", "Invalid Key")

def reset():
    code.set("")
    text1.delete(1.0, END)

def main_screen():
    global screen
    global code
    global text1
    
    screen = Tk()
    screen.geometry("400x400")
    screen.title("Message Encrypt Decrypt App")
    screen.configure(bg="#f3d9b1")  # Skin tone background
    
    # icon
    image_icon = PhotoImage(file="keys.png")
    screen.iconphoto(False, image_icon)
    
    Label(screen, text="Enter text", fg="#2e2e2e", font=("Segoe UI", 13)).place(x=20, y=20)
    text1 = Text(screen, font=("Calibri", 12), bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=20, y=50, width=360, height=100)
    
    Label(screen, text="Enter password", fg="#2e2e2e", font=("Segoe UI", 13)).place(x=20, y=170)
    
    code = StringVar()
    Entry(screen, textvariable=code, width=25, bd=0, font=("Calibri", 15), show="*").place(x=20, y=200)
    
    Button(screen, text="ENCRYPT", height=2, width=20, bg="#ff4f4f", fg="white", bd=0, command=encrypt).place(x=20, y=250)
    Button(screen, text="DECRYPT", height=2, width=20, bg="#4f98ff", fg="white", bd=0, command=decrypt).place(x=210, y=250)
    Button(screen, text="RESET", height=2, width=40, bg="#4f4f4f", fg="white", bd=0, command=reset).place(x=20, y=310)
    
    screen.mainloop()

main_screen()
