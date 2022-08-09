# importing tkinter module
from tkinter import *
# importing datetime module
from datetime import datetime
# importing math module to perfom calculations
import math

# creating tkinter window called root
root = Tk()
# adjust size of window
root.geometry("180x180")
# give the window a title
root.title('Analog Clock')

# add image file
bg = PhotoImage(file="./assets/watch-bg.png")

# create a canvas widget and image as background
canvas=Canvas(root, width=180, height=180)
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
    canvas.coords(h_hand,90,90,90+r_hours*math.sin(math.radians(hours_angle)),90-r_hours*math.cos(math.radians(hours_angle)))
    canvas.coords(m_hand,90,90,90+r_minutes*math.sin(math.radians(minutes_angle)),90-r_minutes*math.cos(math.radians(minutes_angle)))
    canvas.coords(s_hand,90,90,90+r_seconds*math.sin(math.radians(seconds_angle)),90-r_seconds*math.cos(math.radians(seconds_angle)))
    
    # update time every 1000ms (1s)
    root.after(1000,update_time)

# set length of hands
r_hours=40
r_minutes=70
r_seconds=70 

# add a hour hand in canvas widget
h_hand = canvas.create_line(90,90,90,90-r_hours, fill="black", width=2)
# add a minute hand in canvas widget
m_hand = canvas.create_line(90,90,90,90-r_minutes, fill="black", width=2)
# add a second hand in canvas widget
s_hand = canvas.create_line(90,90,90,90-r_seconds, fill="red", width=1)

# call update_time method    
update_time()

#call the mainloop for tkinter window
root.mainloop()