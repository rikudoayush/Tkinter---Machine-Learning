import tkinter as tk
from tkinter import *
'''for python 2 unmark the below and mark the other three'''
#import tkMessageBox
#import tkFileDialog
'''#'''from tkinter.messagebox import *
'''#'''from tkinter.filedialog import askopenfilename
'''#'''from tkinter.colorchooser import askcolor
import random
import time
import datetime
#import subprocess
import webbrowser
import threading
import tkinter_basic

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
#                                                                        D E S I G N I N G   T H E   T I T L E          
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
#                                                                        T E X T S   F O R   A D V A N C E 
#===================================================================================================================================================================================================================================================
explanation = """A slider is a Tkinter object with which a user can set a value by moving an indicator. Sliders can be vertically or horizontally arranged. A slider is created with the Scale method(). Using the Scale widget creates a graphical object, which allows the user
to select a numerical value by moving a knob along a scale of a range of values. The minimum and maximum values can be set as parameters, as well as the resolution.We can also determine if we want the slider vertically or horizontally positioned.A Scale widget is a good alternative
to an Entry widget, if the user is supposed to put in a number from a finite range, i.e. a bounded numerical value.

from Tkinter import *
def show_values():
    print (w1.get(), w2.get())
master = Tk()
w1 = Scale(master, from_=0, to=42, tickinterval=8)
w1.set(19)
w1.pack()
w2 = Scale(master, from_=0, to=200, length=600,tickinterval=10, orient=HORIZONTAL)
w2.set(23)
w2.pack()
Button(master, text='Show', command=show_values).pack()
mainloop()"""

explanation1 = """Tkinter (and TK of course) provides a set of dialogues (dialogs in American English spelling), which can be used to display message boxes, showing warning or errors, or widgets to select files and colours. There are also simple dialogues, asking the user to enter string,
integers or float numbers.

from Tkinter import *
from tkMessageBox import *
def answer():
    showerror("Answer", "Sorry, no answer available")

def callback():
    if askyesno('Verify', 'Really quit?'):
        showwarning('Yes', 'Not yet implemented')
    else:
        showinfo('No', 'Quit has been cancelled')
Button(text='Quit', command=callback).pack(fill=X)
Button(text='Answer', command=answer).pack(fill=X)
mainloop()"""

explanation2 = """There is hardly any serious application, which doesn't need a way to read from a file or write to a file. Furthermore, such an application might have to choose a directory. Tkinter provides the module tkFileDialog for these purposes.

from Tkinter import *
from tkFileDialog   import askopenfilename      
def callback():
    name= askopenfilename() 
    print name
errmsg = 'Error!'
Button(text='File Open', command=callback).pack(fill=X)
mainloop()"""

explanation3 = """Most people, if confronted with the word "menu", will immediately think of a menu in a restaurant. Even though the menu of a restaurant and the menu of a computer program have at first glance nothing in common, we can see that yet
the have a lot in common. In a restaurant, a menu is a presentation of all their food and beverage offerings, while in a computer application it presents all the commands and functions of the application, which are available to the user via the grafical user interface. 
Menus in GUIs are presented with a combination of text and symbols to represent the choices. Selecting with the mouse (or finger on touch screens) on one of the symbols or text, an action will be started. Such an action or operation can for example be the
opening or saving of a file, or the quitting or exiting of an application. A context menu is a menu in which the choices presented to the user are modified according to the current context in which the user is located. 
We introduce in this chapter of our Python Tkinter tutorial the pull-down menus of Tkinter, i.e. the lists at the top of the windows, which appear (or pull down), if you click on an item like for example "File", "Edit" or "Help".

from Tkinter import *
from tkFileDialog   import askopenfilename
def NewFile():
    print "New File!"
def OpenFile():
    name = askopenfilename()
    print name
def About():
    print "This is a simple example of a menu" 
root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)
mainloop()"""

explanation4 = """There are applications where the user should have the possibility to select a colour. Tkinter provides a pop-up menu to choose a colour. To this purpose we have to import the tkColorChooser module and have to use the method askColor:result = tkColorChooser.askColor
( color, option=value, ...)
If the user clicks the OK button on the pop-up window, respectively, the return value of askColor() is a tuple with two elements, both a representation of the chosen colour, e.g. ((106, 150, 98), '#6a9662') 
The first element return[0] is a tuple (R, G, B) with the RGB representation in decimal values (from 0 to 255). The second element return[1] is a hexadecimal representation of the chosen colour. 
If the user clicks "Cancel" the method returns the tuple (None, None).

from Tkinter import *
from tkColorChooser import askcolor                  
def callback():
    result = askcolor(color="#6A9662", 
                      title = "Bernd's Colour Chooser") 
    print result    
root = Tk()
Button(root, 
       text='Choose Color', 
       fg="darkgreen", 
       command=callback).pack(side=LEFT, padx=10)
Button(text='Quit', 
       command=root.quit,
       fg="red").pack(side=LEFT, padx=10)
mainloop()"""

explanation6 = """The Canvas widget supplies graphics facilities for Tkinter. Among these graphical objects are lines, circles, images, and even other widgets. With this widget it's possible to draw graphs and plots, create graphics editors, and implement various kinds of custom widgets. 
We demonstrate in our first example, how to draw a line.The method create_line(coords, options) is used to draw a straight line. The coordinates "coords" are given as four integer numbers: x1, y1, x2, y2 This means that the line goes from the point (x1, y1) to the point (x2, y2) After these
coordinates follows a comma separated list of additional parameters, which may be empty. We set for example the colour of the line to the special green of our website: fill="#476042" We kept the first example intentionally very simple. We create a canvas and draw a straight horizontal
line into this canvas. This line vertically cuts the canvas into two areas. The casting to an integer value in the assignment "y = int(canvas_height / 2)" is superfluous, because create_line can work with float values as well. They are automatically turned into integer values. In the
following you can see the code of our first simple script:

from tkinter import *
canvas_width = 500
canvas_height = 150
def paint( event ):
   python_green = "#476042"
   x1, y1 = ( event.x - 1 ), ( event.y - 1 )
   x2, y2 = ( event.x + 1 ), ( event.y + 1 )
   w.create_oval( x1, y1, x2, y2, fill = python_green )
master = Tk()
master.title( "Painting using Ovals" )
w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack(expand = YES, fill = BOTH)
w.bind( "<B1-Motion>", paint )
message = Label( master, text = "Press and Drag the mouse to draw" )
message.pack( side = BOTTOM )
   
mainloop()"""

explanation7 = """A Tkinter application runs most of its time inside an event loop, which is entered via the mainloop method. It waiting for events to happen. Events can be key presses or mouse operations by the user. 
Tkinter provides a mechanism to let the programmer deal with events. For each widget, it's possible to bind Python functions and methods to an event. 
widget.bind(event, handler) 
If the defined event occurs in the widget, the "handler" function is called with an event object. describing the event.

# write tkinter as Tkinter to be Python 2.x compatible
from tkinter import *
def motion(event):
  print("Mouse position: (%s %s)" % (event.x, event.y))
  return
master = Tk()
whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do 
it.\n(Mahatma Gandhi)"
msg = Message(master, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.bind('<Motion>',motion)
msg.pack()
mainloop())
                                  OPEN IDLE TO SEE THE EXECUTION"""

explanation8 = """
import threading
import time
from tkinter import Tk, Button

root = Tk()

def just_wait(seconds):
    print('Waiting for ', seconds, ' seconds...')
    time.sleep(seconds)
    print('Done sleeping.')

def button_callback():
    # Without the thread, the button will stay depressed and the
    # program will respond until the function has returned
    my_thread = threading.Thread(target=just_wait, args=(5,))
    my_thread.start()

button = Button(root, text='Run long thread.', command=button_callback)
button.pack()

# Without them pressing a button that performs
# a long action will pause the entire program and it 
# Will appear as if the program froze - Note about the GIL and only maximizing one cpu

root.mainloop()

                          OPEN IN IDLE TO SEE THE EXECUTION"""

explanation9 = """                                  DRAWING ON CANVAS

from tkinter import Tk, Canvas
root = Tk()

canv = Canvas(root, width=200, height=100)
canv.pack()

# Draw blue line from top left to bottom right with wide dashes
canv.create_line(0, 0, 200, 100, fill='blue', dash=(5, 15))

# Draw green rectangle at (100,50) to (120,55)
canv.create_rectangle(100, 50, 120, 55, fill='green')

# Draw oval(circle) from (20,20) to (40,40)
canv.create_oval(20, 20, 40, 40)

root.mainloop()"""

explanation10 = """"""

explanation11 = """"""

explanation12 = """"""
#===================================================================================================================================================================================================================================================
#                                                                        D E F I N A T I O N S   F O R   A D V A N C E
#===================================================================================================================================================================================================================================================
def ml():
    import skl_main   

def tkin():
    def show_values():
        print (w1.get(), w2.get())
    master = Tk()
    w1 = Scale(master, from_=0, to=42, tickinterval=8)
    w1.set(19)
    w1.pack()
    w2 = Scale(master, from_=0, to=200, length=600,tickinterval=10, orient=HORIZONTAL)
    w2.set(23)
    w2.pack()
    Button(master, text='Show', command=show_values).pack()

def tkin1():
    def answer():
        showerror("Answer", "Sorry, no answer available")

    def callback():
        if askyesno('Verify', 'Really quit?'):
            showwarning('Yes', 'Not yet implemented')
        else:
            showinfo('No', 'Quit has been cancelled')
    Button(text='Quit', command=callback).pack(fill=X)
    Button(text='Answer', command=answer).pack(fill=X)

def tkin2():
    def callback():
        def OpenFile():
            name = askopenfilename()
            print (name)
        def About():
            print ("This is a simple example of a menu") 
        root = Tk()
        menu = Menu(root)
        root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Open...", command=OpenFile)
        filemenu.add_separator()
    
        errmsg = 'Error!'
        Button(text='File Open', command=callback).pack(fill=X)

def tkin3():
    def NewFile():
       print ("New File!")
    def OpenFile():
        name = askopenfilename()
        print (name)
    def About():
        print ("This is a simple example of a menu") 
    root = Tk()
    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="New", command=NewFile)
    filemenu.add_command(label="Open...", command=OpenFile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    helpmenu = Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About...", command=About)
    
def tkin4():
    def callback():
        result = askcolor(color="#6A9662", 
                          title = "Bernd's Colour Chooser") 
        print (result)   
    root = Tk()
    Button(root, 
           text='Choose Color', 
           fg="darkgreen", 
           command=callback).pack(side=LEFT, padx=10)
    Button(text='Quit', 
           command=root.quit,
           fg="red").pack(side=LEFT, padx=10)
def tkin5():
    canvas_width = 500
    canvas_height = 150
    def paint( event ):
       python_green = "#476042"
       x1, y1 = ( event.x - 1 ), ( event.y - 1 )
       x2, y2 = ( event.x + 1 ), ( event.y + 1 )
       w.create_oval( x1, y1, x2, y2, fill = python_green )
    master = Tk()
    master.title( "Painting using Ovals" )
    w = Canvas(master, 
               width=canvas_width, 
               height=canvas_height)
    w.pack(expand = YES, fill = BOTH)
    w.bind( "<B1-Motion>", paint )
    message = Label( master, text = "Press and Drag the mouse to draw" )
    message.pack( side = BOTTOM )

def tkin6():
    root = tk.Tk()
    def motion(event):
        x, y = event.x, event.y
        print('{}, {}'.format(x, y))

    root.bind('<Motion>', motion)
def tkin7():
    root = Tk()

    def just_wait(seconds):
        print('Waiting for ', seconds, ' seconds...')
        time.sleep(seconds)
        print('Done sleeping.')

    def button_callback():
        # Without the thread, the button will stay depressed and the
        # program will respond until the function has returned
        my_thread = threading.Thread(target=just_wait, args=(5,))
        my_thread.start()

    button = Button(root, text='Run long thread.', command=button_callback)
    button.pack()
def tkin8():
    root = Tk()

    canv = Canvas(root, width=200, height=100)
    canv.pack()

    # Draw blue line from top left to bottom right with wide dashes
    canv.create_line(0, 0, 200, 100, fill='blue', dash=(5, 15))

    # Draw green rectangle at (100,50) to (120,55)
    canv.create_rectangle(100, 50, 120, 55, fill='green')

    # Draw oval(circle) from (20,20) to (40,40)
    canv.create_oval(20, 20, 40, 40)
def Docs():
    webbrowser.open('http://www.tkdocs.com/tutorial/')
def qExit():
    root.destroy()
#=========================================================================================================================================================================================================================================================================================================================
#                                                                                   F R A M E  4
#=========================================================================================================================================================================================================================================================================================================================
def create_window7():
    window7 = tk.Toplevel(root)
    window7.geometry("1600x8000")
    window7.title("BASIC")
    window7.configure(background = "VioletRed1")
    tk.Label(window7, text=explanation8  ,justify = LEFT).pack(side = "top")
    button = Button(window7 , text = "RUN ON IDLE" ,fg="OliveDrab1",bg = "black", command = tkin7).pack()
    tk.Label(window7 , text=explanation9 ,justify = LEFT).pack(side = "top")
    button = Button(window7 , text = "RUN ON IDLE" ,fg="OliveDrab1",bg = "black", command = tkin8).pack()
    #tk.Label(window7 , text=explanation12 ,justify = LEFT).pack(side = "top")
    #button = Button(window7 , text = "RUN ON IDLE" ,fg="OliveDrab1",bg = "black", command = tkin10).pack()
    #tk.Label(window2 , text=explanation10 ,justify = LEFT).pack(side = "top")
    #button = Button(window2 , text = "RUN ON IDLE" ,fg="OliveDrab1",bg = "black", command = tkin7).pack()
    #button = Button(window3 , text = "NEXT" ,fg = "red2", bg = "yellow2" ,command = create_window3).pack()
#=========================================================================================================================================================================================================================================================================================================================
#                                                                                   F R A M E  3
#=========================================================================================================================================================================================================================================================================================================================
def create_window6():
    window6 = tk.Toplevel(root)
    window6.geometry("1600x8000")
    window6.title("BASIC")
    window6.configure(background = "VioletRed1")
    tk.Label(window6, text=explanation6,justify = LEFT).pack(side = "top")
    button = Button(window6 , text = "RUN ON IDLE" ,fg="OliveDrab1",bg = "black", command = tkin5).pack()
    tk.Label(window6 , text=explanation7 ,justify = LEFT).pack(side = "top")
    button = Button(window6 , text = "RUN ON IDLE" ,fg="OliveDrab1",bg = "black", command = tkin6).pack()
    #tk.Label(window6 , text=explanation9 ,justify = LEFT).pack(side = "top")
    button = Button(window6 , text = "NEXT" ,fg = "red2", bg = "yellow2" ,command = create_window7).pack()
    #tk.Label(window6 , background = "VioletRed1").pack()
    #button = Button(window6 , text = "RUN ON IDLE" ,fg="OliveDrab1",bg = "black", command = tkin7).pack()
    #button = Button(window2 , text = "RUN ON IDLE" ,fg="OliveDrab1",bg = "black", command = tkin7).pack()
    
#=========================================================================================================================================================================================================================================================================================================================
#                                                                                   F R A M E  2
#=========================================================================================================================================================================================================================================================================================================================
def create_window5():
    window5 = tk.Toplevel(root)
    window5.geometry("1600x8000")
    window5.title("BASIC")
    window5.configure(background = "VioletRed1")
    tk.Label(window5, text=explanation3,justify = LEFT).pack(side = "top")
    button = Button(window5 , text = "RUN ON IDLE" ,fg="OliveDrab1",bg = "black", command = tkin3).pack()
    tk.Label(window5 , text=explanation4 ,justify = LEFT).pack(side = "top")
    button = Button(window5 , text = "RUN ON IDLE" ,fg="OliveDrab1",bg = "black", command = tkin4).pack()
    button = Button(window5 , text = "NEXT" ,fg = "red2", bg = "yellow2" ,command = create_window6).pack()
   # button = Button(window1 , text = "BACK" , command = create_window).pack()
#=========================================================================================================================================================================================================================================================================================================================
#                                                                                  F R A M E  1
#=========================================================================================================================================================================================================================================================================================================================
def create_window4():
    #root.destroy()
    
    window4 = tk.Toplevel(root)
    window4.geometry("1600x8000")
    window4.title("BASIC")
    window4.configure(background = "VioletRed1")
    tk.Label(window4, text=explanation,justify = LEFT).pack(side = "top")
    button = Button(window4 , text = "RUN ON IDLE" ,fg="OliveDrab1",bg = "black", command = tkin).pack()
    tk.Label(window4 , text=explanation1 ,justify = LEFT).pack(side = "top")
    button = Button(window4 , text = "RUN ON IDLE" ,fg="OliveDrab1", bg = "black",command = tkin1).pack()
    tk.Label(window4 , text=explanation2 ,justify = LEFT).pack(side = "top")
    button = Button(window4 , text = "RUN ON IDLE" , fg="OliveDrab1",bg = "black",command = tkin2).pack()
    button = Button(window4 , text = "NEXT" ,fg = "red2", bg = "yellow2" ,command = create_window5 ).pack()
    
    
#===================================================================================================================================================================================================================================================
#                                                                       M A I N   W I N D O W   B U T T O N S 
#===================================================================================================================================================================================================================================================

btnTotal=tk.Button(f1,padx=16,pady=8,bd=16,fg="red",font=('arial',16,'bold'),width=10,text="Basic",bg="burlywood2").pack(side=TOP, padx=20,pady=7)#grid(row=7,column=1)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="blue",font=('arial',16,'bold'),width=10,text="Advance",bg="burlywood2" , command = create_window4).pack(side=TOP,pady=7)#grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="green",font=('arial',16,'bold'),width=10,text="DOCS",bg="burlywood2",command = Docs).pack(side=TOP,pady=7)#grid(row=7,column=3)

btnTotal=tk.Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="MachineLearning",bg="burlywood2",command = ml).pack(side=TOP,pady=7)#grid(row=7,column=1)

btnExit=Button(f2,padx=16,pady=8,bd=16,fg="purple4",font=('arial',16,'bold'),width=10,text="Exit",bg="burlywood2",command = qExit).pack()#grid(row=7,column=3)


root.mainloop()

