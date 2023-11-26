from tkinter import*
import tkinter as tk

#create the GUI window
root = Tk()
root.title("Calculator")
root.geometry("350x700")
scValue = ""

#Function for computation and displaying values whenever a button is clicked
def onclick(event):
    global scValue
    temp = event.widget.cget("text")
    if(temp == "C"):
        scValue = ""
        entry.delete(0,END)
    elif(temp == "="):
        entry.delete(0,END)
        answer=""
        if scValue != "":
            try:
                answer = eval(scValue)
            except:
                answer = "error"
                scValue = ""
            entry.insert(END,answer)
    else:
        scValue += temp
        entry.insert(END,event.widget.cget("text"))

#entry widget for displaying expressions and results
entry =Entry(root,font=('lucida 20'))
entry.pack(fill=X,ipadx=2,padx=12,pady=10)

#list for button labels
list=["C","/","%","7","8","9","4","5","6","1","2","3","*","-","+",".","0","="]
i=0
j=0
buttons = []

#creating and placing the buttons in the GUI window
for text in list:
    button= Button(root, text=text, height=2, width=5, font="lucida 20 bold", fg="black")
    button.place(x=20+100*i, y=80+100*j)
    button.bind("<Button-1>",onclick)
    buttons.append(button)
    i+=1
    if i==3:
        i=0
        j+=1
#Run the GUI application
root.mainloop()