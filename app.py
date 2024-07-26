import tkinter as tk
import time

def time_update():
    current_time = time.strftime('%H:%M:%S')
    clock_label['text'] = current_time
    root.after(1000, time_update)

root = tk.Tk()
root.title('Digital Clock')

clock_label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
clock_label.pack(anchor='center')

time_update()
root.mainloop()
