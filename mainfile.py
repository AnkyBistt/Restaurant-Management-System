import random
import tkinter as tk
from tkinter import *
import pickle

class item:
    itemno=0
    quant=0
    value=0
    amount=0
    def __init__(self,itemno=0,quant=0,value=0,amount=0):
        self.itemno=itemno
        self.quant=quant
        self.value=value
        self.amount=amount
    def retValue(self):
        return value
    def retQuant(self):
        return quant


class order:
    orderno=0
    itemList=[]

    def __init__(self,order=1,item=[]):
        self.orderno=order
        self.itemList=item


class bill:
    billno=0
    sgst=0
    cgst=0
    total=0
    def __init__(self,bill=0,sgst=0,cgst=0,total=0):
        self.billno=bill
        self.sgst=sgst
        self.cgst=cgst
        self.total=total

'''
def placeorder():
    orderno=random.randint(0,101)
    neworder=order(orderno,ItemList,)
    with open('order.pkl','wb') as wf:
        pickle.dump(neworder,wf,-1)
'''
ItemList=[]

Item=item(0,0,0)

newOrder=order(0,[])

Bill=bill(0,0,0,0)
def updateItemList(val1=0,val2=0,val3=0):
    global Item
    global ItemList
    Item.itemno=val1
    Item.value=val2
    Item.quant=val3
    Item.amount=val2
    ItemList.append(Item)
    print(val1)
    print(val2)
    print(ItemList[0].amount)

#def updateItemQuant(val):
 #   global Item
  #  Item.quant=0
#def updateItemValue(val):
 #   global Item
  #  Item.value=val
#def updateItemList():
 #   global ItemList
  #  ItemList.append(Item)

def placeorder():
    orderno=random.randint(0,101)
    global newOrder
    global ItemList
    newOrder.orderno=orderno
    newOrder.itemList=ItemList
    with open('order.pkl','ab') as wf:
        pickle.dump(newOrder,wf,-1)


def generateBill(sgst=0,cgst=0):
    with open('order.pkl','rb') as rf:
        while True:
            currentorder=pickle.load(rf)
            if currentorder.orderno==newOrder.orderno:
                break
            elif not currentorder:
                break
    global Bill
    global ItemList
    Bill.billno=random.randint(0,1001)
    Bill.total=0
    for i in range(0,len(ItemList)):
        ItemList[i].amount=ItemList[i].quant * ItemList[i].value
        print(ItemList[i].value)
        Bill.total=Bill.total+ItemList[i].value
    Bill.cgst=0.09*Bill.total
    Bill.sgst=0.09*Bill.total
    Bill.total=Bill.total+Bill.cgst+Bill.sgst
    showbill()

def showbill():
    #global newOrder
    billwindow=tk.Tk()
    billwindow.title('BILL')
    billwindow.geometry('600x400')

    label = tk.Label(billwindow, text='BILL No. ')
    label.config(bg='white', font=('times', 20, 'bold'), fg='black')
    label.grid(row=0, column=0)

    label = tk.Label(billwindow, text=Bill.billno)
    label.config(bg='white', font=('times', 20, 'bold'), fg='black')
    label.grid(row=0, column=1)

    label = tk.Label(billwindow, text='Item No.')
    label.config(bg='white', font=('times', 20, 'bold'), fg='black')
    label.grid(row=1, column=0)


    label = tk.Label(billwindow, text='Price')
    label.config(bg='white', font=('times', 20, 'bold'), fg='black')
    label.grid(row=1, column=2)

    n=2
    global ItemList

    for i in range(0,len(ItemList)):
        label=tk.Label(billwindow,text=ItemList[i].itemno)
        label.config(bg='white', font=('times', 15, 'bold'), fg='blue')
        label.grid(row=n,column=0)


        label = tk.Label(billwindow, text=ItemList[i].quant)
        label.config(bg='white', font=('times', 15, 'bold'), fg='blue')
        label.grid(row=n, column=1)

        label = tk.Label(billwindow, text=ItemList[i].value)
        label.config(bg='white', font=('times', 15, 'bold'), fg='blue')
        label.grid(row=n, column=2)

        label = tk.Label(billwindow, text=ItemList[i].amount)
        label.config(bg='white', font=('times', 15, 'bold'), fg='blue')
        label.grid(row=n, column=3)

        n+=1

    label = tk.Label(billwindow, text='CGST')
    label.config(bg='white', font=('times', 15, 'bold'), fg='blue')
    label.grid(row=n, column=0)


    label = tk.Label(billwindow, text='SGST')
    label.config(bg='white', font=('times', 15, 'bold'), fg='blue')
    label.grid(row=n, column=1)


    label = tk.Label(billwindow, text='TOTAL')
    label.config(bg='white', font=('times', 15, 'bold'), fg='blue')
    label.grid(row=n, column=2)

    n+=1


    label = tk.Label(billwindow, text=Bill.cgst)
    label.config(bg='white', font=('times', 15, 'bold'), fg='blue')
    label.grid(row=n, column=0)


    label = tk.Label(billwindow, text=Bill.sgst)
    label.config(bg='white', font=('times', 15, 'bold'), fg='blue')
    label.grid(row=n, column=1)


    label = tk.Label(billwindow, text=Bill.total)
    label.config(bg='white', font=('times', 15, 'bold'), fg='blue')
    label.grid(row=n, column=2)

    billwindow.mainloop()





mainwindow=tk.Tk()
mainwindow.geometry('1200x800')
mainwindow.title('Restaurant Management System')
label1=tk.Label(mainwindow,text='Restaurant Management System')
label1.config(bg='orange',font=('ComicSansMS',50,'bold'),fg='blue')
label1.grid(row=0,columnspan=10,padx=100,pady=1,ipadx=5,ipady=5)
#img=PhotoImage(file='menu_heading.png')
label2=tk.Label(mainwindow,text='MENU')
label2.config(bg='teal',font=('times',25,'italic'),fg='yellow')
label2.grid(row=1,column=1)
label2=tk.Label(mainwindow,text='price')
label2.config(bg='white',font=('times',15,'bold'),fg='blue')
label2.grid(row=1,column=2)

label2=tk.Label(mainwindow,text='quantity')
label2.config(bg='white',font=('times',15,'bold'),fg='blue')
label2.grid(row=1,column=3)


button8=tk.Button(mainwindow,text='PLACE ORDER',relief='raised',command=lambda:placeorder())
button8.config(bg='red',font=('arial',20,'bold'),width=20)
button8.grid(row=2,column=9)

button8=tk.Button(mainwindow,text='CREATE BILL',relief='raised',command=lambda:generateBill())
button8.config(bg='green',font=('arial',20,'bold'),width=20)
button8.grid(row=4,column=9)

img1=PhotoImage(file='img1.png')
labelimg1=tk.Label(mainwindow,image=img1)
labelimg1.grid(row=2,column=0,padx=0,pady=0)
label2=tk.Label(mainwindow,text='CHOLE KULCHE')
label2.config(bg='white',font=('times',20,'bold'),fg='black')
label2.grid(row=2,column=1)
label2=tk.Label(mainwindow,text='150')
label2.config(bg='white',font=('times',15,'bold'),fg='black')
label2.grid(row=2,column=2)
q1=Entry(mainwindow)
q1.grid(row=2,column=3)
qd1=q1.get()
button1=tk.Button(mainwindow,text='ADD',relief='raised',command=lambda:updateItemList(101,150,qd1))
button1.config(bg='white')
button1.grid(row=2,column=4)


img2=PhotoImage(file='paneertikka.png')
labelimg2=tk.Label(mainwindow,image=img2)
labelimg2.grid(row=3,column=0,padx=0,pady=0)
label3=tk.Label(mainwindow,text='PANEER TIKKA')
label3.config(bg='white',font=('times',20,'bold'),fg='black')
label3.grid(row=3,column=1)
label3=tk.Label(mainwindow,text='180')
label3.config(bg='white',font=('times',15,'bold'),fg='black')
label3.grid(row=3,column=2)
q2=Entry(mainwindow)
q2.grid(row=3,column=3)
qd2=q2.get()
button2=tk.Button(mainwindow,text='ADD',relief='raised',command=lambda:updateItemList(102,180,qd2))
button2.config(bg='white')
button2.grid(row=3,column=4)

img3=PhotoImage(file='cholebhature.png')
labelimg3=tk.Label(mainwindow,image=img3)
labelimg3.grid(row=4,column=0,padx=0,pady=0)
label4=tk.Label(mainwindow,text='CHOLE BHATURE')
label4.config(bg='white',font=('times',20,'bold'),fg='black')
label4.grid(row=4,column=1)
label4=tk.Label(mainwindow,text='60')
label4.config(bg='white',font=('times',15,'bold'),fg='black')
label4.grid(row=4,column=2)
q3=Entry(mainwindow)
q3.grid(row=4,column=3)
qd3=q3.get()
button3=tk.Button(mainwindow,text='ADD',relief='raised',command=lambda:updateItemList(103,60,qd3))
button3.config(bg='white')
button3.grid(row=4,column=4)


img4=PhotoImage(file='malaichaap.png')
labelimg4=tk.Label(mainwindow,image=img4)
labelimg4.grid(row=5,column=0,padx=0,pady=0)
label5=tk.Label(mainwindow,text='MALAI CHAAP')
label5.config(bg='white',font=('times',20,'bold'),fg='black')
label5.grid(row=5,column=1)
label5=tk.Label(mainwindow,text='120')
label5.config(bg='white',font=('times',15,'bold'),fg='black')
label5.grid(row=5,column=2)
q4=Entry(mainwindow)
q4.grid(row=5,column=3)
qd4=q4.get()
button4=tk.Button(mainwindow,text='ADD',relief='raised',command=lambda:updateItemList(104,120,qd4))
button4.config(bg='white')
button4.grid(row=5,column=4)


img5=PhotoImage(file='kathiroll.png')
labelimg5=tk.Label(mainwindow,image=img5)
labelimg5.grid(row=6,column=0,padx=0,pady=0)
label6=tk.Label(mainwindow,text='KATHI ROLL')
label6.config(bg='white',font=('times',20,'bold'),fg='black')
label6.grid(row=6,column=1)
label6=tk.Label(mainwindow,text='100')
label6.config(bg='white',font=('times',15,'bold'),fg='black')
label6.grid(row=6,column=2)
q5=Entry(mainwindow)
q5.grid(row=6,column=3)
qd5=q5.get()
button5=tk.Button(mainwindow,text='ADD',relief='raised',command=lambda:updateItemList(105,100,qd5))
button5.config(bg='white')
button5.grid(row=6,column=4)


img6=PhotoImage(file='rajmachawal.png')
labelimg6=tk.Label(mainwindow,image=img6)
labelimg6.grid(row=7,column=0,padx=0,pady=0)
label7=tk.Label(mainwindow,text='RAJMA CAHWAL')
label7.config(bg='white',font=('times',20,'bold'),fg='black')
label7.grid(row=7,column=1)
label7=tk.Label(mainwindow,text='80')
label7.config(bg='white',font=('times',15,'bold'),fg='black')
label7.grid(row=7,column=2)
q6=Entry(mainwindow)
q6.grid(row=7,column=3)
qd6=q6.get()
button6=tk.Button(mainwindow,text='ADD',relief='raised',command=lambda:updateItemList(106,80,qd6))
button6.config(bg='white')
button6.grid(row=7,column=4)


img7=PhotoImage(file='rasmalai.png')
labelimg7=tk.Label(mainwindow,image=img7)
labelimg7.grid(row=8,column=0,padx=0,pady=0)
label8=tk.Label(mainwindow,text=' KESAR RASMALAI')
label8.config(bg='white',font=('times',20,'bold'),fg='black')
label8.grid(row=8,column=1)
label8=tk.Label(mainwindow,text='50')
label8.config(bg='white',font=('times',15,'bold'),fg='black')
label8.grid(row=8,column=2)
q7=Entry(mainwindow)
q7.grid(row=8,column=3)
qd7=q7.get()
button7=tk.Button(mainwindow,text='ADD',relief='raised',command=lambda:updateItemList(107,50,qd7))
button7.config(bg='white')
button7.grid(row=8,column=4)


mainwindow.mainloop()


