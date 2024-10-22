from tkinter import *
import random
import pickle


root = Tk()
class Frame1:
    def __init__(self, root):
        self.root = root
        self.initUI()
        self.NOVICE = BooleanVar()
        self.WHIZ = BooleanVar()
        self.EXPERT = BooleanVar()
        self.GRANDMASTER = BooleanVar()

    def initUI(self):
        root.geometry('400x500')
        # frame1 = Frame(self.root, bg='aquamarine', width=900, height=1000)
        tn = PhotoImage(file="front-page.gif")
        la1 = Label(self.root, image=tn)
        la1.image = tn

        but1 = Button(la1, text='Play', height=0, width=0, font=(('Times', 'New', 'Roman'), 26))
        but3 = Button(la1, text='LEVEL', relief=FLAT, bg='silver', activebackground='yellow', font=((), 23))
        but4 = Button(la1, text='ABOUT', relief=FLAT, bg='silver', font=((), '25'))

        def second_frame_play():
            root.geometry('650x500')
            frame2 = Frame(root, bg='silver', height=70, width=50)
            frame2.pack(expand=YES, fill=BOTH)
            lab1_2 = Label(frame2, background='#E6E6E6')
            # lab1_2.columnconfigure(0, weight=5)
            lab1_2.place(x=1, y=0, width=650)
            tb = PhotoImage(file="goback.gif", height=15, width=15)
            but2 = Button(lab1_2, image=tb, height=15, width=15, relief=FLAT, takefocus='blue')
            but2.image = tb
            but2.pack(side=LEFT)
            lab2 = Label(frame2, text='Enter your\ncode here: ', bg='silver', font=((), 7))
            lab2.place(x=562, y=30)
            lab22 = Label(frame2, text='ME', foreground='black', bg='white',  font=((), 15), width=15)
            lab22.place(x=155, y=81)
            lab23 = Label(frame2, text='YOU', bg='white',  font=((), 15), width=15)
            lab23.place(x=328, y=81)
            lab20 = Label(frame2, bg='silver', width=450)
            lab20.place(x=155, y=108)
            if self.NOVICE.get():
                print('Novice')
            if self.EXPERT.get():
                print('Expert')
            if self.GRANDMASTER.get():
                print('Grandmaster')

            def make_code():
                """Used to make computer code that will be guessed by the player"""
                code_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

                comp_code_list = []
                # liss = set(comp_code_list)

                while len(comp_code_list) < 4:
                    see = random.choice(code_digits)
                    # code_digits.remove(see)
                    comp_code_list.append(see)
                    # print(see)
                    if comp_code_list[0] <= 4:
                        wer = random.randint(5, 9)
                        comp_code_list[0] = wer
                        code_digits.append(see)
                        # code_digits.remove(wer)
                    if len(comp_code_list) == 2:
                        # print('ans = ',comp_code_list[0] - comp_code_list[1])
                        fry = [3, 2, 1, 0, -1, -2, -3]
                        ser = []
                        while comp_code_list[0] - comp_code_list[1] in fry:
                            er = random.randint(1, 6)
                            comp_code_list[1] = er
                            ser.append(er)

                    if len(comp_code_list) == 3:
                        while comp_code_list[2] == comp_code_list[1]:
                            comp_code_list[2] = random.choice(code_digits)
                        jike = [2, 1, 0, -1, -2]
                        while comp_code_list[1] - comp_code_list[2] in jike:
                            br = random.choice(code_digits)
                            comp_code_list[2] = br

                    if len(comp_code_list) == 4:
                        while comp_code_list[2] == comp_code_list[3]:
                            comp_code_list[3] = random.choice(code_digits)
                        # code_digits.remove(comp_code_list[3])
                        fike = [2, 1, 0, -1, -2]
                        kite = [1, 0, -1]
                        while comp_code_list[2] - comp_code_list[3] in fike or comp_code_list[0] - comp_code_list[3] in fike:
                            br = random.choice(code_digits)
                            comp_code_list[3] = br

                    if comp_code_list[0] in code_digits:
                        code_digits.remove(comp_code_list[0])
                    elif comp_code_list[1] in code_digits:
                        code_digits.remove(comp_code_list[1])
                    elif comp_code_list[2] in code_digits:
                        code_digits.remove(comp_code_list[2])
                    elif comp_code_list[3] in code_digits:
                        code_digits.remove(comp_code_list[3])
                return comp_code_list
            mk_code = make_code()
            print('this is my code: ', mk_code)

            def check_code(make_code, player_guess):
                """check computer's code with player's guess if is code is dead or injured"""
                dead = 0
                injures = 0
                list_nos = list(make_code)
                # print(list_nos.index(1))
                players_no = list(player_guess)
                for i in list_nos:
                    for j in players_no:
                        # print(i,j)
                        if int(j) == int(i):

                            if list_nos.index(i) == players_no.index(j):
                                # print(i,j)
                                dead += 1
                                # print(dead, 'd', sep='')

                            if make_code.index(i) != player_guess.index(j):
                                injures += 1
                result = str(dead) + str(injures)
                return result

            def final_code(code_stored):
                lis = []
                xcd = open('codu.pkl', 'rb')
                f = pickle.load(xcd)
                cs = code_stored
                for i in cs:
                    p = i[1]
                    o = str(i[0])
                    if len(str(o)) == 1:
                        l = '0' + o
                    else:
                        l = o
                    for j in f:
                        cg = check_code(j, p)
                        print(j)
                        if str(cg) == l:
                            lis.append(j)
                        if lis.count(j) == 6:
                            return j

            code = StringVar(value='')

            def valid_entry1_command(var, indx, mode, event=None):
                y = 0
                try:

                    nonlocal entry1
                    codee = str(code.get())
                    codeee = set(codee)
                    if len(codee) > 4:
                        nonlocal entry1
                        entry1.delete(4)

                    else:
                        print('yes')
                        pass
                    if len(codee) != len(codeee):

                        y += 1
                        entry1.delete(y, END)
                    else:
                        pass

                except TclError:
                    print('tclerror')
                    pass
            code.trace("w", valid_entry1_command)
            entry1 = Entry(frame2, textvariable=code, width=4)

            entry1.place(x=615, y=32)
            lab3 = Label(frame2, text='Enter the result\n(dead, injured)', bg='silver', font=((), 7))
            lab3.place(x=5, y=30)

            code2 = IntVar(value='')

            def valid_entry2_command(var, indx, mode):
                print('hello')
                try:
                    codee2 = str(code2.get())
                    if len(codee2) > 2:
                        nonlocal entry2
                        entry2.delete(2)
                    else:
                        pass

                except TclError:
                    print('tclerror')
                    pass

            code2.trace("w", valid_entry2_command)
            entry2 = Entry(frame2, textvariable=code2, width=2)
            entry2.place(x=75, y=32)

            code4 = ''
            lab4= Label(frame2, width=15, height=15, text=code4,  font=((), 15), anchor=NW)
            lab4.place(x=155, y=110)

            code5 = ''
            lab5 = Label(frame2,  width=15, height=15, text=code5,  font=((), 15), anchor=NW)
            lab5.place(x=328, y=110)

            entry1.focus_set()

            listy = []
            listy11 = listy.copy()

            guesses = ['0123', '3456', '6789', '9012', '2345', '8903', '2190', '1234']

            def computer_guess(guesses):
                """makes six guesses of player's code"""

                rand_choice = random.choice(guesses)
                guesses.remove(rand_choice)
                return rand_choice

            def code_store(make_cde, playr_result, goj):
                """makes a list of dictionaries that store the computer guess and the player's result"""


                dio = playr_result
                code = make_cde
                code_tuple = (dio, code)
                goj.append(code_tuple)
                return goj
            c_guess = ''

            def c_gue(event=None):
                nonlocal guesses
                nonlocal lab5
                nonlocal code5
                nonlocal entry2
                nonlocal c_guess
                nonlocal goj
                fn_code = final_code(goj)
                entry2.focus_set()
                c_guess = computer_guess(guesses)
                if len(goj) == 6:
                    code5 += str(fn_code) + '\t      '
                else:
                    code5 += str(c_guess) + '\t      '

                lab5.config(text=code5)

            def winwin(event=None):
                frame2.destroy()
                self.initUI()

            def winner_code(event=None):

                fr01 = Label(frame2, text='I WON', width=30, height=9, background='brown')
                fr01.place(x=180, y=100)
                lab5.config(state=DISABLED)

                but6 = Button(fr01, text='EXIT', command=lambda: winwin())
                but6.place(x=56, y=45)

            def change_code(event=None):
                code_frame = Toplevel(root, takefocus=True)
                code_frame.focusmodel(model='passive')
                code_frame.geometry('200x200+150+150')
                code_frame.positionfrom(who='program')

                code_frame.transient(root)
                nonlocal listy
                lab_11 = Label(code_frame, text='Enter the index you\n you want to change')
                lab_11.grid(row=2, column=1)
                cod_ch = ''
                entry_1 = Entry(code_frame, width=4, textvariable=cod_ch)
                entry_1.grid(row=2, column=2)
            but5 = Button(lab1_2, text='change code', relief=FLAT)
            but5.pack(side=LEFT, padx=5)
            but5.bind('<Button-1>', change_code)

            def listy1(event=None):
                my_code = entry1.get()
                nonlocal listy11

                try:
                    my_code_int = int(my_code)
                    listy11.append(my_code_int)

                    nonlocal code4
                    nonlocal lab4
                    nonlocal lab5
                    nonlocal mk_code
                    everyy = str(my_code_int)
                    eve = everyy + '\t       '
                    ck_code = str(check_code(mk_code, everyy))
                    ck_cod = ck_code[0] + 'd' + ck_code[1] + 'i\n'
                    listy.append(eve)
                    listy.append(ck_cod)
                    code4 = ''.join(listy)
                    print(code4)
                    if ck_code == '40':
                        lab4.after(2100, lambda: winner_code())

                    lab4 = Label(frame2, width=15, height=15, justify='left', text=code4,  font=((), 15), anchor=NW)
                    lab4.place(x=155, y=110)
                    print(len(entry1.get()))
                    if len(entry1.get()) > 4 or type(entry1.get()) == 'str':
                        print('error')
                        listy.remove(my_code_int)
                    entry1.delete(0, 4)
                except ValueError or len(my_code) < 4 or len(my_code) > 4:

                    print('your code cannot be of type str')
                entry1.config(state=DISABLED)
                entry2.config(state=NORMAL)
                nonlocal lab5
                lab5.after(3500, lambda: c_gue())

            listy20 = []
            listy21 = listy.copy()
            goj = []

            def listy2(event=None):
                my_code1 = entry2.get()
                if my_code1 == '40':
                    winner_code()
                nonlocal listy20

                try:
                    my_code_int1 = int(my_code1)

                    listy20.append(my_code_int1)

                    for ever in listy20:
                        nonlocal guesses
                        listy21.append(ever)
                        nonlocal code5
                        nonlocal lab5
                        nonlocal goj
                        lab5.destroy()
                        everr = str(ever)
                        try:
                            code5 += everr[0] + 'd' + everr[1] + 'i' + '\n'
                        except IndexError:
                            code5 += '0' + 'd' + everr[0] + 'i' + '\n'
                        if len(everr) == 1:
                            ev = '0' + everr[0]
                            ev_s = str(ev)
                            cd_store = code_store(c_guess, ev_s, goj)
                        else:
                            cd_store = code_store(c_guess, ever, goj)

                        print(cd_store)
                        lab5 = Label(frame2, width=15, height=15, justify='left', text=code5, font=((), 15), anchor=NW)
                        lab5.place(x=328, y=110)

                        listy20.remove(ever)

                    if len(entry2.get()) > 2 or type(entry2.get()) == 'str':
                        print('error')
                        listy20.remove(my_code_int1)
                    entry2.delete(0, 2)
                except ValueError or len(my_code1) < 2 or len(my_code1) > 2:

                    print('your code cannot be of type str')
                entry2.config(state=DISABLED)
                entry1.config(state=NORMAL)
                entry1.focus_set()

            entry2.bind("<Return>", listy2)
            entry1.bind("<Return>", listy1)

            if len(entry1.get()) == 4:
                print('hello')

            def go_back(event=None):
                nonlocal frame2
                frame2.destroy()
                self.initUI()

            but2.bind('<Button-1>', go_back)

        def change_frame(event=None):
            la1.destroy()
            second_frame_play()

        def level_frame(event=None):
            la1.destroy()
            frame_lf1 = Frame(root, bg='silver', width=50, height=70)
            frame_lf1.pack(expand=YES, fill=BOTH)
            lab_sub = Label(frame_lf1, bg='#E6E6E6', width=450)
            lab_sub.place(x=1, y=0, width=450)
            tb = PhotoImage(file="goback.gif", height=15, width=15)
            but2 = Button(lab_sub, image=tb, height=15, width=15, relief=FLAT, takefocus='blue')
            but2.image = tb
            but2.pack(side=TOP, anchor=W)
            frame00 = LabelFrame(frame_lf1, bg='#E6E6E6', text='Level', width=150, height=160, relief=GROOVE, borderwidth=2, labelanchor=NW, pady=0)
            frame00.place(x=145, y=80)

            def onclick(event=None):
                if self.NOVICE.get():
                    self.WHIZ.set(False)
                    self.EXPERT.set(False)
                    self.GRANDMASTER.set(False)

            def onclick1(event=None):
                if self.WHIZ.get():
                    self.NOVICE.set(False)
                    self.EXPERT.set(False)
                    self.GRANDMASTER.set(False)

            def onclick2(event=None):
                if self.EXPERT.get():
                    self.WHIZ.set(False)
                    self.NOVICE.set(False)
                    self.GRANDMASTER.set(False)

            def onclick3(event=None):
                if self.GRANDMASTER.get():
                    self.WHIZ.set(False)
                    self.EXPERT.set(False)
                    self.NOVICE.set(False)

            check_but = Checkbutton(frame_lf1, text='Novice', variable=self.NOVICE, command=onclick, bg='#E6E6E6')
            check_but.place(x=180, y=100)
            check_but1 = Checkbutton(frame_lf1, text='Whiz', variable=self.WHIZ, command=onclick1, bg='#E6E6E6')
            check_but1.place(x=180, y=130)
            check_but2 = Checkbutton(frame_lf1, text='Expert', variable=self.EXPERT, command=onclick2, bg='#E6E6E6')
            check_but2.place(x=180, y=160)
            check_but3 = Checkbutton(frame_lf1, text='Grandmaster', variable=self.GRANDMASTER, command=onclick3, bg='#E6E6E6')
            check_but3.place(x=180, y=190)

            def go_back(event=None):
                nonlocal frame_lf1
                frame_lf1.destroy()
                self.initUI()

            but2.bind('<Button-1>', go_back)

        la1.pack(fill=BOTH, expand=YES)
        la1.config(height=500, width=400)
        but1.bind('<Button-1>', change_frame)
        but3.bind('<Button-1>', level_frame)
        but1.pack(pady=70)
        but3.pack(pady=0)
        but4.pack(pady=70)
        # frame1.pack(expand=YES, fill=BOTH)


root.resizable(width=False, height=False)
root.geometry('400x500')
# root.wm_attributes("-transparentcolor",'grey', )
fr = Frame1(root=root)


root.mainloop()
