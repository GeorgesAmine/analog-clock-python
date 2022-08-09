# importing tkinter module
from tkinter import *
# importing datetime module
from datetime import datetime
# importing math module to perfom calculations
import math
# importing PIL to handle images
from PIL import Image

# creating tkinter window called root
root = Tk()
# give the window a title
root.title('Analog Clock')

# select image file
bg_filename="./assets/watch-bg2.png"
# get image size
with Image.open(bg_filename) as img:
    w = img.size[0]
    h = img.size[1]

# adjust size of window
root.geometry(str(w)+"x"+str(h))
bg = PhotoImage(file=bg_filename)


# create a canvas widget and image as background
canvas=Canvas(root, width=w, height=h)
canvas.pack(fill = "both", expand = True)
canvas.create_image( 0, 0, image = bg, anchor = "nw")

#update_time method
def update_time():
    # get time now
    now=datetime.now()
    # extract hours, minutes and seconds
    hours=now.hour
    minutes=now.minute
    seconds=now.second

    # convert to angles and the clock
    hours_angle=hours*30+minutes*0.5
    minutes_angle=minutes*6+seconds*0.1
    seconds_angle=seconds*6

    # updates hands coords to match the calculated angles
    canvas.coords(h_hand,center_x,center_y,center_x+r_hours*math.sin(math.radians(hours_angle)),center_y-r_hours*math.cos(math.radians(hours_angle)))
    canvas.coords(m_hand,center_x,center_y,center_x+r_minutes*math.sin(math.radians(minutes_angle)),center_y-r_minutes*math.cos(math.radians(minutes_angle)))
    canvas.coords(s_hand,center_x,center_y,center_x+r_seconds*math.sin(math.radians(seconds_angle)),center_y-r_seconds*math.cos(math.radians(seconds_angle)))
    
    # update time every 1000ms (1s)
    root.after(1000,update_time)

# set length of hands
r_hours=0.2*h
r_minutes=0.3*h
r_seconds=0.3*h

#Setting image center
center_x=w/2
center_y=h/2

# add a hour hand in canvas widget
h_hand = canvas.create_line(center_x,center_y,center_x,center_y-r_hours, fill="black", width=4)
# add a minute hand in canvas widget
m_hand = canvas.create_line(center_x,center_y,center_x,center_y-r_minutes, fill="black", width=4)
# add a second hand in canvas widget
s_hand = canvas.create_line(center_x,center_y,center_x,center_y-r_seconds, fill="red", width=2)

# call update_time method    
update_time()

#call the mainloop for tkinter window
root.mainloop()