from tkinter import * 
import speedtest

#SET WINDOW Properties
window = Tk()
window.geometry('360x600')
window.resizable(False,False)

window.configure(bg='#1a212d')
window.title('NetVelocity')

# ADD ICON
win_icon = PhotoImage(file='images/logo.png')
window.iconphoto(False,win_icon)

# ADD GRAPHICS
top_bar = PhotoImage(file='images/topbar.png')
Label(window,image=top_bar,bg='#1a212d').pack()

speed_ring = PhotoImage(file='images/ring.png')
Label(window,image=speed_ring,bg='#1a212d').pack(pady=(40,0))

start_button = PhotoImage(file="images/button.png")
start = Button(window,image=start_button,bg='#1a212d',bd=0,activebackground='#1a212d', cursor='hand2')
start.pack(pady=10)

# ADD OUTPUT LABEL

#TOP BAR LABELS
Label(window,text='PING',font='arial 10 bold',bg='#384056').place(x=50,y=0)         #PING      top left
Label(window,text='DOWNLOAD',font='arial 10 bold',bg='#384056').place(x=140,y=0)    #DOWNLOAD  top middle
Label(window,text='UPLOAD',font='arial 10 bold',bg='#384056').place(x=260,y=0)      #UPLOAD    top right

Label(window,text='MS',font='arial 7 bold',bg='#384056',fg='white').place(x=63,y=80)             # MS      top left
Label(window,text='MBPS',font='arial 7 bold',bg='#384056',fg='white').place(x=165+2,y=80)        # MBPS 1  top middle
Label(window,text='MBPS',font='arial 7 bold',bg='#384056',fg='white').place(x=275+2,y=80)        # MBPS 2  top right

#DOWNLOAD LABEL (in middle)
Label(window,text='Download',font='arial 15 bold',bg='#384056',fg='white').place(x=140-3,y=280)  # Download   top circle
Label(window,text='MBPS',font='arial 15 bold',bg='#384056',fg='white').place(x=155,y=380)        # MBPS 3     bottom circle



window.mainloop()