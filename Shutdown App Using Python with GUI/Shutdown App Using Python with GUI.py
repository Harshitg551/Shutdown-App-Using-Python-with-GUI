from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")  # Restart

def restart_time():
    os.system("shutdown /r /t 30")  # Restart with time

def logout():
    os.system("shutdown -l")  # Log out

def shutdown():
    os.system("shutdown /s /t 1")  # Shutdown

st = Tk()
st.title("ShutDown App")  # App title
st.geometry("500x500")    # Size

# Load the background image using the absolute path
bg_image = PhotoImage(file=r"man-7628305_640.png")

# Create a label to display the background image
bg_label = Label(st, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

r_button = Button(st, text="Restart", font=("Times New Roman", 30, "bold"), 
                  relief=RAISED, cursor="plus", command=restart)  # For hovering in 3D, use relief
r_button.place(x=150, y=60, height=50, width=200)

rt_button = Button(st, text="Restart With Time", font=("Times New Roman", 18, "bold"), 
                   relief=RAISED, cursor="plus", command=restart_time)
rt_button.place(x=150, y=170, height=50, width=200)

lg_button = Button(st, text="Log-Out", font=("Times New Roman", 30, "bold"), 
                   relief=RAISED, cursor="plus", command=logout)
lg_button.place(x=150, y=270, height=50, width=200)

st_button = Button(st, text="Shutdown", font=("Times New Roman", 30, "bold"), 
                   relief=RAISED, cursor="plus", command=shutdown)
st_button.place(x=150, y=370, height=50, width=200)

st.mainloop()  # Main loop is for showing the graphic
