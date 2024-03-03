from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
from stegano import lsb

root=Tk()
root.title("Steganography - Hide a Secret Message in a File")
root.geometry("700x500+150+180")
root.resizable(False,False)
root.configure(bg="#2f4155")

filename = None
hidden_data = None

def showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(("All files", "*.*"),))
    if filename:
        filetype = filename.split(".")[-1].lower()
        if filetype in ["png", "jpg", "jpeg", "gif"]:
            img=Image.open(filename)
            img=ImageTk.PhotoImage(img)
            lbl.configure(image=img, width=250, height=250)
            lbl.image=img
        else:
            messagebox.showerror("Error", "Unsupported file format!")

def Hide():
    global hidden_data
    global filename
    message=text1.get(1.0, END)
    try:
        hidden_data = lsb.hide(str(filename), message)
        messagebox.showinfo("Success", "Data hidden successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error hiding data: {str(e)}")

def Show():
    global filename
    try:
        clear_message = lsb.reveal(filename)
        text1.delete(1.0, END)
        text1.insert(END, clear_message)
    except Exception as e:
        messagebox.showerror("Error", f"Error revealing data: {str(e)}")

def save():
    global hidden_data
    if hidden_data:
        try:
            output_filename = filedialog.asksaveasfilename(defaultextension=".png",
                                                           filetypes=(("PNG files", "*.png"), ("All files", "*.*")))
            if output_filename:
                hidden_data.save(output_filename)
                messagebox.showinfo("Success", "Image saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error saving image: {str(e)}")
    else:
        messagebox.showerror("Error", "No hidden data to save!")


#icon
image_icon=PhotoImage(file="E:\VS code\Projects\project data for stegano\logo.jpg")
root.iconphoto(False,image_icon)


#logo
logo=PhotoImage(file="E:\VS code\Projects\project data for stegano\logo.png")
Label(root,image=logo,bg="#2f4155").place(x=10,y=0)

Label(root,text="CYBER SCIENCE",bg="#2f4155",fg="white",font="arial 25 bold").place(x=100,y=20)


# First Frame
f=Frame(root,bd=3,bg="black",width=340,height=280,relief=GROOVE)
f.place(x=10,y=80)

lbl=Label(f,bg="black")
lbl.place(x=40,y=10)

# Second Frame
frame2=Frame(root,bd=3,bg="black",width=340,height=280,relief=GROOVE)
frame2.place(x=350,y=80)

text1=Text(frame2,font="Roboto 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=320,height=295)

scrollbar1=Scrollbar(frame2)
scrollbar1.place(x=320,y=0,height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Third Frame
frame3=Frame(root,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
frame3.place(x=10,y=370)

Button(frame3,text="Open File",width=10,height=2,font="arial 14 bold",command=showimage).place(x=20,y=30)
Button(frame3,text="Save File",width=10,height=2,font="arial 14 bold",command=save).place(x=180,y=30)
Label(frame3,text="Select Image, Video, Audio, or Text File",bg="#2f4155",fg="yellow").place(x=20,y=5)

# Fourth Frame
frame4=Frame(root,bd=3,bg="#2f4155",width=340,height=280,relief=GROOVE)
frame4.place(x=360,y=370)

Button(frame4,text="Hide Data",width=10,height=2,font="arial 14 bold",command=Hide).place(x=20,y=30)
Button(frame4,text="Show Data",width=10,height=2,font="arial 14 bold",command=Show).place(x=180,y=30)
Label(frame4,text="Hide and Show Data",bg="#2f4155",fg="yellow").place(x=20,y=5)

root.mainloop()
