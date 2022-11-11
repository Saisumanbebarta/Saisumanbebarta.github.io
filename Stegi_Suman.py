from tkinter import *
from tkinter.filedialog import *
from stegano import exifHeader as stg
from tkinter import messagebox
import glob
def encode():
    main.destroy()
    enc = Tk()
    enc.title("encode")
    enc.geometry("500x400+300+150")
    label1 = Label(text="Secret Message")
    label1.place(relx=0.1, rely=0.1, height=20, width=100)
    entry = Entry()
    entry.place(relx=0.4, rely=0.1)
    label2 = Label(text="File name")
    label2.place(relx=0.1, rely=0.2, height=20, width=100)
    entrysave = Entry()
    entrysave.place(relx=0.4, rely=0.2)

    def openfile():
        global fileopen
        fileopen = StringVar()
        fileopen = askopenfilename(initialdir='/Desktop', title='select file', filetypes=(("jpeg files", "*jpg"), ("all files", "*.*")))
        label3 = Label(text=fileopen)
        label3.place(relx=0.3, rely=0.3)
    def encodee():
        response = messagebox.askyesno("pop up", "do you want to encode")
        if response == 1:
            stg.hide(fileopen,entrysave.get()+'.jpg', entry.get())
            messagebox.showinfo("pop up", "successfully encode")
        else:
            messagebox.showwarning("pop up", "unsuccessful")
    buttonselect = Button(text='select file', command=openfile)
    buttonselect.place(relx=0.1, rely=0.3)
    buttonencode= Button(text="Encode", command=encodee)
    buttonencode.place(relx=0.4, rely=0.5)
def decode():
    main.destroy()
    dnc = Tk()
    dnc.title("decode")
    dnc.geometry("500x400+300+150")
    def openfile():
        global fileopen
        fileopen = StringVar()
        fileopen = askopenfilename(initialdir='/Desktop', title='select file', filetypes=(("jpeg files", "*jpg"), ("all files", "*.*")))
    def decodee():
        message= stg.reveal(fileopen)
        label4= Label(text=message)
        label4.place(relx=0.3,rely=0.3)
    buttonselect = Button(text='select file', command=openfile)
    buttonselect.place(relx=0.1, rely=0.3)
    buttonencode = Button(text="Decode", command=decodee)
    buttonencode.place(relx=0.4, rely=0.5)

def decodei():
    main.destroy()
    dnc = Tk()
    dnc.title("decode")
    dnc.geometry("500x400+300+150")
    magic_numbers = {'jpg': bytes([0xFF, 0xD8, 0xFF, 0xE0])}
    for x in glob.glob("*jpg"):
        with open(x, 'rb') as fd:
            file_data = fd.read()
            print("Detected " + str(file_data.count(magic_numbers['jpg'])) + " JPG files in file : " + fd.name)
            if file_data.count(magic_numbers['jpg']) > 1:
                print("Trying to extract embedded files")
                for f in range(file_data.count(magic_numbers['jpg'])):
                    with open(str(f + 1) + ".jpg", "wb") as ff:
                        ff.write(magic_numbers['jpg'] + file_data.split(magic_numbers['jpg'])[f + 1])
                        print("Generated file : " + str(f + 1) + ".jpg")
    messagebox.showinfo("pop up", "successfully Decoded Image")


main = Tk()
main.title("img stegano")
main.geometry("500x400+300+150")
encodeb = Button(text='Encode Message', command=encode)
encodeb.place(relx=0.2, rely=0.3, height=40, width=100)
decodeb = Button(text='Decode Message', command=decode)
decodeb.place(relx=0.4, rely=0.3, height=40, width=100)
decodebi = Button(text='Decode Image', command=decodei)
decodebi.place(relx=0.6, rely=0.3, height=40, width=100)
main.mainloop()