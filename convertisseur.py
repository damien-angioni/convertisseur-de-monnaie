from tkinter import *
def Historique(bouton):
    if(bouton=="plus"):
        global navig
        global histonav
        if(navig<=1):
            histform=histonav[len(histonav)-navig]
            lecture.set(histform)
        else:
            navig=navig-1
            histform=histonav[len(histonav)-navig]
            lecture.set(histform)
    if(bouton=="moins"):
        if(navig>=(len(histonav)-1)):
            histform=histonav[len(histonav)-navig]
            lecture.set(histform)
        else:
            navig=navig+1
            histform=histonav[len(histonav)-navig]
            lecture.set(histform)
def clique(toconv):
    global requette
    global resultat
    requette = saisie
    traité = requette.get()
    chk_livrest=traité.__contains__("livre")
    chk_francche=traité.__contains__("franc")
    chk_euro=traité.__contains__("euro")
    chk_dollarus=traité.__contains__("dollar")
    chk_roubleru=traité.__contains__("rouble")
    chk_roupiein=traité.__contains__("roupie")
    chk_jpyen=traité.__contains__("yen")
    chk_dong=traité.__contains__("dong")
    expression=""
    if(chk_livrest==True):
        i=0
        while(i<len(traité)):
            if(traité[i]=="0")or(traité[i]=="1")or(traité[i]=="2")or(traité[i]=="3")or(traité[i]=="4")or(traité[i]=="5")or(traité[i]=="6")or(traité[i]=="7")or(traité[i]=="8")or(traité[i]=="9")or(traité[i]=="."):
                expression=expression+traité[i]
            i=i+1
        if(toconv=="£"):
            devise_traduite=livrest*float(expression)/livrest
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"£")
            histonav.append(str(devise_traduite)+"£")
        elif(toconv=="₣"):
            devise_traduite=francche*float(expression)/livrest
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"₣")
            histonav.append(str(devise_traduite)+"₣")
        elif(toconv=="€"):
            devise_traduite=euro*float(expression)/livrest
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"€")
            histonav.append(str(devise_traduite)+"€")
        elif(toconv=="$"):
            devise_traduite=dollarus*float(expression)/livrest
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"$")
            histonav.append(str(devise_traduite)+"$")
        elif(toconv=="₽"):
            devise_traduite=roubleru*float(expression)/livrest
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"₽")
            histonav.append(str(devise_traduite)+"₽")
        elif(toconv=="₹"):
            devise_traduite=roupiein*float(expression)/livrest
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"₹")
            histonav.append(str(devise_traduite)+"₹")
        elif(toconv=="¥"):
            devise_traduite=jpyen*float(expression)/livrest
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"¥")
            histonav.append(str(devise_traduite)+"¥")
        elif(toconv=="Đ"):
            devise_traduite=dong*float(expression)/livrest
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"Đ")
            histonav.append(str(devise_traduite)+"Đ")
    elif(chk_francche==True):
        i=0
        while(i<len(traité)):
            if(traité[i]=="0")or(traité[i]=="1")or(traité[i]=="2")or(traité[i]=="3")or(traité[i]=="4")or(traité[i]=="5")or(traité[i]=="6")or(traité[i]=="7")or(traité[i]=="8")or(traité[i]=="9")or(traité[i]=="."):
                expression=expression+traité[i]
            i=i+1
        if(toconv=="£"):
            devise_traduite=livrest*float(expression)/francche
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"£")
            histonav.append(str(devise_traduite)+"£")
        elif(toconv=="₣"):
            devise_traduite=francche*float(expression)/francche
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"₣")
            histonav.append(str(devise_traduite)+"₣")
        elif(toconv=="€"):
            devise_traduite=euro*float(expression)/francche
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"€")
            histonav.append(str(devise_traduite)+"€")
        elif(toconv=="$"):
            devise_traduite=dollarus*float(expression)/francche
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"$")
            histonav.append(str(devise_traduite)+"$")
        elif(toconv=="₽"):
            devise_traduite=roubleru*float(expression)/francche
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"₽")
            histonav.append(str(devise_traduite)+"₽")
        elif(toconv=="₹"):
            devise_traduite=roupiein*float(expression)/francche
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"₹")
            histonav.append(str(devise_traduite)+"₹")
        elif(toconv=="¥"):
            devise_traduite=jpyen*float(expression)/francche
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"¥")
            histonav.append(str(devise_traduite)+"¥")
        elif(toconv=="Đ"):
            devise_traduite=dong*float(expression)/francche
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"Đ")
            histonav.append(str(devise_traduite)+"Đ")
    elif(chk_euro==True):
        i=0
        while(i<len(traité)):
            if(traité[i]=="0")or(traité[i]=="1")or(traité[i]=="2")or(traité[i]=="3")or(traité[i]=="4")or(traité[i]=="5")or(traité[i]=="6")or(traité[i]=="7")or(traité[i]=="8")or(traité[i]=="9")or(traité[i]=="."):
                expression=expression+traité[i]
            i=i+1
        if(toconv=="£"):
            devise_traduite=livrest*float(expression)/euro
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"£")
            histonav.append(str(devise_traduite)+"£")
        elif(toconv=="₣"):
            devise_traduite=francche*float(expression)/euro
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"₣")
            histonav.append(str(devise_traduite)+"₣")
        elif(toconv=="€"):
            devise_traduite=euro*float(expression)/euro
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"€")
            histonav.append(str(devise_traduite)+"€")
        elif(toconv=="$"):
            devise_traduite=dollarus*float(expression)/euro
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"$")
            histonav.append(str(devise_traduite)+"$")
        elif(toconv=="₽"):
            devise_traduite=roubleru*float(expression)/euro
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"₽")
            histonav.append(str(devise_traduite)+"₽")
        elif(toconv=="₹"):
            devise_traduite=roupiein*float(expression)/euro
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"₹")
            histonav.append(str(devise_traduite)+"₹")
        elif(toconv=="¥"):
            devise_traduite=jpyen*float(expression)/euro
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"¥")
            histonav.append(str(devise_traduite)+"¥")
        elif(toconv=="Đ"):
            devise_traduite=dong*float(expression)/euro
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"Đ")
            histonav.append(str(devise_traduite)+"Đ")
    elif(chk_dollarus==True):
        i=0
        while(i<len(traité)):
            if(traité[i]=="0")or(traité[i]=="1")or(traité[i]=="2")or(traité[i]=="3")or(traité[i]=="4")or(traité[i]=="5")or(traité[i]=="6")or(traité[i]=="7")or(traité[i]=="8")or(traité[i]=="9")or(traité[i]=="."):
                expression=expression+traité[i]
            i=i+1
        if(toconv=="£"):
            devise_traduite=livrest*float(expression)/dollarus
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"£")
            histonav.append(str(devise_traduite)+"£")
        elif(toconv=="₣"):
            devise_traduite=francche*float(expression)/dollarus
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"₣")
            histonav.append(str(devise_traduite)+"₣")
        elif(toconv=="€"):
            devise_traduite=euro*float(expression)/dollarus
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"€")
            histonav.append(str(devise_traduite)+"€")
        elif(toconv=="$"):
            devise_traduite=dollarus*float(expression)/dollarus
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"$")
            histonav.append(str(devise_traduite)+"$")
        elif(toconv=="₽"):
            devise_traduite=roubleru*float(expression)/dollarus
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"₽")
            histonav.append(str(devise_traduite)+"₽")
        elif(toconv=="₹"):
            devise_traduite=roupiein*float(expression)/dollarus
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"₹")
            histonav.append(str(devise_traduite)+"₹")
        elif(toconv=="¥"):
            devise_traduite=jpyen*float(expression)/dollarus
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"¥")
            histonav.append(str(devise_traduite)+"¥")
        elif(toconv=="Đ"):
            devise_traduite=dong*float(expression)/dollarus
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"Đ")
            histonav.append(str(devise_traduite)+"Đ")
    elif(chk_roubleru==True):
        i=0
        while(i<len(traité)):
            if(traité[i]=="0")or(traité[i]=="1")or(traité[i]=="2")or(traité[i]=="3")or(traité[i]=="4")or(traité[i]=="5")or(traité[i]=="6")or(traité[i]=="7")or(traité[i]=="8")or(traité[i]=="9")or(traité[i]=="."):
                expression=expression+traité[i]
            i=i+1
        if(toconv=="£"):
            devise_traduite=livrest*float(expression)/roubleru
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"£")
            histonav.append(str(devise_traduite)+"£")
        elif(toconv=="₣"):
            devise_traduite=francche*float(expression)/roubleru
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"₣")
            histonav.append(str(devise_traduite)+"₣")
        elif(toconv=="€"):
            devise_traduite=euro*float(expression)/roubleru
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"€")
            histonav.append(str(devise_traduite)+"€")
        elif(toconv=="$"):
            devise_traduite=dollarus*float(expression)/roubleru
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"$")
            histonav.append(str(devise_traduite)+"$")
        elif(toconv=="₽"):
            devise_traduite=roubleru*float(expression)/roubleru
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"₽")
            histonav.append(str(devise_traduite)+"₽")
        elif(toconv=="₹"):
            devise_traduite=roupiein*float(expression)/roubleru
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"₹")
            histonav.append(str(devise_traduite)+"₹")
        elif(toconv=="¥"):
            devise_traduite=jpyen*float(expression)/roubleru
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"¥")
            histonav.append(str(devise_traduite)+"¥")
        elif(toconv=="Đ"):
            devise_traduite=dong*float(expression)/roubleru
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"Đ")
            histonav.append(str(devise_traduite)+"Đ")
    elif(chk_roupiein==True):
        i=0
        while(i<len(traité)):
            if(traité[i]=="0")or(traité[i]=="1")or(traité[i]=="2")or(traité[i]=="3")or(traité[i]=="4")or(traité[i]=="5")or(traité[i]=="6")or(traité[i]=="7")or(traité[i]=="8")or(traité[i]=="9")or(traité[i]=="."):
                expression=expression+traité[i]
            i=i+1
        if(toconv=="£"):
            devise_traduite=livrest*float(expression)/roupiein
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"£")
            histonav.append(str(devise_traduite)+"£")
        elif(toconv=="₣"):
            devise_traduite=francche*float(expression)/roupiein
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"₣")
            histonav.append(str(devise_traduite)+"₣")
        elif(toconv=="€"):
            devise_traduite=euro*float(expression)/roupiein
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"€")
            histonav.append(str(devise_traduite)+"€")
        elif(toconv=="$"):
            devise_traduite=dollarus*float(expression)/roupiein
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"$")
            histonav.append(str(devise_traduite)+"$")
        elif(toconv=="₽"):
            devise_traduite=roubleru*float(expression)/roupiein
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"₽")
            histonav.append(str(devise_traduite)+"₽")
        elif(toconv=="₹"):
            devise_traduite=roupiein*float(expression)/roupiein
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"₹")
            histonav.append(str(devise_traduite)+"₹")
        elif(toconv=="¥"):
            devise_traduite=jpyen*float(expression)/roupiein
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"¥")
            histonav.append(str(devise_traduite)+"¥")
        elif(toconv=="Đ"):
            devise_traduite=dong*float(expression)/roupiein
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"Đ")
            histonav.append(str(devise_traduite)+"Đ")
    elif(chk_jpyen==True):
        i=0
        while(i<len(traité)):
            if(traité[i]=="0")or(traité[i]=="1")or(traité[i]=="2")or(traité[i]=="3")or(traité[i]=="4")or(traité[i]=="5")or(traité[i]=="6")or(traité[i]=="7")or(traité[i]=="8")or(traité[i]=="9")or(traité[i]=="."):
                expression=expression+traité[i]
            i=i+1
        if(toconv=="£"):
            devise_traduite=livrest*float(expression)/jpyen
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"£")
            histonav.append(str(devise_traduite)+"£")
        elif(toconv=="₣"):
            devise_traduite=francche*float(expression)/jpyen
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"₣")
            histonav.append(str(devise_traduite)+"₣")
        elif(toconv=="€"):
            devise_traduite=euro*float(expression)/jpyen
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"€")
            histonav.append(str(devise_traduite)+"€")
        elif(toconv=="$"):
            devise_traduite=dollarus*float(expression)/jpyen
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"$")
            histonav.append(str(devise_traduite)+"$")
        elif(toconv=="₽"):
            devise_traduite=roubleru*float(expression)/jpyen
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"₽")
            histonav.append(str(devise_traduite)+"₽")
        elif(toconv=="₹"):
            devise_traduite=roupiein*float(expression)/jpyen
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"₹")
            histonav.append(str(devise_traduite)+"₹")
        elif(toconv=="¥"):
            devise_traduite=jpyen*float(expression)/jpyen
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"¥")
            histonav.append(str(devise_traduite)+"¥")
        elif(toconv=="Đ"):
            devise_traduite=dong*float(expression)/jpyen
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"Đ")
            histonav.append(str(devise_traduite)+"Đ")
    elif(chk_dong==True):
        i=0
        while(i<len(traité)):
            if(traité[i]=="0")or(traité[i]=="1")or(traité[i]=="2")or(traité[i]=="3")or(traité[i]=="4")or(traité[i]=="5")or(traité[i]=="6")or(traité[i]=="7")or(traité[i]=="8")or(traité[i]=="9")or(traité[i]=="."):
                expression=expression+traité[i]
            i=i+1
        if(toconv=="£"):
            devise_traduite=livrest*float(expression)/dong
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"£")
            histonav.append(str(devise_traduite)+"£")
        elif(toconv=="₣"):
            devise_traduite=francche*float(expression)/dong
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"₣")
            histonav.append(str(devise_traduite)+"₣")
        elif(toconv=="€"):
            devise_traduite=euro*float(expression)/dong
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"€")
            histonav.append(str(devise_traduite)+"€")
        elif(toconv=="$"):
            devise_traduite=dollarus*float(expression)/dong
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"$")
            histonav.append(str(devise_traduite)+"$")
        elif(toconv=="₽"):
            devise_traduite=roubleru*float(expression)/dong
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"₽")
            histonav.append(str(devise_traduite)+"₽")
        elif(toconv=="₹"):
            devise_traduite=roupiein*float(expression)/dong
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"₹")
            histonav.append(str(devise_traduite)+"₹")
        elif(toconv=="¥"):
            devise_traduite=jpyen*float(expression)/dong
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"¥")
            histonav.append(str(devise_traduite)+"¥")
        elif(toconv=="Đ"):
            devise_traduite=dong*float(expression)/dong
            devise_traduite=round(devise_traduite,2)
            resultat.set(str(devise_traduite)+"Đ")
            histonav.append(str(devise_traduite)+"Đ")
    else:
        resultat.set("Devise non traitable, essayez autre chose...")
devise_traduite=0.00
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
consigne2=Label(page,text="La devise écrite en lettre, en minuscule.",font=('times 10'), width=35, height=2).place(x=83,y=105)
saisie = Entry(page, bd = 5,width=35)
saisie.place(x=97,y=75)
resultat=StringVar()
output=Label(page,textvariable=resultat,font=('times 10'), width=35, height=2)
output.place(x=83,y=315)
historique=Label(page,textvariable=lecture,font=('times 10'), width=35, height=2)
historique.place(x=83,y=365)
boutonlivre = Button(page,text="£",height= 3,command=lambda: clique("£"), width=7,cursor = "hand2").place(x=75,y=175)
boutonfranc = Button(page,text="₣",height= 3,command=lambda: clique("₣"), width=7,cursor = "hand2").place(x=145,y=175)
boutoneuro = Button(page,text="€",height= 3,command=lambda: clique("€"), width=7,cursor = "hand2").place(x=215,y=175)
boutondollar = Button(page,text="$",height= 3,command=lambda: clique("$"), width=7,cursor = "hand2").place(x=285,y=175)
boutonrouble = Button(page,text="₽",height= 3,command=lambda: clique("₽"), width=7,cursor = "hand2").place(x=75,y=245)
boutonroupie = Button(page,text="₹",height= 3,command=lambda: clique("₹"), width=7,cursor = "hand2").place(x=145,y=245)
boutonyen = Button(page,text="¥",height= 3,command=lambda: clique("¥"), width=7,cursor = "hand2").place(x=215,y=245)
boutondong = Button(page,text="Đ",height= 3,command=lambda: clique("Đ"), width=7,cursor = "hand2").place(x=285,y=245)
histoplus = Button(page,text="🡒",height= 3,command=lambda: Historique("plus"), width=7,cursor = "hand2").place(x=215,y=425)
histominus = Button(page,text="🡐",height= 3,command=lambda: Historique("moins"), width=7,cursor = "hand2").place(x=145,y=425)
page.mainloop()