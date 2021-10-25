from tkinter import *
from PIL import ImageTk,Image
import random

p1_score=0
p2_score=0

root=Tk()
root.title("Endless dice game")
root.geometry("600x400")
root.configure(background="light coral")

i_charmander=ImageTk.PhotoImage(Image.open("charmender.jpg"))
i_pikachu=ImageTk.PhotoImage(Image.open("pikachu.jpg"))
i_persion=ImageTk.PhotoImage(Image.open("persion.jpg"))
i_bulbasour=ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
i_abra=ImageTk.PhotoImage(Image.open("abra.jpg"))
i_nidoking=ImageTk.PhotoImage(Image.open("nidoking.jpg"))
i_paras=ImageTk.PhotoImage(Image.open("paras.jpg"))
i_Iyvasour=ImageTk.PhotoImage(Image.open("Iyvasour.jpg"))
i_ratata=ImageTk.PhotoImage(Image.open("ratata.jpg"))
i_jigglypuff=ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
i_kadabra=ImageTk.PhotoImage(Image.open("kadabra.jpg"))
i_meowth=ImageTk.PhotoImage(Image.open("meowth.jpg"))
i_squirtle=ImageTk.PhotoImage(Image.open("squirtle.jpg"))
img_button=ImageTk.PhotoImage(Image.open("button.jpg"))

player1=Label(root,text="Player 1",bg="dark blue",fg="turquoise")
player1.place(relx=0.1,rely=0.3,anchor=CENTER)

player2=Label(root,text="Player 2",bg="dark blue",fg="turquoise")
player2.place(relx=0.9,rely=0.3,anchor=CENTER)

player1_score=Label(root,bg="light green",fg="orange")
player1_score.place(relx=0.1,rely=0.4,anchor=CENTER)

player2_score=Label(root,bg="light green",fg="orange")
player2_score.place(relx=0.9,rely=0.4,anchor=CENTER)

pokemonlist=[i_charmander,i_pikachu,i_persion,i_bulbasour,i_abra,i_nidoking,i_paras,i_Iyvasour,i_ratata,i_jigglypuff,i_kadabra,i_meowth,i_squirtle]
powerlist=[50,200,70,60,30,90,40,100,40,70,70,60,50]
label=Label(root)
label.place(relx=0.5,rely=0.5,anchor=CENTER)

def Player1():
    global p1_score
    randomnumber=random.randint(1,13)
    randompokemon=pokemonlist[randomnumber]
    label["image"]=randompokemon
    
    randompowerlist=powerlist[randomnumber]
    p1_score=p1_score+randompowerlist
    player1_score["text"]=str(p1_score)

player1_btn=Button(root,image=img_button,command=Player1)
player1_btn.place(relx=0.1,rely=0.6,anchor=CENTER)


def Player2():
    global p2_score
    randomnumber2=random.randint(1,13)
    randompokemon2=pokemonlist[randomnumber2]
    label["image"]=randompokemon2
    
    randompowerlist2=powerlist[randomnumber2]
    p2_score=p2_score+randompowerlist2
    player2_score["text"]=str(p2_score)

player2_btn=Button(root,image=img_button,command=Player2)
player2_btn.place(relx=0.9,rely=0.6,anchor=CENTER)




root.mainloop()





