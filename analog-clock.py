# importing tkinter module
from tkinter import *
from datetime import datetime
import math
# importing date to retrieve 
# today's date and time
from datetime import datetime

# creating tkinter window
root = Tk()
#Adjust size
root.geometry("180x180")
#Give it a title
root.title('Analog Clock')

#Add image file
bg = PhotoImage(file="./assets/watch-bg.png")

#Show image file
label1 = Label(root,image=bg)
label1.place(x=0, y=0) 

# Create a canvas widget
canvas=Canvas(root, width=180, height=180)
canvas.pack(fill = "both", expand = True)
canvas.create_image( 0, 0, image = bg, anchor = "nw")

#update_time method
def update_time():
    now=datetime.now()
    hours=now.hour
    minutes=now.minute
    seconds=now.second

    hours_angle=hours*30+minutes*0.5
    minutes_angle=minutes*6+seconds*0.1
    seconds_angle=seconds*6

    canvas.coords(h_hand,90,90,90+r_hours*math.sin(math.radians(hours_angle)),90-r_hours*math.cos(math.radians(hours_angle)))
    canvas.coords(m_hand,90,90,90+r_minutes*math.sin(math.radians(minutes_angle)),90-r_minutes*math.cos(math.radians(minutes_angle)))
    canvas.coords(s_hand,90,90,90+r_seconds*math.sin(math.radians(seconds_angle)),90-r_seconds*math.cos(math.radians(seconds_angle)))
    
    root.after(1000,update_time)


r_hours=40
r_minutes=70
r_seconds=70 

# Add a hour hand in canvas widget
h_hand = canvas.create_line(90,90,90,90-r_hours, fill="black", width=2)
# Add a minute hand in canvas widget
m_hand = canvas.create_line(90,90,90,90-r_minutes, fill="black", width=2)
# Add a second hand in canvas widget
s_hand = canvas.create_line(90,90,90,90-r_seconds, fill="red", width=1)
    
update_time()

root.mainloop()