import tkinter as tk
window = tk . Tk()
window. title("GradePro - Smart Student Grade Calculator")
window.geometry("500x650")
window.configure(bg="#E6E6FA")
                  
lable = tk.Label(window,
 text = "Student Marks Calculator" , font=("Arial" , 20, "bold"), fg="#C2185B").pack(pady=15)



math_label = tk.Label(window,
text = "Math Marks" , font=("Arial" , 12, "bold"))
math_label.pack()

math_entry = tk.Entry(window, width=20)
math_entry.pack()



english_label = tk.Label(window,
text = "English Marks" , font=("Arial" , 12, "bold")) 
english_label.pack() 

english_entry = tk.Entry(window, width=20)
english_entry.pack()


computer_label = tk.Label(window,
text = "Computer Marks" , font=("Arial", 12, "bold"))
computer_label.pack()  

computer_entry = tk.Entry(window, width=20)
computer_entry.pack()

islamiat_label = tk.Label(window,
 text= "Islamiat Marks" , font=("Arial", 12, "bold"))
islamiat_label.pack()

islamiat_entry = tk.Entry(window, width=20)
islamiat_entry.pack()

pak_label = tk.Label(window,
 text="Pak Studies Marks" , font=("Arial", 12, "bold"))
pak_label.pack()

pak_entry = tk.Entry(window, width=20)
pak_entry.pack()

urdu_label = tk.Label(window,
text="Urdu Marks" , font=("Arial" , 12, "bold")) 
urdu_label.pack()

urdu_entry = tk.Entry(window, width=20)
urdu_entry.pack()

physics_label = tk.Label(window,
text="Physics Marks" , font=("Arial", 12, "bold"))
physics_label.pack()

physics_entry = tk.Entry(window, width=20)
physics_entry.pack()

result_label = tk.Label(window,
text="" , font=("Arial", 12, "bold"))
result_label.pack()                        

def calculate():                            
    math = int(math_entry.get()) 
    english = int(english_entry.get())
    computer = int(computer_entry.get())
    islamiat  = int(islamiat_entry.get())
    pak = int(pak_entry.get())
    urdu = int(urdu_entry.get())
    physics = int(physics_entry.get())
    total = math + english + computer + islamiat + pak + urdu + physics  
    average = total/7
    percentage = (total / 550) * 100
    if percentage >= 80:
        grade = "A+"
    elif percentage >= 70:
          grade = "A"
    elif percentage >= 60:
         grade = "B"
    elif percentage >= 50:
         grade = "C"
    else:
         grade = "F"

    result_label.config(text=f"Total:{total}\nPercentage:{percentage:.2f}%\nAverage:.f:{average}\nGrade:{grade}")


     
calculate_button = tk.Button(window,
text="Calculate",
command=calculate, bg="blue" , fg="white", font=("Arial", 12, "bold"), width=15)
calculate_button.pack()
def clear():
        math_entry.delete(0, tk.END)
        english_entry.delete(0, tk.END)
        computer_entry.delete(0, tk.END)
        islamiat_entry.delete(0, tk.END)
        pak_entry.delete(0, tk.END)
        urdu_entry.delete(0, tk.END)
        physics_entry.delete(0, tk.END)
        result_label.config(text="")




clear_button = tk.Button(window,
text="Clear", command=clear,bg="red", fg="white", font=("Arial", 12, "bold"), width=15)
clear_button.pack(pady=10)
 
window.mainloop()  
     



