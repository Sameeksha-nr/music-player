import pygame
from pygame import mixer
from tkinter import *
from tkinter import filedialog

#Variables and Initialiser
pygame.mixer.init()
current_volume = 0.5

#Functions
def select_song():
    filename= filedialog.askopenfilename(initialdir= "C:/")
    song= filename
    current_song= filename.split("/")
    current_song= current_song[-1]

    try:
        
        mixer.music.load(song)
        mixer.music.set_volume(current_volume)
        mixer.music.play()
        song_title.config(text= str(current_song))
        volume_label.config(text= str(current_volume))
       
        
    except Exception as e:
        print(e)
        song_title.config(text= "Error playing song, choose another file")

def increase_volume():
    global current_volume;
    try:
        if current_volume >=5:
            volume_label.config(text= "Max")
            return
        current_volume = current_volume + 0.2
        mixer.music.set_volume(current_volume)
        current_volume= round(current_volume, 1)
        volume_label.config(text= str(current_volume))
    except Exception as e:
        print(e)
        song_title.config(text= "Please Select a Song")

def decrease_volume():
    global current_volume;
    try:
        if current_volume <=0:
            volume_label.config(text= "Mute")
            return    
        current_volume = current_volume - 0.2
        current_volume= round(current_volume, 1)
        mixer.music.set_volume(current_volume)
        volume_label.config(text= str(current_volume))
    except Exception as e:
        print(e)
        song_title.config(text= "Please Select a Song")


def pause_song():
   try:
      mixer.music.pause()      
   except Exception as e:
       print(e)
       song_title.config(text= "Please Select a Song")

def play_song():
    try:
        mixer.music.unpause()
    except Exception as e:
        print(e)
        song_title.config(text= "Please Select a Song")

#Screen setup
        
screen = Tk()
screen.title("Music Player")
screen.geometry("1000x300")
screen.configure(bg='#856ff8')


#Frames and Labels

display_frame= Frame(screen, bg='#856ff8')
display_frame.pack()
Label(display_frame, text= "Music Player!!!", font=("Helvetica", 40, "italic"), fg= "purple", bg='#856ff8').grid(sticky= "N")
song_title= Label(display_frame, font= ("Times New Roman", 20), bg='#856ff8')
song_title.grid(row = 10)

frame= Frame(screen, bg='#856ff8')
frame.pack(side = BOTTOM)
volume_label= Label(frame, text= "Volume: ", bg= '#856ff8')
volume_label.grid(row=1, column= 3)

        
#Images for buttons

play_img = PhotoImage(file= 'playbutton.png')
play_img = play_img.subsample(3, 3)
pause_img = PhotoImage(file= 'pausebutton.png')
pause_img = pause_img.subsample(3, 3)
volume_up_img = PhotoImage(file= 'Volume_UP.png')
volume_up_img = volume_up_img.subsample(3, 3)
volume_down_img = PhotoImage(file= 'Volume_down.png')
volume_down_img = volume_down_img.subsample(3, 3)


#Buttons

fileselect= Button(display_frame, text= "Select a Song to Play", command= select_song, font= ("Sans Serif", 15), bg="black", fg= "white", activebackground= "white", activeforeground= "black").grid(padx= 5)
play_button = Button(frame, image= play_img, command= play_song ,borderwidth = 0, bg='#856ff8')
pause_button = Button(frame, image= pause_img, command= pause_song, borderwidth = 0, bg='#856ff8')
volume_up_button = Button(frame, image= volume_up_img,command= increase_volume, borderwidth = 0, bg='#856ff8')
volume_down_button = Button(frame, image= volume_down_img, command= decrease_volume, borderwidth = 0, bg='#856ff8')
play_button.grid(row=0, column= 4)
pause_button.grid(row=0, column= 2)
volume_down_button.grid(row=1, column= 0)
volume_up_button.grid(row=1, column= 5)

screen.mainloop()
