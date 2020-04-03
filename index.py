from tkinter import *

def main():
    root = Tk()
    root.geometry("480x600+400+100")
    root.title("Home")
    root.resizable(width=False, height=False)


    def sortear():
        conf1['text'] = str(time1.get())
        conf2['text'] = str(time5.get())
        conf3['text'] = str(time2.get())
        conf4['text'] = str(time6.get())
        conf5['text'] = str(time3.get())
        conf6['text'] = str(time7.get())
        conf7['text'] = str(time4.get())
        conf8['text'] = str(time8.get())

        conf11['text'] = str(time4.get())
        conf22['text'] = str(time7.get())
        conf33['text'] = str(time1.get())
        conf44['text'] = str(time6.get())
        conf55['text'] = str(time2.get())
        conf66['text'] = str(time5.get())
        conf77['text'] = str(time3.get())
        conf88['text'] = str(time8.get())

        conf111['text'] = str(time3.get())
        conf222['text'] = str(time5.get())
        conf333['text'] = str(time4.get())
        conf444['text'] = str(time6.get())
        conf555['text'] = str(time1.get())
        conf666['text'] = str(time7.get())
        conf777['text'] = str(time2.get())
        conf888['text'] = str(time8.get())

        conf1A['text'] = str(time2.get())
        conf2B['text'] = str(time7.get())
        conf3C['text'] = str(time3.get())
        conf4D['text'] = str(time6.get())
        conf5E['text'] = str(time4.get())
        conf6F['text'] = str(time5.get())
        conf7G['text'] = str(time1.get())
        conf8H['text'] = str(time8.get())


    Label(root, text="Sorteio das Equipes",fg='green', font=("Helvetica Neue",25,"bold")).pack()

    Label(root, text="Chave A",fg='red', font=("Helvetica", 15, "bold")).place(x=65, y=50)
    time1 = Entry(root)
    time1.place(x=15, y=80)

    time2 = Entry(root)
    time2.place(x=15, y=110)

    time3 = Entry(root)
    time3.place(x=15, y=140)

    time4 = Entry(root)
    time4.place(x=15, y=170)

    Label(root, text="Chave B",fg='red', font=("Helvetica", 15, "bold")).place(x=325, y=50)
    time5 = Entry(root)
    time5.place(x=270, y=80)

    time6 = Entry(root)
    time6.place(x=270, y=110)

    time7 = Entry(root)
    time7.place(x=270, y=140)

    time8 = Entry(root)
    time8.place(x=270, y=170)

    Button(root, text="Sortea", command=sortear).place(x=15, y=210)

    ##########   PRIMEIRO CHAVEAMENTO   ###########
    conf1 = Label(root, text='')
    conf1.place(x=15, y=260)
    Label(root, text="X").place(x=100, y=260)
    conf2 = Label(root, text='')
    conf2.place(x=140, y=260)

    conf3 = Label(root, text='')
    conf3.place(x=15, y=280)
    Label(root, text="X").place(x=100, y=280)
    conf4 = Label(root, text='')
    conf4.place(x=140, y=280)

    conf5 = Label(root, text='')
    conf5.place(x=15, y=300)
    Label(root, text="X").place(x=100, y=300)
    conf6 = Label(root, text='')
    conf6.place(x=140, y=300)

    conf7 = Label(root, text='')
    conf7.place(x=15, y=320)
    Label(root, text="X").place(x=100, y=320)
    conf8 = Label(root, text='')
    conf8.place(x=140, y=320)

    ##########   SEGUNDO CHAVEAMENTO   ###########
    conf11 = Label(root, text='')
    conf11.place(x=260, y=260)
    Label(root, text="X").place(x=350, y=260)
    conf22 = Label(root, text='')
    conf22.place(x=390, y=260)

    conf33 = Label(root, text='')
    conf33.place(x=260, y=280)
    Label(root, text="X").place(x=350, y=280)
    conf44 = Label(root, text='')
    conf44.place(x=390, y=280)

    conf55 = Label(root, text='')
    conf55.place(x=260, y=300)
    Label(root, text="X").place(x=350, y=300)
    conf66 = Label(root, text='')
    conf66.place(x=390, y=300)

    conf77 = Label(root, text='')
    conf77.place(x=260, y=320)
    Label(root, text="X").place(x=350, y=320)
    conf88 = Label(root, text='')
    conf88.place(x=390, y=320)

    ##########   TERCEIRO CHAVEAMENTO   ###########
    conf111 = Label(root, text='')
    conf111.place(x=15, y=400)
    Label(root, text="X").place(x=100, y=400)
    conf222 = Label(root, text='')
    conf222.place(x=140, y=400)

    conf333 = Label(root, text='')
    conf333.place(x=15, y=420)
    Label(root, text="X").place(x=100, y=420)
    conf444 = Label(root, text='')
    conf444.place(x=140, y=420)

    conf555 = Label(root, text='')
    conf555.place(x=15, y=440)
    Label(root, text="X").place(x=100, y=440)
    conf666 = Label(root, text='')
    conf666.place(x=140, y=440)

    conf777 = Label(root, text='')
    conf777.place(x=15, y=460)
    Label(root, text="X").place(x=100, y=460)
    conf888 = Label(root, text='')
    conf888.place(x=140, y=460)

    ##########   QUARTO CHAVEAMENTO   ###########
    conf1A = Label(root, text='')
    conf1A.place(x=260, y=400)
    Label(root, text="X").place(x=350, y=400)
    conf2B = Label(root, text='')
    conf2B.place(x=390, y=400)

    conf3C = Label(root, text='')
    conf3C.place(x=260, y=420)
    Label(root, text="X").place(x=350, y=420)
    conf4D = Label(root, text='')
    conf4D.place(x=390, y=420)

    conf5E = Label(root, text='')
    conf5E.place(x=260, y=440)
    Label(root, text="X").place(x=350, y=440)
    conf6F = Label(root, text='')
    conf6F.place(x=390, y=440)

    conf7G = Label(root, text='')
    conf7G.place(x=260, y=460)
    Label(root, text="X").place(x=350, y=460)
    conf8H = Label(root, text='')
    conf8H.place(x=390, y=460)

    root.mainloop()
