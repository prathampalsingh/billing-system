#a Python library that can be used to construct basic graphical user interface (GUI) applications
from tkinter import*
#generates random numbers in Python
import random
#allows us to handle various operations regarding time, its conversions and representations, which find its use in various applications in life
import time


root = Tk()
# building, browsing, navigating and visualizing detector geometries.
root.geometry("890x580+0+0")

root.title("XEROX CENTER BILLING SYSTEM") #The name of the application that will appear in top right corner of the window

Tops = Frame(root,bg="white",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)
#------------------TIME--------------
localtime=time.asctime(time.localtime(time.time()))
#-----------------INFO TOP------------
lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="XEROX CENTER BILLING",fg="Black",bd=10,anchor='w')#main title that will show at the center of application
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="steel blue",anchor=W)#font
lblinfo.grid(row=1,column=0)


def Ref():
    x=random.randint(12980, 50876)
    randomRef = str(x)
    rand.set(randomRef)
#refers to cost of (co)
    #you can change the name using crtl+f (find then name then click on replace all)
    co_filling =float(filling.get())
    co_lamination= float(Lamination.get())
    co_colorxerox= float(colorxerox.get())
    co_BW_print= float(bwprint.get())
    Co_color_print= float(color_print.get())
    Co_BW_xerox= float(bwxerox.get())

#change the pricing of your products here 
    costoffilling = co_filling*10
    costofLamination = co_lamination*20
    costofcolorxerox = co_colorxerox*5
    costofbwprint = co_BW_print*8
    costofcolorprint = Co_color_print*15
    costofbwxerox = Co_BW_xerox*2

    costoftotal = "Rs.",str('%.2f'% (costoffilling +  costofLamination + costofcolorxerox + costofbwprint + costofcolorprint + costofbwxerox))
    PayTax=((costoffilling +  costofLamination + costofcolorxerox + costofbwprint +  costofcolorprint + costofbwxerox)*0.33)
    Totalcost=(costoffilling +  costofLamination + costofcolorxerox + costofbwprint  + costofcolorprint + costofbwxerox)
    Ser_Charge=((costoffilling +  costofLamination + costofcolorxerox + costofbwprint + costofcolorprint + costofbwxerox)/99)
    Service="Rs.",str('%.2f'% Ser_Charge) #service charge
    OverAllCost="Rs.",str( PayTax + Totalcost + Ser_Charge)
    PaidTax="Rs.",str('%.2f'% PayTax)#tax

    Service_Charge.set(Service)
    cost.set(costoftotal)
    Tax.set(PaidTax)
    Subtotal.set(costoftotal)
    Total.set(OverAllCost)


def qexit():
    root.destroy()

#Resets the cursor. This method is available in read, write, or append mode.
def reset():
    rand.set("")
    filling.set("")
    Lamination.set("")
    colorxerox.set("")
    bwprint.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    bwxerox.set("")
    Tax.set("")
    cost.set("")
    color_print.set("")


#---------------------------------------------------------------------------------------
#A StringVar object in Tkinter can help manage the value of a widget such as an Entry widget or a Label widget.
rand = StringVar()
filling = StringVar()
Lamination = StringVar()
colorxerox = StringVar()
bwprint = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
bwxerox = StringVar()
Tax = StringVar()
cost = StringVar()
color_print = StringVar()

#a widget that is used to implement display boxes where you can place text or images.
lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="brown",bd=20,anchor='w')
lblreference.grid(row=0,column=0)
txtreference = Entry(f1,font=('ariel' ,16,'bold'), textvariable=rand , bd=6,insertwidth=6,bg="yellow" ,justify='right')
txtreference.grid(row=0,column=1)

#Filing
lblfilling = Label(f1, font=( 'aria' ,16, 'bold' ),text=" Filling ",fg="blue",bd=10,anchor='w')
lblfilling.grid(row=2,column=0)
txtfilling = Entry(f1,font=('ariel' ,16,'bold'), textvariable=filling , bd=6,insertwidth=4,bg="green" ,justify='right')
txtfilling.grid(row=2,column=1)

#Lamination
lblLamination = Label(f1, font=( 'aria' ,16, 'bold' ),text="Lamination ",fg="blue",bd=10,anchor='w')
lblLamination.grid(row=3,column=0)
txtLamination = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Lamination , bd=6,insertwidth=4,bg="green" ,justify='right')
txtLamination.grid(row=3,column=1)

#Color Xerox
lblcolorxerox = Label(f1, font=( 'aria' ,16, 'bold' ),text="Color xerox ",fg="blue",bd=10,anchor='w')
lblcolorxerox.grid(row=4,column=0)
txtcolorxerox = Entry(f1,font=('ariel' ,16,'bold'), textvariable=colorxerox , bd=6,insertwidth=4,bg="green" ,justify='right')
txtcolorxerox.grid(row=4,column=1)

#Black and White Print
lblbwprint = Label(f1, font=( 'aria' ,16, 'bold' ),text="B&W Print ",fg="blue",bd=10,anchor='w')
lblbwprint.grid(row=5,column=0)
txtbwprint = Entry(f1,font=('ariel' ,16,'bold'), textvariable=bwprint , bd=6,insertwidth=4,bg="green" ,justify='right')
txtbwprint.grid(row=5,column=1)

#Color ptint
lblcolor_print = Label(f1, font=( 'aria' ,16, 'bold' ),text="Color Print",fg="blue",bd=10,anchor='w')
lblcolor_print.grid(row=6,column=0)
txtcolor_print = Entry(f1,font=('ariel' ,16,'bold'), textvariable=color_print , bd=6,insertwidth=4,bg="green" ,justify='right')
txtcolor_print.grid(row=6,column=1)

#Black and White Xerox
lblbwxerox = Label(f1, font=( 'aria' ,16, 'bold' ),text="B&W Xerox",fg="blue",bd=10,anchor='w')
lblbwxerox.grid(row=1,column=0)
txtbwxerox = Entry(f1,font=('ariel' ,16,'bold'), textvariable=bwxerox , bd=6,insertwidth=4,bg="green" ,justify='right')
txtbwxerox.grid(row=1,column=1)

#cost
lblcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cost",fg="black",bd=10,anchor='w')
lblcost.grid(row=2,column=2)
txtcost = Entry(f1,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="white" ,justify='right')
txtcost.grid(row=2,column=3)

#service charge
lblService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="black",bd=10,anchor='w')
lblService_Charge.grid(row=3,column=2)
txtService_Charge = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="white" ,justify='right')
txtService_Charge.grid(row=3,column=3)

#tax
lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax",fg="black",bd=10,anchor='w')
lblTax.grid(row=4,column=2)
txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="white" ,justify='right')
txtTax.grid(row=4,column=3)

#SUBtotal
lblSubtotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Subtotal",fg="black",bd=10,anchor='w')
lblSubtotal.grid(row=5,column=2)
txtSubtotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="white" ,justify='right')
txtSubtotal.grid(row=5,column=3)

#total
lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="green",bd=10,anchor='w')
lblTotal.grid(row=6,column=2)
txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="grey" ,justify='right')
txtTotal.grid(row=6,column=3)

#-----------------------------------------buttons------------------------------------------
lblTotal = Label(f1,text="---------------------",fg="white")
lblTotal.grid(row=7,columnspan=3)

#total button
btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="red",command=Ref)
btnTotal.grid(row=8, column=1)

#reset button
btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="red",command=reset)
btnreset.grid(row=8, column=2)

#exit button
btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="red",command=qexit)
btnexit.grid(row=8, column=3)

#this button opens the tab where we can see the pricing of each item
def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    #filing
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Filling", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="10", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    #lamination
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Lamination ", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="20", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    #Color xerox
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Color Xerox ", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="5", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    #black and white print
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="B&W Print ", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="8", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    #Color print
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Color Print", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="15", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    #black and white print
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="B&W Xerox", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="2", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)

    roo.mainloop()

btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="red",command=price)
btnprice.grid(row=8, column=0)

root.mainloop()