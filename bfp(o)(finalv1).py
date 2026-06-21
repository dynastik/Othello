#othello game with cheezy graphics(animations), zero readability code, but kinda smart logic, and et=self
import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image, ImageSequence
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
        et.y = ''
        et.lodng = None 
        et.skplbl = et.can.create_text(90, 200, text='', fill="White", font=('Comic Sans MS', 10))

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

        et.loading_anim_id = None
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
                et.bt = ctk.CTkButton(et.frm,width=70,height=70,text='',border_spacing=0,fg_color='green',state='disabled',border_width=2,border_color='#1fd655',font=('Arial',50),bg_color='green')
                et.bt.grid(row=r, column=s, padx=2, pady=2)
                et.br[(r, s)] = et.bt
        et.brd[3][3] = 1
        et.brd[4][3] = 2
        et.brd[3][4] = 2
        et.brd[4][4] = 1                    
        et.br[(3,3)].configure(text='●',text_color_disabled=et.relp,state='disabled')
        et.br[(4,3)].configure(text='●',text_color_disabled=et.pmoc,state='disabled')
        et.br[(3,4)].configure(text='●',text_color_disabled=et.pmoc,state='disabled')
        et.br[(4,4)].configure(text='●',text_color_disabled=et.relp,state='disabled')
        et.pld,et.op = 1,2
        et.mvs += 1
        et.spd()
    def show_loading(et,spt):
        if spt:
            if et.lodng is not None and et.lodng.winfo_exists():  
                et.lodng.destroy()
            et.lodng = ctk.CTkLabel(et.can,text='Computer moving...',text_color='White',font=('Comic Sans MS',10))
            et.lodng.place(x=10,y=300)
            et.gif = Image.open("pie/bfp(o)/loadingif.gif")
            et.gif.seek(0)
            et.loading_frames = [CTkImage(light_image=frame.copy().convert("RGBA").resize((50, 50)), size=(50, 50)) for frame in ImageSequence.Iterator(et.gif)]
            et.loading_label = ctk.CTkLabel(et.can, text="")
            et.loading_label.place(x=50, y=250)
            def animate(idx=0):
                if hasattr(et, "loading_frames") and et.loading_frames:
                    if hasattr(et, "loading_label") and et.loading_label.winfo_exists():
                        et.loading_label.configure(image=et.loading_frames[idx])
                        et.loading_anim_id = et.wnd.after(100, animate, (idx + 1) % len(et.loading_frames))
            animate()
        else:
            if hasattr(et, "loading_anim_id") and et.loading_anim_id is not None:
                et.wnd.after_cancel(et.loading_anim_id)
                et.loading_anim_id = None
            if hasattr(et, "loading_label") and et.loading_label.winfo_exists():
                et.loading_label.destroy()
            if et.lodng is not None and et.lodng.winfo_exists():
                try:
                    et.lodng.configure(text='')
                except Exception:
                    pass
    def tadpu(et,roh,coh,tiles):
        et.y = ''
        movr = et.pld  
        et.mvs += 1
        et.nd = 0  
        basegrad = ["#ffffff","#bbbbbb","#bbbbbb","#535252","#333333","#1F1F1F","#0E0E0E","#000000"]
        def gradan(gr,fx,fy,clr):
            gradd = basegrad if clr == 'Black' else list(reversed(basegrad))
            if gr == 7:
                et.br[(fx,fy)].configure(text='●',text_color_disabled=clr,state='disabled')
                return
            et.br[(fx,fy)].configure(text='●',text_color=gradd[gr],state='normal')
            gr += 1
            et.can.after(100, lambda: gradan(gr,fx,fy,clr))
        if et.pld == 1:
            et.brd[roh][coh] = 1
            for fx,fy in tiles: et.brd[fx][fy] = 1
            et.br[(roh,coh)].configure(text='●',text_color_disabled=et.relp,state='disabled',border_color='#1fd655')
            def vowow(tih):
                if tih >= len(tiles):
                    for (til,wil) in tiles:
                        et.br[(til,wil)].configure(text='●',text_color_disabled=et.relp,state='disabled',border_color='#1fd655')
                    return
                fx,fy = tiles[tih]
                gradan(0, fx, fy, et.relp)
                et.can.after(500, lambda: vowow(tih+1))
            vowow(0)
        else:
            et.brd[roh][coh] = 2
            for fx,fy in tiles:
                et.brd[fx][fy] = 2
                et.br[(fx,fy)].configure(state='normal',border_color="#d61f1f",text_color=et.relp)
            et.br[(roh,coh)].configure(state='normal')
            def vowow(tih):
                if tih >= len(tiles):
                    return
                fx,fy = tiles[tih]
                gradan(0, fx, fy, et.pmoc)
                et.can.after(500, lambda: vowow(tih+1))
            vowow(0)
        def blnk(brbr):
            et.br[(roh,coh)].configure(state='normal')
            if brbr>=20:
                for (til,wil) in tiles:
                        et.br[(til,wil)].configure(text='●',text_color_disabled=et.pmoc,state='disabled',border_color='#1fd655')
                et.br[(roh,coh)].configure(text='●',state='disabled',border_color='#1fd655',text_color_disabled=et.pmoc)
                return
            color = et.pmoc if brbr%2 == 0 else 'green'
            et.br[(roh,coh)].configure(text='●', text_color=color,border_color='#d61f1f')
            et.can.after(100, lambda: blnk(brbr + 1))
        if (et.pld,et.op) == (2,1):
            et.br[(roh,coh)].configure(state='normal')
            blnk(0)
        r = sum(row.count(1) for row in et.brd)
        p = sum(row.count(2) for row in et.brd)
        et.can.itemconfig(et.cnt, text=f"{et.relp} = {r}\n{et.pmoc} = {p}")
        reds = set(tiles)
        for l in range(8):
            for o in range(8):
                if et.br[(l,o)].cget('state') == 'normal'and (l,o) not in reds:
                    et.br[(l,o)].configure(state='disabled',border_color='#1fd655')
        if movr == 2:
            et.can.itemconfig(et.trnlbl, text=f"{et.relp}'s \n(player's) turn")
            et.y = ''
            et.pld,et.op = 1,2
            et.spd()
        else:  
            et.can.itemconfig(et.trnlbl, text=f"{et.pmoc}'s \n(computer's) turn")
            et.pld,et.op = 2,1
            et.show_loading(True)
            et.can.after(2000,et.rtpmc)
    def dilav(et,r,c):
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
    def spd(et):
        for q in range(8):
            for z in range(8):
                et.br[(q,z)].configure(command=lambda: None)
        mves = []
        vlad = False
        for q in range(8):
            for z in range(8):
                tiles = et.dilav(q,z)
                if tiles:
                    vlad = True
                    if et.y == 'cump':
                        mves.append((q,z))
                    else:
                        et.nd = 0
                        et.br[(q,z)].configure(state='normal', border_color="Blue")
                        if et.pld == 1:
                            et.br[(q,z)].configure(command=lambda q=q, z=z,tiles=tiles :et.tadpu(q,z,tiles))
        if et.y == 'cump':
            return mves
        if vlad == False:
            et.nd += 1
            et.mvs += 1
            et.pld,et.op = et.op,et.pld
            if et.nd == 2:
                r = sum(row.count(1) for row in et.brd)
                p = sum(row.count(2) for row in et.brd)
                if r > p:
                    et.niw = et.relp
                elif p > r:
                    et.niw = et.pmoc
                else:
                    et.niw = 'Tie'
                et.can.after(3000,et.ennd)
            else:
                if et.pld == 2:
                    et.lodng.configure(text='Your turn was skipped...')
                    et.can.itemconfig(et.trnlbl, text=f"{et.pmoc}'s \n(computer's) turn")
                    et.can.after(3000,et.rtpmc)
                else:
                    et.spd()
    def ennd(et):
        et.fad = ['#90EE90','#90EE90','#90EE90','#32CD32','#32CD32','#32CD32','#008000','#008000','#008000','#228B22','#228B22','#228B22','#004225','#004225','#004225','#002D04','#002D04','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220','#013220']
        et.gomr = 180
        et.sz = 0
        et.mogr = 610
        def amin():
            if not et.wnd.winfo_exists():
                return
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
                    win_text = f'{et.niw} wins!' if et.niw != 'Tie' else "It's a tie!"
                    et.can.itemconfig(et.cnt, text=win_text, fill='White')
        def myav():
            for widget in et.wnd.winfo_children():
                widget.destroy()
            gam(et.wnd)
        et.restrt = ctk.CTkButton(et.can,text='Restart',text_color='White',fg_color='#089383',command=myav,width=90,height=30,font=('Comic Sans MS',20,'bold'))
        et.restrt.place(x=10,y=10)
        et.frm.destroy()
        amin()
    def rtpmc(et):
        et.y = 'cump'
        vlaidmves = et.spd()
        et.nebors = {(0, 0): [(0, 1), (1, 0), (1, 1)],(0, 7): [(0, 6), (1, 7), (1, 6)],(7, 0): [(6, 0), (7, 1), (6, 1)],(7, 7): [(6, 7), (7, 6), (6, 6)]}
        def crnoer(pos):
            return pos in [(0, 0), (0, 7), (7, 0), (7, 7)]
        def edj(poj):
            return poj in [(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6)]
        et.bstmv = {}
        for vr, vc in vlaidmves:
            rwrd = 0
            tiles = et.dilav(vr, vc)
            if crnoer((vr, vc)):
                rwrd += 50
            else:
                for corner, neighbors in et.nebors.items():
                    if (vr, vc) in neighbors:
                        rwrd -= 25 
            for c,d in tiles:
                if edj((c,d)):
                    rwrd+=6
            if edj((vr, vc)):
                rwrd += 6
            rwrd += len(tiles)
            et.bstmv[(vr, vc)] = rwrd
        if not et.bstmv:
            et.nd += 1
            et.mvs += 1
            et.pld,et.op = et.op,et.pld
            if et.nd == 2:
                r = sum(row.count(1) for row in et.brd)
                p = sum(row.count(2) for row in et.brd)
                if r > p:
                    et.niw = et.relp
                elif p > r:
                    et.niw = et.pmoc
                else:
                    et.niw = 'Tie'
                et.can.after(3000,et.ennd)
            else:
                et.y = ''
                et.show_loading(False)
                et.can.itemconfig(et.skplbl, text="Computer's turn\nwas skipped!")
                et.can.after(2000, lambda: et.can.itemconfig(et.skplbl, text=''))
                et.spd()
            return
        else:
            (roh, coh) = max(et.bstmv, key=et.bstmv.get)
            et.pld, et.op = 2, 1
            tiles = et.dilav(roh, coh)  
            et.tadpu(roh, coh, tiles)
        et.y = ''
        et.show_loading(False)
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')
pop = ctk.CTk()
ply = gam(pop)
pop.mainloop()