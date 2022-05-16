import random
import time
from turtle import color
  
# Timer starts
starttime = time.time()
#---------------------------------------------------------------------------  RANDOM WORD select
WORDLIST = "cuvinte secrete.txt"

def loadWords():
    print("Loading the word from file...")
    inFile = open(WORDLIST, 'r')
    line = inFile.readline()
    wordlist = line.split()
    return random.choice(wordlist)



def hangman():
    global word,ll,lenword1,lenwordvar,ffdata,temps,first
    first = inpp.get()
    input1.delete(0,END)
    if(lenwordvar>0):
        if(first in word):
            for i in range(lenword1):
                if(word[i] == first and ll[i] == '_ '):
                    ll.pop(i)
                    ll.insert(i,word[i])
                    xx = ''.join(ll)
                    word = list(word)
                    word.pop(i)
                    word.insert(i,"_ ")
                    wordlabel.configure(text=xx)
                    if(xx==temps):
                        totaltime = round((time.time() - starttime), 2)
                        ans.configure(text='Felicitari, ai gasit cuvantul intr-un timp record de {} secunde.'.format(totaltime))
                        res = messagebox.askyesno("Notification",'Felicitari, ai gasit cuvantul intr-un timp record de {} secunde. Vrei sa mai incerci alt cuvant?'.format(totaltime))
                        
                        if(res==True):
                            chooseword()
                        else:
                            root.destroy()
                    else:
                        break
        else:
            lenwordvar = lenwordvar - 1
            leftchances.configure(text='Incercari ramase: {}'.format(lenwordvar))
    if(lenwordvar<=0):
        ans.configure(text='Ai pierdut, cuvantul era {}'.format(word))
        res = messagebox.askyesno("Notification", 'Ai pierdut cuvantul tau era {}. Vrei sa mai incerci alt cuvant?'.format(word))
        if (res == True):
            chooseword()
        else:
            root.destroy()


def jj(event):
    hangman()
    
from tkinter import *
from tkinter import messagebox
worldlist = loadWords()

root = Tk()
root.geometry('800x500+300+100')
bg = PhotoImage(file = "background.png")
  
# Create Canvas

canvas1 = Canvas( root, width = 900,height = 900)
canvas1.pack(fill = "both", expand = True)
  
# Display image

canvas1.create_image( 0, 0, image = bg,anchor = "nw")

root.iconbitmap('iconita.ico')
root.title('Spânzurătoarea')

#-------------------------------------------------------
introlabel = Label(root,text='Hai sa jucam spanzuratoarea',font=('arial',35,'bold'),bg='#676767', borderwidth=1, relief="solid")
introlabel.place(x=200,y=0)

wordlabel = Label(root,text='',font=('arial',55,'bold'),bg='#676767', borderwidth=1, relief="solid")
wordlabel.place(x=180,y=150)

leftchances = Label(root,text='',font=('arial',25,'bold'),bg='#C70039', borderwidth=1, relief="solid")
leftchances.place(x=550,y=100)

ans = Label(root,text='',font=('arial',25,'bold'),bg='#676767', borderwidth=1, relief="solid")
ans.place(x=80,y=440)

#-------------------------------------------------------

inpp = StringVar()
input1 = Entry(root,font=('chiller',25,'bold'),relief=RIDGE,bd=5,bg='black',justify='center',fg='white',textvariable=inpp)
input1.focus_set()
input1.place(x=210,y=250)
#-------------------------------------------------------
bt1 = Button(root,text='Submit',font=('arial',15,'bold'),width=15,bd=5,bg='#C70039',activebackground='blue'
             ,activeforeground='white',command=hangman)
bt1.place(x=300,y=350)
root.bind("<Return>",jj)
#-------------------------------------------------------


#------------------------------------------------------- 

def chooseword():
    global word,ll,lenword1,lenwordvar,ffdata,temps
    word = loadWords()
    ll = ["_ " for i in word]
    lenword1 = len(word)
    lenwordvar = lenword1
    temps = word
    leftchances.configure(text='Incercari ramase: {}'.format(lenwordvar))
    ffdata = ''
    for i in ll:
        ffdata += i+' '
    wordlabel.configure(text=ffdata)
    ans.configure(text='')

chooseword()
root.mainloop()