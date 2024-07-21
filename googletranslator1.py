from tkinter import *
from tkinter import ttk


from googletrans import Translator,LANGUAGES # importing the google translator module and languages

# Translator ka kaam

def change(text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans= Translator()
    trans1 = trans.translate(text1, src=src1.lower(), dest=dest1.lower())

    return trans1.text

def get_data():
    s=comb_sor.get() # we will get the data of combo box of the source
    d=comb_dest.get() # we will get the data of combo box of the destination
    msg=Sor_Txt.get(1.0,END) # will get the data of source text from starting to end
    textget=change(text=msg,src=s,dest=d)
    dest_Txt.delete(1.0,END) # deleting the date of destination text from starting to end
    dest_Txt.insert(END,textget)




















# Create the main window
root = Tk()
root.title("Translator")
root.geometry("500x700")  # Width and height of the translator
root.config(bg="blue")  # Background color of the translator

# Label for the title
lab_txt = Label(root, text="Translator", font=("Time New Roman", 30, "bold"), bg="light grey")
lab_txt.place(x=100, y=40, height=50, width=300)

# Frame to contain text areas and labels
frame=Frame(root).pack(side=BOTTOM)
# Heading of source text
lab_src_txt = Label(root, text="Source text", font=("Time New Roman", 20, "bold"), fg="black",bg="light grey")
lab_src_txt.place(x=100, y=100, height=20, width=300)

# Textbox for source text
Sor_Txt = Text(root, font=("Time New Roman", 20), bg="light grey", wrap=WORD)
Sor_Txt.place(x=10, y=130, height=150, width=480)

# Combo box for source text
list_text=list(LANGUAGES.values()) # language # we will start getting different different langauges in it
comb_sor=ttk.Combobox(frame,value=list_text) 
comb_sor.place(x=10, y=300, height=40, width=100) # placement of comb_Sor or rather say Combo box
# you can set values to combo box
comb_sor.set("English")
button_langchange=Button(frame,text="Translate",relief=RAISED,command=get_data) # relief=Raised just gives 3 D ness to the button
# place the button
button_langchange.place(x=170, y=300, height=40, width=150)




# create another combo box for destination

comb_dest=ttk.Combobox(frame,value=list_text) 
comb_dest.place(x=360, y=300, height=40, width=150) # placement of comb_Sor or rather say Combo box
# you can set values to combo box
comb_dest.set("English")



# Heading of Destination text
lab_src_txt = Label(root, text="Destination text", font=("Time New Roman", 20, "bold"), fg="black",bg="light grey")
lab_src_txt.place(x=100, y=360, height=20, width=300)

# make text box of destination

dest_Txt = Text(root, font=("Time New Roman", 20), bg="light grey", wrap=WORD)
dest_Txt.place(x=10, y=400, height=150, width=480)







# Run the application
root.mainloop()
