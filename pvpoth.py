import customtkinter as ctk
class gam():
    def __init__(et,wnd):
        et.brd = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
        et.wnd = wnd
        et.wnd.title('Thisdestrydmybren!')
        et.wnd.geometry('800x600')
        et.frm = ctk.CTkFrame(et.wnd,width=250,height=125,fg_color='#013220')
        et.frm.place(x=187,y=150)
        et.stf = ctk.CTkFrame(et.wnd,width=197,height=576,fg_color='#013220',corner_radius=15)
        et.stf.place(x=600,y=10)
        et.can = ctk.CTkCanvas(et.wnd,bg='#013220',width=180,height=575, highlightthickness=0)
        et.can.place(x=610,y=10)
        et.can.create_line(0, 10, 0, 560, width=1, fill="White")
        et.relp = ''
        et.pmoc = ''
        et.br = {}
        et.mvs = -1
        et.nd = 0

        et.hed = ctk.CTkLabel(et.frm,text_color='White',text='Othello',font=('Comic Sans MS',40))
        et.hed.place(x=50,y=5)
        et.ins = ctk.CTkLabel(et.frm,text_color='#1fd655',text='Choose your coin color-',font=('Comic Sans MS',20))
        et.ins.place(x=20,y=50)
        et.blwh = ctk.CTkButton(et.frm,text_color='White',fg_color='black',text='Black',command=lambda: et.sttr('Black','White'),width=10)
        et.blwh.place(x=75, y=85)
        et.whbl = ctk.CTkButton(et.frm,text_color='black',fg_color='White',text='White',command=lambda: et.sttr('White','Black'),width=10)
        et.whbl.place(x=130, y=85)
        et.trnlbl = et.can.create_text(90, 90, text='', fill="White", font=('Comic Sans MS', 16))
        et.cnt = et.can.create_text(90, 150, text='', fill="White", font=('Comic Sans MS', 16))
    def sttr(et,pl,cm):
        et.ins.destroy()
        et.blwh.destroy()
        et.whbl.destroy()
        et.relp,et.pmoc = pl,cm
        et.str = ctk.CTkButton(et.frm,text='Start',text_color='White',fg_color='#089383',command=et.btun,width=90,height=30,font=('Comic Sans MS',20,'bold'))
        et.str.place(x=80,y=70)
    def btun(et):
        for widget in et.frm.winfo_children():
            widget.destroy()
        et.frm.place(x=5,y=5)
        for r in range(8):
            for s in range(8):
                et.bt = ctk.CTkButton(et.frm,width=70,height=70,text='',border_spacing=0,fg_color='green',state='disabled',border_width=2,border_color='#1fd655',font=('Arial',50))
                et.bt.grid(row=r, column=s, padx=2, pady=2)
                et.br[(r, s)] = et.bt
        et.brd[3][3] = 1
        et.brd[4][3] = 2
        et.brd[3][4] = 2
        et.brd[4][4] = 1
        et.br[(3,3)].configure(text='●',text_color_disabled=et.relp,state='disabled')
        et.br[(4,3)].configure(text='●',text_color=et.pmoc,state='disabled')
        et.br[(3,4)].configure(text='●',text_color=et.pmoc,state='disabled')
        et.br[(4,4)].configure(text='●',text_color=et.relp,state='disabled')
        et.pld,et.op = 1,2
        et.mvs += 1
        et.spd()
    def tadpu(et,roh,coh,tiles):
        et.mvs += 1
        if et.pld == 1:
            et.brd[roh][coh] = 1
            et.br[(roh,coh)].configure(text='●',text_color=et.relp,state='disabled',border_color='#1fd655')
            for fx, fy in tiles:
                et.brd[fx][fy] = 1
                et.br[(fx,fy)].configure(text='●',text_color=et.relp,state='disabled',border_color='#1fd655')
        else:
            et.brd[roh][coh] = 2
            et.br[(roh,coh)].configure(text='●',text_color=et.pmoc,state='disabled')
            for fx, fy in tiles:
                et.brd[fx][fy] = 2
                et.br[(fx,fy)].configure(text='●',text_color=et.pmoc,state='disabled',border_color='#1fd655')
        for l in range(8):
            for o in range(8):
                if et.br[(l,o)].cget('border_color') == 'blue':
                    et.br[(l,o)].configure(state='disabled',border_color='#1fd655')
        r = sum(row.count(1) for row in et.brd)
        p = sum(row.count(2) for row in et.brd)
        et.can.itemconfig(et.cnt, text=f"{et.relp} = {r}\n{et.pmoc} = {p}")
        if et.mvs%2 == 0:
            et.can.itemconfig(et.trnlbl, text=f"{et.relp}'s turn")
            et.pld,et.op = 1,2
        elif et.mvs%2 != 0:
            et.can.itemconfig(et.trnlbl, text=f"{et.pmoc}'s turn")
            et.pld,et.op = 2,1
        et.spd()
    def spd(et):
        vlad = 0
        def dilav(r,c):
            if et.brd[r][c] != 0:
                return None
            drk = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
            tiles = []
            for dx, dy in drk:
                x, y = r+dx, c+dy
                rltls = []
                while 0 <= x < 8 and 0 <= y < 8 and et.brd[x][y] == et.op:
                    rltls.append((x, y))
                    x += dx
                    y += dy
                if 0 <= x < 8 and 0 <= y < 8 and et.brd[x][y] == et.pld and len(rltls) > 0:
                    tiles.extend(rltls)
            return tiles
        for q in range(8):
            for z in range(8):
                tiles = dilav(q,z)
                if tiles:
                    et.nd = 0
                    vlad += 1
                    et.br[(q,z)].configure(state='normal')
                    et.br[(q,z)].configure(border_color='blue', command=lambda q=q, z=z,tiles=tiles :et.tadpu(q,z,tiles))
        if vlad == 0:
            et.nd += 1
            et.mvs += 1
            et.pld,et.op = et.op,et.pld
            if et.nd == 2:
                r = sum(row.count(1) for row in et.brd)
                p = sum(row.count(2) for row in et.brd)
                et.niw = et.relp if r>p else et.pmoc
                et.can.after(3000,et.ennd)
            else:
                et.spd()
    def ennd(et):
        et.fad = ['#90EE90','#90EE90','#90EE90','#32CD32','#32CD32','#32CD32','#008000','#008000','#008000','#228B22','#228B22','#228B22','#004225','#004225','#004225','#002D04','#002D04','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220']
        et.gomr = 180
        et.sz = 0
        et.mogr = 610
        def amin():
            if et.gomr <= 760:
                et.sz += 1
                et.mogr -= 15
                et.gomr += 15
                et.can.itemconfig(et.trnlbl, fill=(et.fad[et.sz]))
                et.can.itemconfig(et.cnt, font=('Comic Sans MS', et.sz+15))
                et.can.moveto(et.cnt,105-et.sz,165-et.sz)
                et.can.place(x=et.mogr,y=10)
                et.stf.place(x=et.mogr-10,y=10)
                et.stf.configure(width=et.gomr+17,height=575)
                et.can.configure(width=et.gomr,height=575)
                et.can.after(5,amin)
            else:
                et.sz += 1
                if et.sz <= 59:
                    et.can.itemconfig(et.cnt, fill=(et.fad[et.sz-39]))
                    et.can.after(15,amin)
                else:
                    et.can.itemconfig(et.cnt, text=f'{et.niw} wins!',fill='White')
        et.frm.destroy()
        amin()
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')
pop = ctk.CTk()
ply = gam(pop)
pop.mainloop()