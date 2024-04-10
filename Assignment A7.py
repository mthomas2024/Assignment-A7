#Mason Thomas
#GUI Dev
#Assignment A7
#4/9/2024

import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

#Goobal holders
imageFile = None

#Create Window
root = Tk()
root.title("Smart Home Application")
root.geometry("750x600")

#Display Instructions
title = Label(text = "Smart Home\nElectric Savings")
title.place(relx=.8, rely=.1, anchor=CENTER)

#Picture Frame
pic = ttk.Frame(root, width=400,height=300)
pic.place(relx=.3, rely=.2, anchor=CENTER)
pic.configure(borderwidth="2")
pic.configure(relief="groove")
        
class SavingsApp:
    def __init__(self, root):
        global imageFile
        
        imageFile = "smarthome.jpg"

        frame = pic
        img = Image.open(imageFile)
        photo = ImageTk.PhotoImage(img.resize((400,300)))
        lblImage = ttk.Label(frame, image = photo)
        lblImage.image = photo
        lblImage.place(relx=.5,rely=.5,anchor=CENTER)
        
        self.months = []
        self.savings = []
        self.load_data()

        self.selected_month = tk.StringVar()
        self.selected_month.set("Select a month")
        
        self.combo_months = ttk.Combobox(root, values=self.months, textvariable=self.selected_month)
        self.combo_months.place(relx=.8, rely=.3, anchor=CENTER)
        self.combo_months.bind("<<ComboboxSelected>>", self.update_month_label)
        
        self.label_savings = tk.Label(root, text="")
        self.label_savings.place(relx=.5, rely=.6, anchor=CENTER)
        
        self.display_button = tk.Button(root, text="Display Statistics", command=self.display_statistics)
        self.display_button.place(relx=.5, rely=.7, anchor=CENTER)
        
        self.label_average = tk.Label(root, text="")
        self.label_average.place(relx=.5, rely=.8, anchor=CENTER)
        
        self.label_max_savings = tk.Label(root, text="")
        self.label_max_savings.place(relx=.5, rely=.9, anchor=CENTER)
    
    def load_data(self):
        try:
            with open("savings.txt", "r") as file:
                lines = file.readlines()
                for i in range(0, len(lines), 2):
                    month = lines[i].strip()
                    saving = lines[i+1].strip()
                    self.months.append(month)
                    self.savings.append(float((saving)))
        except FileNotFoundError:
            print("File not found.")
    
    def update_month_label(self, event):
        selected_index = self.months.index(self.selected_month.get())
        savings_value = self.savings[selected_index]
        self.label_savings.config(text=f"The electric savings for {self.selected_month.get()}: ${savings_value:.2f}")
    
    def display_statistics(self):
        average_savings = sum(self.savings) / len(self.savings)
        max_savings_index = self.savings.index(max(self.savings))
        max_savings_month = self.months[max_savings_index]
        
        self.label_average.config(text=f"The average monthly savings: ${average_savings:.2f}")
        self.label_max_savings.config(text=f"{max_savings_month} had the most significant monthly savings") 


app = SavingsApp(root)
root.mainloop()


