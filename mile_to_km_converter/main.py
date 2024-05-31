from tkinter import *
    
    
def main():
    window = Tk()
    window.title("Mile To Kilometer Converter")
    window.minsize(width=500, height=300)
    
    entry = Entry(width=10)
    entry.grid(column=3, row=0)
   
    label1 = Label(text="Miles")
    label1.grid(row=0, column=4)
    label1.config(padx=10, pady=10)
    
    label2 = Label(text='is equal to')
    label2.grid(row=1, column=0)
    
    km_label = Label(text='0')
    km_label.grid(row=1, column=1)
    
    label3 = Label(text='Km')
    label3.grid(row=1, column=3)
    
    def calculate():
        mile_value = float(entry.get())
        km_value = round(mile_value * 1.609)
        km_label.config(text=f'{km_value}')
    
    button = Button(text='Calculate', command=calculate)
    button.grid(row=2, column=3) 
    
    window.mainloop()
    
    
if __name__ == "__main__":
    main()
    
    

