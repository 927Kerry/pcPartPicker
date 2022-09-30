import tkinter as tk
import tkMessageBox
import pcPartPickerLinks


#initialize app 
root = tk.Tk()
root.title("pcPartPicker")

#where to put the app window on launch
x = root.winfo_screenwidth() //2
y = int(root.winfo_screenheight() *0.1)
root.geometry("500x600+" +str(x) + '+' + str(y))

frame1 = tk.Frame(root, width=800, height=1000, bg="#CCDBEE")
frame1.grid(row=9, column=0)


#title


#price slider in £250 intervals 


#selection button for intel or amd cpu 


#selection button for nvidia or amd gpu


#button to generate pcpartpickerlist link 


#popup to show link to partpicker link 




root.mainloop()