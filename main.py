from tkinter import *
import math
root = Tk()
root.configure(background="black")
root.title("SIMPLE CALCULATOR")
root.resizable(0,0)
root.geometry("410x450")
def btn_click(item):
    global expression
    expression += str(item)
    display.set(expression)

def btn_clear():
        global expression
        expression = ""
        display.set(" ")

def btn_equal():
            global expression
            result = str(eval(expression))
            display.set(result)
            expression = " "
expression = ""
display = StringVar()
entry_frame = Frame(root,width=234,height=49,bd=0, highlightbackground="black",highlightcolor="black",highlightthickness =2)
entry_frame.pack(side=TOP, expand=YES, fill=X)
btn_entry = Entry(entry_frame,relief=SUNKEN,justify="right",bg="grey",bd=30,font=('arial',18,'bold'),textvariable=display).pack(side=TOP,ipadx=300,ipady=17)

button_frame= Frame(root,bg="black")
button_frame.pack(ipady=200,ipadx=200)

btn_C = Button(button_frame,text="C",bg="white",fg="black",height=1,width=8,relief='sunken',command=lambda: btn_clear()).grid(row=0,column=0,ipady=20,ipadx=20)
btn_Divide = Button(button_frame,text="/",bg="white",fg="black",height=1,width=8,relief='sunken',command=lambda: btn_click("/")).grid(row=0,column=1,ipady=20,ipadx=20)
btn_mul = Button(button_frame,text="*",bg="white",fg="black",height=1,width=8,relief='sunken',command=lambda: btn_click("*")).grid(row=0,column=2,ipady=20,ipadx=20)
btn_square = Button(button_frame,text="^2",bg="white",fg="black",height=1,width=8,relief='sunken',command=lambda: btn_click("**2")).grid(row=0,column=3,ipady=20,ipadx=20)


btn_seven = Button(button_frame,text="7",bg="white",fg="red",height=1,width=8,relief= 'sunken',command=lambda: btn_click(7)).grid(row=1,column=0,ipady=20,ipadx=20)
btn_eight = Button(button_frame,text="8",bg="white",fg="red",height=1,width=8,relief= 'sunken',command=lambda: btn_click(8)).grid(row=1,column=1,ipady=20,ipadx=20)
btn_nine = Button(button_frame,text="9",bg="white",fg="red",height=1,width=8,relief= 'sunken', command=lambda: btn_click(9)).grid(row=1,column=2,ipady=20, ipadx=20)
btn_minus = Button(button_frame,text="-",bg="white",fg="black",height=1,width=8,relief= 'sunken', command=lambda: btn_click("-")).grid(row=1,column=3,ipady=20,ipadx=20)


btn_four = Button(button_frame,text="4",bg="white",fg="red",height=1,width=8,relief='sunken', command=lambda: btn_click(4)).grid(row=2,column=0,ipady=20, ipadx=20)
btn_five = Button(button_frame,text="5",bg="white",fg="red",height=1,width=8,relief='sunken', command=lambda: btn_click(5)).grid(row=2,column=1,ipady=20, ipadx=20)
btn_six = Button(button_frame,text="6",bg="white",fg="red",height=1,width=8,relief='sunken', command=lambda: btn_click(6)).grid(row=2,column=2,ipady=20,  ipadx=20)
btn_plus = Button(button_frame,text="+",bg="white",fg="black",height=1,width=8,relief='sunken', command=lambda: btn_click("+")).grid(row=2,column=3,ipady=20, ipadx=20)


btn_one = Button(button_frame,text="1",bg="white",fg="red",height=1,width=8,relief='sunken', command=lambda: btn_click(1)).grid(row=3,column=0,ipady=20, ipadx=20)
btn_two = Button(button_frame,text="2",bg="white",fg="red",height=1,width=8,relief='sunken', command=lambda: btn_click(2)).grid(row=3,column=1,ipady=20, ipadx=20)
btn_three = Button(button_frame,text="3",bg="white",fg="red",height=1,width=8,relief='sunken', command=lambda: btn_click(3)).grid(row=3,column=2,ipady=20,ipadx=20)
btn_equals = Button(button_frame,text="=",bg="white",fg="black",height=1,width=8,relief='sunken', command=lambda: btn_equal()).grid(row=3,column=3,ipady=20,ipadx=20)


btn_cube_root = Button(button_frame,text="∛",bg="white",fg="black",height=1,width=8,relief='sunken', command=lambda: btn_click("**(1/3)")).grid(row=4,column=0,ipady=20,ipadx=20)
btn_zero = Button(button_frame,text="0",bg="white",fg="red",height=1,width=8,relief='sunken', command=lambda: btn_click(0)).grid(row=4,column=1,ipady=20,ipadx=20)
btn_dot = Button(button_frame,text=".",bg="white",fg="red",height=1,width=8,relief='sunken', command=lambda: btn_click(".")).grid(row=4,column=2,ipady=20,ipadx=20)
btn_sqrt = Button(button_frame,text="√",bg="white",fg="black",height=1,width=8,relief='sunken', command=lambda:btn_click("**(0.5)")).grid(row=4,column=3,ipady=20,ipadx=20)


root.mainloop()
