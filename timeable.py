from tkinter import*
from tkinter.font import Font
from tkinter.messagebox import *
def failist_sõnastikusse():
    tund_kirjeldus={}
    file=open("Tund.txt","r")
    for line in file:
        tund,kirjeldus=line.strip().split(":")
        tund_kirjeldus[tund.strip()]=kirjeldus.strip()
    file.close()
    return tund_kirjeldus

def kirjeldus():
    pass

def kirjeldus_aknasse(t:str):
    if (askyesno("Küsimus","Kas tahad kirjeldust näha?")):
        alam_aken=Toplevel()
        lbl_kirjeldus=Label(alam_aken,text=tund_kirjeldus[t]).pack()
    else:
        showinfo("Vastus","Kui ei taha, siis ei taha!!!")
tund_kirjendus={}
aken=Tk()
aken.title("Tunniplaan TARpv21")
aken.geometry("1920x1080")
p=["Esmaspäev","Teisipäev","Kolmapäev","Neljapäev","Reede"]
tund_kirjeldus=failist_sõnastikusse()
j=0
for i in range(1,10,2):
    paev=Label(aken, text=p[j],relief="solid",font="Calibri 25").grid(row=i, column=0, rowspan=2, sticky=N+S+W+E)
    j+=1

kell=["7:40-8:25","8:30-9:15","9:20-10:05","10:10-10:55","11:00-11:45","11:50-12:35","12:40-13:25","13:30-14:15","14:20-15:05","15:10-15:55","16:00-16:45"]
for i in range(11):
    tund="t"+str(i)
    tund=tund1=Label(aken, text=str(i)+"\n"+kell[i], relief="solid",font="Calibri 15").grid(row=0, column=i+1, sticky=N+S+W+E)

#Понедельник
p1=Button(text="Multimeedia", font="Calibri 20",bg="cornflowerblue",relief="groove",command=lambda:kirjeldus_aknasse("Multimeedia")).grid(row=1,column=2,columnspan=2,sticky=N+S+W+E)
p2=Button(text="Programmeerimise alused", font="Calibri 20",bg="skyblue",relief="groove",command=lambda:kirjeldus_aknasse("Programmeerimise alused")).grid(row=2,column=2,columnspan=3,sticky=N+S+W+E)
p3=Button(text="Programmeerimise alused", font="Calibri 20",bg="skyblue",relief="groove",command=lambda:kirjeldus_aknasse("Programmeerimise alused")).grid(row=1,column=5,columnspan=3,sticky=N+S+W+E)
p4=Button(text="Multimeedia", font="Calibri 20",bg="cornflowerblue",relief="groove",command=lambda:kirjeldus_aknasse("Multimeedia")).grid(row=2,column=5,columnspan=2,sticky=N+S+W+E)
p5=Button(text="Rühma juhatuja tund", font="Calibri 20",bg="skyblue",relief="groove",command=lambda:kirjeldus_aknasse("Rühma juhatuja tund")).grid(row=1,column=8,rowspan=2,sticky=N+S+W+E)

#Вторник
p6=Button(text="Inglise keel", font="Calibri 26",bg="floralwhite",relief="groove",command=lambda:kirjeldus_aknasse("Inglise Keel Grupp 1")).grid(row=3,column=2,columnspan=2,sticky=N+S+W+E)
p7=Button(text="Inglise keel", font="Calibri 26",bg="mediumslateblue",relief="groove",command=lambda:kirjeldus_aknasse("Inglise Keel Grupp 2")).grid(row=4,column=2,columnspan=2,sticky=N+S+W+E)
p8=Button(text="Operatsioonisüsteemide alused", font="Calibri 26",bg="mediumorchid",relief="groove",command=lambda:kirjeldus_aknasse("Operatsioonisüsteemide alused")).grid(row=3,column=4,columnspan=2,rowspan=2,sticky=N+S+W+E)
p10=Button(text="Kehaline kasvatus", font="Calibri 26",bg="palevioletred",relief="groove",command=lambda:kirjeldus_aknasse("Kehaline kasvatus")).grid(row=3,column=7,columnspan=2,rowspan=2,sticky=N+S+W+E)
p11=Button(text="Eesti keel", font="Calibri 26",bg="mediumpurple",relief="groove",command=lambda:kirjeldus_aknasse("Eesti Keel Grupp 1")).grid(row=3,column=9,sticky=N+S+W+E)
p12=Button(text="Eesti keel", font="Calibri 26",bg="darkgrey",relief="groove",command=lambda:kirjeldus_aknasse("Eesti Keel Grupp 2")).grid(row=4,column=9,sticky=N+S+W+E)
p13=Button(text="Ajalugu", font="Calibri 26",bg="khaki",relief="groove",command=lambda:kirjeldus_aknasse("Ajalugu")).grid(row=3,column=10,rowspan=2,sticky=N+S+W+E)

#Среда
p14=Button(text="Programmeerimise alused", font="Calibri 26",bg="skyblue",relief="groove",command=lambda:kirjeldus_aknasse("Programmeerimise alused")).grid(row=5,column=2,columnspan=3,sticky=N+S+W+E)
p15=Button(text="Multimeedia", font="Calibri 26",bg="cornflowerblue",relief="groove",command=lambda:kirjeldus_aknasse("Multimeedia")).grid(row=6,column=2,columnspan=3,sticky=N+S+W+E)
p16=Button(text="Multimeedia", font="Calibri 26",bg="cornflowerblue",relief="groove",command=lambda:kirjeldus_aknasse("Multimeedia")).grid(row=6,column=6,columnspan=3,sticky=N+S+W+E)
p17=Button(text="Programmeerimise alused", font="Calibri 26",bg="skyblue",relief="groove",command=lambda:kirjeldus_aknasse("Programmeerimise alused")).grid(row=5,column=6,columnspan=3,sticky=N+S+W+E)
p18=Button(text="Kunstiained", font="Calibri 26",bg="orchid",relief="groove",command=lambda:kirjeldus_aknasse("Kunstiained")).grid(row=5,column=9,columnspan=2,rowspan=2,sticky=N+S+W+E)

#Четверг
p19=Button(text="Andmebaasisüsteemide alused", font="Calibri 26",bg="DeepPink1",relief="groove",command=lambda:kirjeldus_aknasse("Andmebaasisüsteemide alused")).grid(row=7,column=2,columnspan=5,rowspan=2,sticky=N+S+W+E)
p20=Button(text="Ajalugu", font="Calibri 26",bg="khaki",relief="groove",command=lambda:kirjeldus_aknasse("Ajalugu")).grid(row=7,column=6,rowspan=2,sticky=N+S+W+E)
p21=Button(text="Eesti keel", font="Calibri 26",bg="mediumpurple",relief="groove",command=lambda:kirjeldus_aknasse("Eesti Keel Grupp 1")).grid(row=7,column=7,sticky=N+S+W+E)
p22=Button(text="Eesti keel", font="Calibri 26",bg="darkgrey",relief="groove",command=lambda:kirjeldus_aknasse("Eesti Keel Grupp 2")).grid(row=8,column=7,sticky=N+S+W+E)

#Пятница
p23=Button(text="Vene keel", font="Calibri 26",bg="greenyellow",relief="groove",command=lambda:kirjeldus_aknasse("Keel ja Kirjandus")).grid(row=9,column=3,columnspan=2,rowspan=3,sticky=N+S+W+E)
p24=Button(text="Matemaatika", font="Calibri 26",bg="lightpink",relief="groove",command=lambda:kirjeldus_aknasse("Matemaatika")).grid(row=9,column=6,columnspan=2,rowspan=2,sticky=N+S+W+E)
p25=Button(text="Suhtlemine ja kliienditeenindus", font="Calibri 26",bg="mediumslateblue",relief="groove",command=lambda:kirjeldus_aknasse("Suhtlemine ja Klienditeenindus")).grid(row=9,column=8,columnspan=2,rowspan=2,sticky=N+S+W+E)
p26=Button(text="Ajalugu", font="Calibri 26",bg="khaki",relief="groove",command=lambda:kirjeldus_aknasse("Ajalugu")).grid(row=9,column=10,rowspan=2,sticky=N+S+W+E)

aken.mainloop()
