from tkinter import * 
import speedtest

def test():
   
    UP = round(speedtest.Speedtest().upload()/(1024*1024),2)
    upload_speed.config(text=UP)
    print(UP)
    
    DOWN = round(speedtest.Speedtest().download()/(1024*1024))
    download_speed.config(text=DOWN)
    Download_speed.config(text=DOWN)
    print(DOWN)
    
    servernames = []
    speedtest.Speedtest().get_servers(servernames)
    Latency = speedtest.Speedtest().results.ping
    latency.config(text=Latency)


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
start = Button(window,image=start_button,bg='#1a212d',bd=0,activebackground='#1a212d', cursor='hand2',command=test)
start.pack(pady=10)

# ADD OUTPUT LABEL

#TOP BAR LABELS
Label(window,text='PING',font='arial 10 bold',bg='#384056').place(x=50,y=0)         #PING      top left
Label(window,text='DOWNLOAD',font='arial 10 bold',bg='#384056').place(x=140,y=0)    #DOWNLOAD  top middle
Label(window,text='UPLOAD',font='arial 10 bold',bg='#384056').place(x=260,y=0)      #UPLOAD    top right

Label(window,text='MS',font='arial 7 bold',bg='#384056',fg='white').place(x=63,y=80)             # MS      top left
Label(window,text='Mbps',font='arial 7 bold',bg='#384056',fg='white').place(x=165+2,y=80)        # Mbps 1  top middle
Label(window,text='Mbps',font='arial 7 bold',bg='#384056',fg='white').place(x=275+2,y=80)        # Mbps 2  top right

#DOWNLOAD LABEL (in middle)
Label(window,text='Download',font='arial 15 bold',bg='#384056',fg='white').place(x=140-3,y=280)         # Download    top circle
Label(window,text='Mbps',font='arial 15 bold',bg='#384056',fg='white').place(x=155,y=380)               # Mbps 3      bottom circle

Download_speed= Label(window,text='00',font='arial 40 bold',bg='#384056',fg='white')                    # Main speed  middle circle
Download_speed.place(x=185,y=380,anchor='center')
# TOP VARIABLE VALUES

latency = Label( window,text='00',font='arial 13 bold',bg='#384056',fg='white')
latency.place(x=70+2,y=60,anchor='center')

download_speed = Label( window,text='00',font='arial 13 bold',bg='#384056',fg='white')
download_speed.place(x=180+2,y=60,anchor='center')

upload_speed = Label( window,text='00',font='arial 13 bold',bg='#384056',fg='white')
upload_speed.place(x=290+3,y=60,anchor='center')

window.mainloop()