
import tkinter as tk
from time import sleep

#from calcMath import user_button

root = tk.Tk()
HEIGHT = 450
WIDTH = 450



line_1 = ""

def user_button(n, equation):
    global line_1
    #store entered button value in a string
    line_1 = line_1 + str(n)

    #puts the equation into a set so the user can see it when inputing a number
    equation.set(line_1)
    
    
#evaluates the equation from the user
def do_math(answer):
    global line_1
    try:
        new_expression = eval(answer)
    except:
        equation.set("Enter a valid expression...")
        
    equation.set(new_expression)

    line_1 = f"{answer}"



def clear_screen(answer):
    global line_1

    line_1 = ""
    equation.set(line_1)





#the equation that the user enters
equation = tk.StringVar() 


#defines the size of the window
canvas = tk.Canvas(height= HEIGHT, width = WIDTH)
canvas.pack()

#border for the entry frame
top_frame = tk.Frame(root, bg = "#66b3ff" ,bd=2)
top_frame.place(relx=0.1,rely=0.1, relwidth=0.8, relheight=0.12)

#screen for the numbers
entry = tk.Entry(top_frame, bg= "#ffffcc", bd = 10,justify="right",textvariable=equation)
entry.place( relwidth=1,relheight=1)

#Blue border under the buttons
bottom_frame = tk.Frame(root, bg="#66b3ff",bd= 5)
bottom_frame.place(relwidth=0.8, relheight=0.6, rely=0.3, relx =0.1)

#white frame under the #buttons
bTop_frame = tk.Frame(bottom_frame, bg="#ffffcc",)
bTop_frame.place(relwidth=0.6, relheight=1)

#white frame under the sign buttons
rTop_frame = tk.Frame(bottom_frame, bg="#ffffcc",)
rTop_frame.place(relwidth=0.3, relheight=1, relx=0.65)



#makes the buttons for the sign

buttonPlus = tk.Button(rTop_frame,text="+",height=2,width=2,command = lambda:user_button("+",equation))
buttonPlus.grid(row=0,column=0)

buttonMinus = tk.Button(rTop_frame,text="-",height=2,width=2,command = lambda:user_button("-",equation))
buttonMinus.grid(row=0,column=1)

buttonDiv= tk.Button(rTop_frame,text="/",height=2,width=2,command = lambda:user_button("/",equation))
buttonDiv.grid(row=1,column=0)

buttonX = tk.Button(rTop_frame,text="x",height=2,width=2,command = lambda:user_button("*",equation))
buttonX.grid(row=1,column=1)

buttonEqu = tk.Button(rTop_frame,text="=",height=2,width=2,command = lambda:do_math(line_1))
buttonEqu.grid(row=2,column=0)

buttonClear = tk.Button(rTop_frame,text="C",height=2,width=2,command = lambda:clear_screen(line_1))
buttonClear.grid(row=2,column=1)


#makes the #keys
button1 = tk.Button(bTop_frame, text="1",height=2,width=3,command=lambda:user_button(1,equation))
button1.grid(row=0, column=0, padx=9, pady=15,)

button2 = tk.Button(bTop_frame, text="2",height=2,width=3,command=lambda:user_button(2,equation))
button2.grid(row=0, column=1, padx=9, pady=10,)

button3 = tk.Button(bTop_frame, text="3",height=2,width=3,command=lambda:user_button(3,equation))
button3.grid(row=0, column=2, padx=9, pady=10,)

button4 = tk.Button(bTop_frame, text="4",height=2,width=3,command=lambda:user_button(4,equation))
button4.grid(row=1, column=0, padx=9, pady=10,)

button5 = tk.Button(bTop_frame, text="5",height=2,width=3,command=lambda:user_button(5,equation))
button5.grid(row=1, column=1, padx=9, pady=10,)

button6 = tk.Button(bTop_frame, text="6",height=2,width=3,command=lambda:user_button(6,equation))
button6.grid(row=1, column=2, padx=9, pady=10,)

button7 = tk.Button(bTop_frame, text="7",height=2,width=3,command=lambda:user_button(7,equation))
button7.grid(row=2,column=0, padx=9, pady=10,)

button8 = tk.Button(bTop_frame, text="8",height=2,width=3,command=lambda:user_button(8,equation))
button8.grid(row=2,column=1, padx=9, pady=10,)

button9 = tk.Button(bTop_frame, text="9",height=2,width=3,command=lambda:user_button(9,equation))
button9.grid(row=2, column=2, padx=9, pady=10,)

button0 = tk.Button(bTop_frame, text="0",height=1,width=2,command=lambda:user_button(0,equation))
button0.grid(row=3, column=1, padx=9, pady=10,)

    




root.mainloop()