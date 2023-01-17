from tkinter import *
resultat=0
navig=1
histonav=["début de l'historique"]
histform=histonav[len(histonav)-navig]
livrest=88.54
francche=99.98
euro=100
dollarus=108.22 
roubleru=7418.05
roupiein=8848.59
jpyen=13935.44
dong=2535910.31
page=Tk()
page.configure(background="light gray")
page.title("Convertisseur de devises")
page.geometry('420x520')
lecture=StringVar()
lecture.set(histform)
consigne1=Label(page,text="Entrer votre somme ainsi que votre devise.",font=('times 10'), width=35, height=2).place(x=83,y=45)
consigne2=Label(page,text="La devise écrite en lettre et au singulier.",font=('times 10'), width=35, height=2).place(x=83,y=105)
saisie = Entry(page, bd = 5,width=35).place(x=97,y=75)
output=Label(page,textvariable=resultat,font=('times 10'), width=35, height=2).place(x=83,y=315)
historique=Label(page,textvariable=lecture,font=('times 10'), width=35, height=2).place(x=83,y=365)
boutonlivre = Button(page,text="£",height= 3, width=7,cursor = "hand2").place(x=75,y=175)
boutonfranc = Button(page,text="₣",height= 3, width=7,cursor = "hand2").place(x=145,y=175)
boutoneuro = Button(page,text="€",height= 3, width=7,cursor = "hand2").place(x=215,y=175)
boutondollar = Button(page,text="$",height= 3, width=7,cursor = "hand2").place(x=285,y=175)
boutonrouble = Button(page,text="₽",height= 3, width=7,cursor = "hand2").place(x=75,y=245)
boutonroupie = Button(page,text="₹",height= 3, width=7,cursor = "hand2").place(x=145,y=245)
boutonyen = Button(page,text="¥",height= 3, width=7,cursor = "hand2").place(x=215,y=245)
boutondong = Button(page,text="Đ",height= 3, width=7,cursor = "hand2").place(x=285,y=245)
histoplus = Button(page,text="🡒",height= 3, width=7,cursor = "hand2").place(x=215,y=425)
histominus = Button(page,text="🡐",height= 3, width=7,cursor = "hand2").place(x=145,y=425)
page.mainloop()