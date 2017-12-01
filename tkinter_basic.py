import tkinter as tk
from tkinter import *
import random
import time
import datetime
#import subprocess
import webbrowser
#import tkinter_advance

root = tk.Tk()
root.geometry("1600x8000")
root.title("Tkinter Tutorial")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
root.focus_set()
root.bind("<Escape>", lambda e: e.widget.quit())
#root.overrideredirect(True)
#root.configure(background = "burlywood2")
#=============================================================================================================================================================================================================================================================================================================
#                                                                                  I M A G E
#==============================================================================================================================================================================================================================
logo = PhotoImage(file="logo.gif")
photo=PhotoImage(file="shake.gif")
w1 = Label(root, image=logo).pack(side="top")
w2 = Label(root, 
           justify=RIGHT,
           padx = 10).pack(side="top")
#============================================================================================================================================================================================================================================================================================================
#                                                                   D E S I G N I N G   T H E   T I T L E          
#============================================================================================================================================================================================================================================================================================================
Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=TOP)
f2=Frame(root,width=800,height=700,relief=SUNKEN)
f2.pack(side=BOTTOM)
f3=Frame(root,width=800,height=700,relief=SUNKEN)
f3.pack(side=TOP)

localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('arial',50,'italic'),text="THIS IS TKINTER TUTORIAL",fg="DarkOrange3",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)
#===================================================================================================================================================================================================================================================
#                                                                         T E X T S   F O R   B A S I C 
#===================================================================================================================================================================================================================================================
explanation = """We will start our tutorial with one of the easiest widgets of Tk (Tkinter), i.e. a label. A Label is a Tkinter Widget class, which is used to display text or an image. The label is a widget that the user just views but not interact with. There is hardly any
book or introduction into a programming language, which doesn't start with the "Hello World" example. We will draw on tradition but will slightly modify the output to "Hello Tkinter" instead of "Hello World". The following Python script uses Tkinter to create a window with
the text "Hello Tkinter". You can use the Python interpretor to type this scriptline after line, or you can save it in a file, for example "hello.py":

from Tkinter import *
root = Tk()
w = Label(root, text="Hello Tkinter!")
w.pack()
root.mainloop()"""

explanation1 = """Some Tk widgets, like the label, text, and canvas widget, allow you to specify the fonts used to display text. This can be achieved by setting the attribute "font". typically via a "font" configuration option. You have to consider that fonts are one of several areas that are not platform
-independent.The attribute fg can be used to have the text in another colour and the attribute bg can be used to change the background colour of the label. 
import tkinter as tk

root = tk.Tk()
tk.Label(root, 
		 text="Red Text in Times Font",
		 fg = "red",
		 font = "Times").pack()
tk.Label(root, 
		 text="Green Text in Helvetica Font",
		 fg = "light green",
		 bg = "dark green",
		 font = "Helvetica 16 bold italic").pack()
tk.Label(root, 
		 text="Blue Text in Verdana bold",
		 fg = "blue",
		 bg = "yellow",
		 font = "Verdana 10 bold").pack()

root.mainloop()"""

explanation2 = """The widget can be used to display short text messages. The message widget is similar in its functionality to the Label widget, but it is more flexible in displaying text, e.g. the font can be changed while the Label widget can only display text in a single font.
It provides a multiline object, that is the text may span more than one line. The text is automatically broken into lines and justified. We were ambiguous, when we said, that the font of the message widget can be changed. This means that we can choose arbitrarily a font for one widget,
but the text of this widget will be rendered solely in this font. This means that we can't change the font within a widget. So it's not possible to have a text in more than one font. If you need to display text in multiple fonts, we suggest to use a Text widget. 
The syntax of a message widget: 
	w = Message ( master, option, ... ) 
	Let's have a look at a simple example. The following script creates a message with a famous saying by Mahatma Gandhi: 

	import tkinter as tk
	master = tk.Tk()
	whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
	msg = tk.Message(master, text = whatever_you_do)
	msg.config(bg='lightgreen', font=('times', 24, 'italic'))
	msg.pack()
	tk.mainloop()"""

explanation3 = """The Button widget is a standard Tkinter widget, which is used for various kinds of buttons. A button is a widget which is designed for the user to interact with, i.e. if the button is pressed by mouse click some action might be started. They can also contain text
and images like labels. While labels can display text in various fonts, a button can only display text in a single font. The text of a button can span more than one line. A Python function or method can be associated with a button. This function or method will be executed, if the
button is pressed in some way.
def write_slogan():
    print("Tkinter is easy to use!")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Hello",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)
"""

explanation4 = """Some widgets (like text entry widgets, radio buttons and so on) can be connected directly to application variables by using special options: variable, textvariable, onvalue, offvalue, and value. This connection works both ways: if the variable changes for any reason,
the widget it's connected to will be updated to reflect the new value. These Tkinter control variables are used like regular Python variables to keep certain values. It's not possible to hand over a regular Python variable to a widget through a variable or textvariable option. The
only kinds of variables for which this works are variables that are subclassed from a class called Variable, defined in the Tkinter module. They are declared like this:
x = StringVar() # Holds a string; default value ""
x = IntVar() # Holds an integer; default value 0
x = DoubleVar() # Holds a float; default value 0.0
x = BooleanVar() # Holds a boolean, returns 0 for False and 1 for True"""

explanation5 = """A radio button, sometimes called option button, is a graphical user interface element of Tkinter, which allows the user to choose (exactly) one of a predefined set of options. Radio buttons can contain text or images. The button can only display text in a single font.
A Python function or method can be associated with a radio button. This function or method will be called, if you press this radio button. Radio buttons are named after the physical buttons used on old radios to select wave bands or preset radio stations. If such a button was pressed,
other buttons would pop out, leaving the pressed button the only pushed in button.Each group of Radio button widgets has to be associated with the same variable. Pushing a button changes the value of this variable to a predefined certain value. 

import tkinter as tk
root = tk.Tk()
v = tk.IntVar()
tk.Label(root, text=Choose a programming language:,justify = tk.LEFT,padx = 20).pack()
tk.Radiobutton(root,text="Python",padx = 20,variable=v,value=1).pack(anchor=tk.W)
tk.Radiobutton(root,text="Perl",padx = 20,variable=v, value=2).pack(anchor=tk.W)
root.mainloop()"""

explanation6 = """Instead of having radio buttons with circular holes containing white space, we can have radio buttons with the complete text in a box. We can do this by setting the indicatoron (stands for "indicator on") option to 0, which means that there will be no separate radio button
indicator. The default is 1.We exchange the definition of the Radiobutton in the previous example with the following one: 

     tk.Radiobutton(root,text=language , indicatoron = 0 , width = 20 , padx = 20 , variable=v , command=ShowChoice , value=val).pack(anchor=tk.W)"""

explanation7 = """Entry widgets are the basic widgets of Tkinter used to get input, i.e. text strings, from the user of an application. This widget allows the user to enter a single line of text. If the user enters a string, which is longer than the available display space of the widget, the
content will be scrolled. This means that the string cannot be seen in its entirety. The arrow keys can be used to move to the invisible parts of the string. If you want to enter multiple lines of text, you have to use the text widget. An entry widget is also limited to single font. 
The syntax of an entry widget looks like this: 
w = Entry(master, option, ... ) 
"master" represents the parent window, where the entry widget should be placed.

from tkinter import *
master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
mainloop( )"""

explanation8 = """To put it in a nutshell: The get() method is what we are looking for. We extend our little script by two buttons "Quit" and "Show". We bind the function show_entry_fields(), which is using the get() method on the Entry objects, to the Show button.

from tkinter import *
def show_entry_fields():
  print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
Button(master, text='Quit', command=master.destroy).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
mainloop( )"""

explanation9 = """Checkboxes, also known as tickboxes or tick boxes or check boxes, are widgets that permit the user to make multiple selections from a number of different options. This is different to a radio button, where the user can make only one choice. 
Usually, checkboxes are shown on the screen as square boxes that can contain white spaces (for false, i.e not checked) or a tick mark or X (for true, i.e. checked),state of a checkbox is changed by clicking the mouse on the box. Alternatively it can be done by
clicking on the caption, or by using a keyboard shortcut, for example the space bar. A Checkbox has two states: on or off. The Tkinter Checkbutton widget can contain text, but only in a single font, or images, and a button can be associated with a Python function or method.
from tkinter import *
master = Tk()
def var_states():
   print("male: %d,\nfemale: %d" % (var1.get(), var2.get()))
Label(master, text="Your sex:").grid(row=0, sticky=W)
var1 = IntVar()
Checkbutton(master, text="male", variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(master, text="female", variable=var2).grid(row=2, sticky=W)
Button(master, text='Quit', command=master.destroy).grid(row=3, sticky=W, pady=4)
Button(master, text='Show', command=var_states).grid(row=4, sticky=W, pady=4)
mainloop()"""

explanation10 = """A text widget is used for multi-line text area. The Tkinter text widget is very powerful and flexible and can be used for a wide range of tasks. Though one of the main purposes is to provide simple multi-line areas, as they are often used in forms, text widgets
can also be used as simple text editors or even web browsers. Furthermore, text widgets can be used to display links, images, and HTML, even using CSS styles. 
In most other tutorials and text books, it's hard to find a very simple and basic example of a text widget.

from Tkinter import *
root = Tk()
T = Text(root, height=2, width=30)
T.pack()
T.insert(END, "Just a text Widget\nin two lines\n")
mainloop() """

explanation11 = """Now we will be adding scroll - bar

from Tkinter import *
root = Tk()
S = Scrollbar(root)
T = Text(root, height=4, width=50)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote = HAMLET: To be, or not to be--that is the question: Whether 'tis nobler in the mind to suffer The slings and arrows of outrageous fortune Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--No more--and by a sleep to say we end The heartache, and the thousand natural shocks That flesh is heir to. 'Tis a consummation
Devoutly to be wished.
T.insert(END, quote)
mainloop(  )"""

explanation12 = """we will now add an image to the text and bind a command to a text line

from Tkinter import *
root = Tk()
text1 = Text(root, height=20, width=30)
photo=PhotoImage(file='./William_Shakespeare.gif')    text1.insert(END,'\n')
text1.image_create(END, image=photo).pack(side=LEFT)
text2 = Text(root, height=20, width=50)
scroll = Scrollbar(root, command=text2.yview)
text2.configure(yscrollcommand=scroll.set)
text2.tag_configure('bold_italics', font=('Arial',12, 'bold', 'italic'))                   text2.tag_configure('big', font=('Verdana', 20, 'bold'))
text2.tag_configure('color', foreground='#476042',font=('Tempus Sans ITC', 12, 'bold'))
text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END, "Not now, maybe later!"))  text2.insert(END,'\nWilliam Shakespeare\n', 'big')
quote = To be, or not to be that is the question: Whether 'tis Nobler in the mind to suffer The Slings and Arrows of outrageous Fortune, Or to take Arms against a Sea of troubles,
text2.insert(END, quote, 'color')              text2.insert(END, 'follow-up\n', 'follow')
text2.pack(side=LEFT)                          scroll.pack(side=RIGHT, fill=Y)
root.mainloop()"""
#===================================================================================================================================================================================================================================================
#                                                                            D E F I N A T I O N S   F O R   B A S I C 
#===================================================================================================================================================================================================================================================
def ml():
    import skl_main

def tkin():
    root = Tk()
    w = Label(root, text="Hello Tkinter!")
    w.pack()

def tkin1():
    

    root = tk.Tk()
    tk.Label(root, 
                     text="Red Text in Times Font",
                     fg = "red",
                     font = "Times").pack()
    tk.Label(root, 
                     text="Green Text in Helvetica Font",
                     fg = "light green",
                     bg = "dark green",
                     font = "Helvetica 16 bold italic").pack()
    tk.Label(root, 
                     text="Blue Text in Verdana bold",
                     fg = "blue",
                     bg = "yellow",
                     font = "Verdana 10 bold").pack()

def tkin2():
    
	master = tk.Tk()
	whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
	msg = tk.Message(master, text = whatever_you_do)
	msg.config(bg='lightgreen', font=('times', 24, 'italic'))
	msg.pack()
	

def tkin3():
        print("Tkinter is easy to use!")

        root = tk.Tk()
        frame = tk.Frame(root)
        frame.pack()

        button = tk.Button(frame, 
                           text="QUIT", 
                           fg="red",
                           command=quit)
        button.pack(side=tk.LEFT)
        slogan = tk.Button(frame,
                           text="Hello",
                           command=write_slogan)
        slogan.pack(side=tk.LEFT)

def tkin4():        
        root = tk.Tk()

        v = tk.IntVar()

        tk.Label(root, 
                text="""Choose a 
        programming language:""",
                justify = tk.LEFT,
                padx = 20).pack()
        tk.Radiobutton(root, 
                      text="Python",
                      padx = 20, 
                      variable=v, 
                      value=1).pack(anchor=tk.W)
        tk.Radiobutton(root, 
                      text="Perl",
                      padx = 20, 
                      variable=v, 
                      value=2).pack(anchor=tk.W)
def tkin5():
    root = tk.Tk()
    v = tk.IntVar()
    language = [
    ("Python",1),
    ("Perl",2),
    ("Java",3),
    ("C++",4),
    ("C",5)
]
    def ShowChoice():
        print(v.get())
    for val, language in enumerate(language):
                tk.Radiobutton(root, 
                              text=language,
                              indicatoron = 0,
                              width = 20,
                              padx = 20, 
                              variable=v, 
                              command=ShowChoice,
                  value=val).pack(anchor=tk.W)

def tkin5():
    master = Tk()
    Label(master, text="First Name").grid(row=0)
    Label(master, text="Last Name").grid(row=1)
    e1 = Entry(master)
    e2 = Entry(master)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    
def tkin6():
    master = Tk()
    e1 = Entry(master)
    e2 = Entry(master)
    def show_entry_fields():
        print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    Label(master, text="First Name").grid(row=0)
    Label(master, text="Last Name").grid(row=1)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    Button(master, text='Quit', command=master.destroy).grid(row=3, column=0, sticky=W, pady=4)
    Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
    
def tkin7():
    master = Tk()
    def var_states():
       print("male: %d,\nfemale: %d" % (var1.get(), var2.get()))
    Label(master, text="Your sex:").grid(row=0, sticky=W)
    var1 = IntVar()
    Checkbutton(master, text="male", variable=var1).grid(row=1, sticky=W)
    var2 = IntVar()
    Checkbutton(master, text="female", variable=var2).grid(row=2, sticky=W)
    Button(master, text='Quit', command=master.destroy).grid(row=3, sticky=W, pady=4)
    Button(master, text='Show', command=var_states).grid(row=4, sticky=W, pady=4)

def tkin8():
    root = Tk()
    T = Text(root, height=2, width=30)
    T.pack()
    T.insert(END, "Just a text Widget\nin two lines\n")


def tkin9():
    root = Tk()
    S = Scrollbar(root)
    T = Text(root, height=4, width=50)
    S.pack(side=RIGHT, fill=Y)
    T.pack(side=LEFT, fill=Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = """HAMLET: To be, or not to be--that is the question: Whether 'tis nobler in the mind to suffer The slings and arrows of outrageous fortune Or to take arms against a sea of troubles
    And by opposing end them. To die, to sleep--No more--and by a sleep to say we end The heartache, and the thousand natural shocks That flesh is heir to. 'Tis a consummation
    Devoutly to be wished."""
    T.insert(END, quote)
def tkin10():
    root = Tk()
    text1 = Text(root, height=20, width=30)
    
    text1.insert(END,'\n')
    text1.image_create(END, image = photo)
    text1.pack(side=LEFT)
    text2 = Text(root, height=20, width=50)
    scroll = Scrollbar(root, command=text2.yview)
    text2.configure(yscrollcommand=scroll.set)
    text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
    text2.tag_configure('big', font=('Verdana', 20, 'bold'))
    text2.tag_configure('color', foreground='#476042', 
    font=('Tempus Sans ITC', 12, 'bold'))
    text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END, "Not now, maybe later!"))
    text2.insert(END,'\nWilliam Shakespeare\n', 'big')
    quote = """To be, or not to be that is the question:
    Whether 'tis Nobler in the mind to suffer
    The Slings and Arrows of outrageous Fortune,
    Or to take Arms against a Sea of troubles, """
    text2.insert(END, quote, 'color')
    text2.insert(END, 'follow-up\n', 'follow')
    text2.pack(side=LEFT)
    scroll.pack(side=RIGHT, fill=Y)

def Docs():
    webbrowser.open('http://www.tkdocs.com/tutorial/')
def qExit():
    root.destroy()
#=========================================================================================================================================================================================================================================================================================================================
#                                                                                   F R A M E  4
#=========================================================================================================================================================================================================================================================================================================================
def create_window3():
    window3 = tk.Toplevel(root)
    window3.geometry("1600x8000")
    window3.title("BASIC")
    window3.configure(background = "VioletRed1")
    tk.Label(window3, text=explanation10  ,justify = LEFT).pack(side = "top")
    button = Button(window3 , text = "RUN ON IDLE" ,fg="OliveDrab1",bg = "black", command = tkin8).pack()
    tk.Label(window3 , text=explanation11 ,justify = LEFT).pack(side = "top")
    button = Button(window3 , text = "RUN ON IDLE" ,fg="OliveDrab1",bg = "black", command = tkin9).pack()
    tk.Label(window3 , text=explanation12 ,justify = LEFT).pack(side = "top")
    button = Button(window3 , text = "RUN ON IDLE" ,fg="OliveDrab1",bg = "black", command = tkin10).pack()
    #tk.Label(window2 , text=explanation10 ,justify = LEFT).pack(side = "top")
    #button = Button(window2 , text = "RUN ON IDLE" ,fg="OliveDrab1",bg = "black", command = tkin7).pack()
    #button = Button(window3 , text = "NEXT" ,fg = "red2", bg = "yellow2" ,command = create_window3).pack()
#=========================================================================================================================================================================================================================================================================================================================
#                                                                                   F R A M E  3
#=========================================================================================================================================================================================================================================================================================================================
def create_window2():
    window2 = tk.Toplevel(root)
    window2.geometry("1600x8000")
    window2.title("BASIC")
    window2.configure(background = "VioletRed1")
    tk.Label(window2, text=explanation7,justify = LEFT).pack(side = "top")
    button = Button(window2 , text = "RUN ON IDLE" ,fg="OliveDrab1",bg = "black", command = tkin5).pack()
    tk.Label(window2 , text=explanation8 ,justify = LEFT).pack(side = "top")
    button = Button(window2 , text = "RUN ON IDLE" ,fg="OliveDrab1",bg = "black", command = tkin6).pack()
    tk.Label(window2 , text=explanation9 ,justify = LEFT).pack(side = "top")
    button = Button(window2 , text = "RUN ON IDLE" ,fg="OliveDrab1",bg = "black", command = tkin7).pack()
    #tk.Label(window2 , text=explanation10 ,justify = LEFT).pack(side = "top")
    #button = Button(window2 , text = "RUN ON IDLE" ,fg="OliveDrab1",bg = "black", command = tkin7).pack()
    button = Button(window2 , text = "NEXT" ,fg = "red2", bg = "yellow2" ,command = create_window3).pack()
#=========================================================================================================================================================================================================================================================================================================================
#                                                                                   F R A M E  2
#=========================================================================================================================================================================================================================================================================================================================
def create_window1():
    window1 = tk.Toplevel(root)
    window1.geometry("1600x8000")
    window1.title("BASIC")
    window1.configure(background = "VioletRed1")
    tk.Label(window1, text=explanation3,justify = LEFT).pack(side = "top")
    button = Button(window1 , text = "RUN ON IDLE" ,fg="OliveDrab1",bg = "black", command = tkin3).pack()
    tk.Label(window1 , text=explanation4 ,justify = LEFT).pack(side = "top")
    tk.Label(window1 , text=explanation5 ,justify = LEFT).pack(side = "top")
    button = Button(window1 , text = "RUN ON IDLE" ,fg="OliveDrab1",bg = "black", command = tkin4).pack()
    tk.Label(window1 , text=explanation6 ,justify = LEFT).pack(side = "top")
    button = Button(window1 , text = "RUN ON IDLE" ,fg="OliveDrab1", bg = "black",command = tkin5).pack()
    button = Button(window1 , text = "NEXT" ,fg = "red2", bg = "yellow2" ,command = create_window2).pack()
   # button = Button(window1 , text = "BACK" , command = create_window).pack()
#=========================================================================================================================================================================================================================================================================================================================
#                                                                                  F R A M E  1
#=========================================================================================================================================================================================================================================================================================================================
def create_window():
    #root.destroy()
    
    window = tk.Toplevel(root)
    window.geometry("1600x8000")
    window.title("BASIC")
    window.configure(background = "VioletRed1")
    tk.Label(window, text=explanation,justify = LEFT).pack(side = "top")
    button = Button(window , text = "RUN ON IDLE" ,fg="OliveDrab1",bg = "black", command = tkin).pack()
    tk.Label(window , text=explanation1 ,justify = LEFT).pack(side = "top")
    button = Button(window , text = "RUN ON IDLE" ,fg="OliveDrab1", bg = "black",command = tkin1).pack()
    tk.Label(window , text=explanation2 ,justify = LEFT).pack(side = "top")
    button = Button(window , text = "RUN ON IDLE" , fg="OliveDrab1",bg = "black",command = tkin2).pack()
    button = Button(window , text = "NEXT" ,fg = "red2", bg = "yellow2" ,command = create_window1 ).pack()
    
    
#===================================================================================================================================================================================================================================================
#                                                                       M A I N   W I N D O W   B U T T O N S 
#===================================================================================================================================================================================================================================================

btnTotal=tk.Button(f1,padx=16,pady=8,bd=16,fg="red",font=('arial',16,'bold'),width=10,text="Basic",bg="burlywood2",command=create_window).pack(side=TOP, padx=20,pady=7)#grid(row=7,column=1)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="blue",font=('arial',16,'bold'),width=10,text="Advance",bg="burlywood2").pack(side=TOP,pady=7)#grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="green",font=('arial',16,'bold'),width=10,text="DOCS",bg="burlywood2",command = Docs).pack(side=TOP,pady=7)#grid(row=7,column=3)

btnTotal=tk.Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="MachineLearning",bg="burlywood2",command = ml).pack(side=TOP,pady=7)#grid(row=7,column=1)

btnExit=Button(f2,padx=16,pady=8,bd=16,fg="purple4",font=('arial',16,'bold'),width=10,text="Exit",bg="burlywood2",command = qExit).pack()#grid(row=7,column=3)


root.mainloop()

