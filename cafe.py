#project on cafe management system using python
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
import os
import tempfile
from tkinter import messagebox
class CafeManagement:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1515x700+0+50")
        self.root.title("Cafe Management System")
        self.root.resizable(False,False)
        headingFrame=Frame(self.root,relief=RIDGE,borderwidth=5,background='yellow')
        headingFrame.place(x=3,y=5,width=1510,height=60)
        nameHeading=Label(headingFrame,text="CAFE MANAGEMENT SYSTEM",font=("robot",25,'bold'),foreground='blue',bg='yellow')
        nameHeading.pack(pady=5)
        #---------------------------variable create--------------------
        
        self.var_cappuccino=StringVar()
        self.var_Mocha=StringVar()
        self.var_Lrish=StringVar()
        self.var_Latte=StringVar()
        self.var_Iecd=StringVar()
        self.var_LatteMa=StringVar()
        self.var_Chiifon=StringVar()
        self.var_sponge=StringVar()
        self.var_vanilla=StringVar()
        self.var_coconut=StringVar()
        self.var_cupcake=StringVar()
        self.var_black=StringVar()
        
        frame1=Frame(self.root,relief=RIDGE,borderwidth=5,background='yellow')
        frame1.place(x=3,y=65,width=1510,height=560)
        frame2=LabelFrame(frame1,relief=RIDGE,borderwidth=5,background='white',text='Coffee',font=("roboto",15,'bold'))
        frame2.place(x=3,y=3,width=1040,height=270)
        
       
        #image add 1 in frame 1
        image_1=Image.open(r'D:\Cafe Management system\Photos\cappuccino.jpg')
        image_1=image_1.resize((150,90))
        self.photo1=ImageTk.PhotoImage(image_1)
        self.imageLabel=Label(frame2,image=self.photo1)
        #self.imageLabel.place(x=2,y=60)
        self.imageLabel.grid(row=0,column=0,padx=3,pady=5)
        
        
        #Cappuccino label and entry-----------------------
        
        CappuccinoName=Label(frame2,text='Name:Cappuccino',font=("times new roman",15,'bold'))
        CappuccinoName.place(x=160,y=5)
        #price Cappuccino
        CappuccinoPrice=Label(frame2,text='Price:50',font=("times new roman",15,'bold'))
        CappuccinoPrice.place(x=160,y=35)
        #Qty Cappuccino
        CappuccinoName=Label(frame2,text='Qty:',font=("times new roman",15,'bold'))
        CappuccinoName.place(x=160,y=65)
        #entry Cappuccino
        CappuccinoNameEntry=ttk.Entry(frame2,font=("times new roman",15,'bold'),justify='center',textvariable=self.var_cappuccino)
        CappuccinoNameEntry.place(x=210,y=65,width=55)
        CappuccinoNameEntry.insert(0,0)
        
        #---------------------------------
        
        #image add 1 in frame 1
        image_2=Image.open(r'D:\Cafe Management system\Photos\mocha.jpg')
        image_2=image_2.resize((150,90))
        self.photo2=ImageTk.PhotoImage(image_2)
        self.imagemocha=Label(frame2,image=self.photo2)
        #self.imageLabel.place(x=2,y=60)
        self.imagemocha.place(x=330,y=5)
        
        #mocha label and entry-----------------------
        
        mochaName=Label(frame2,text='Name:Mocha',font=("times new roman",15,'bold'))
        mochaName.place(x=487,y=5)
        #price mocha
        mochaPrice=Label(frame2,text='Price:30',font=("times new roman",15,'bold'))
        mochaPrice.place(x=487,y=35)
        #Qty mocha
        mochaNameQty=Label(frame2,text='Qty:',font=("times new roman",15,'bold'))
        mochaNameQty=Label(frame2,text='Qty:',font=("times new roman",15,'bold'))
        mochaNameQty.place(x=487,y=65)
        #entry mocha
        mochaNameEntry=ttk.Entry(frame2,font=("times new roman",15,'bold'),justify='center',textvariable=self.var_Mocha)
        mochaNameEntry.place(x=537,y=65,width=55)
        mochaNameEntry.insert(0,0)
        
        #image add 1 in frame 1
        image_3=Image.open(r'D:\Cafe Management system\Photos\lrish.jpg')
        image_3=image_3.resize((150,90))
        self.photo3=ImageTk.PhotoImage(image_3)
        self.imagemocha=Label(frame2,image=self.photo3)
        #self.imageLabel.place(x=2,y=60)
        self.imagemocha.place(x=618,y=5)
        
        #mocha label and entry-----------------------
        
        lrishName=Label(frame2,text='Name:Lrish',font=("times new roman",15,'bold'))
        lrishName.place(x=778,y=5)
        #price mocha
        lrishPrice=Label(frame2,text='Price:30',font=("times new roman",15,'bold'))
        lrishPrice.place(x=778,y=35)
        #Qty mocha
        lrishNameQty=Label(frame2,text='Qty:',font=("times new roman",15,'bold'))
        lrishNameQty=Label(frame2,text='Qty:',font=("times new roman",15,'bold'))
        lrishNameQty.place(x=778,y=65)
        #entry mocha
        lrishNameEntry=ttk.Entry(frame2,font=("times new roman",15,'bold'),justify='center',textvariable=self.var_Lrish)
        lrishNameEntry.place(x=830,y=65,width=55)
        lrishNameEntry.insert(0,0)
        
        #---------------second row------------------------
        #Latte label and entry-----------------------
        
        #image add 1 in frame 1
        image_4=Image.open(r'D:\Cafe Management system\Photos\Latte.jpg')
        image_4=image_4.resize((150,90))
        self.photo4=ImageTk.PhotoImage(image_4)
        self.imageLabel4=Label(frame2,image=self.photo4)
        self.imageLabel4.grid(row=1,column=0,padx=3,pady=15)
        
        latteName=Label(frame2,text='Name:Latte',font=("times new roman",15,'bold'))
        latteName.place(x=160,y=120)
        #price Latte
        latteNamePrice=Label(frame2,text='Price:70',font=("times new roman",15,'bold'))
        latteNamePrice.place(x=160,y=150)
        #Qty Latte
        latteName=Label(frame2,text='Qty:',font=("times new roman",15,'bold'))
        latteName.place(x=160,y=180)
        #entry Latte
        latteNameEntry=ttk.Entry(frame2,font=("times new roman",15,'bold'),justify='center',textvariable=self.var_Latte)
        latteNameEntry.place(x=210,y=181,width=55)
        latteNameEntry.insert(0,0)
        
        #---------------------------------
        
       #---------------------------------
        
        #image add 1 in frame 1
        image_5=Image.open(r'D:\Cafe Management system\Photos\iced.jpg')
        image_5=image_5.resize((150,90))
        self.photo5=ImageTk.PhotoImage(image_5)
        self.image5=Label(frame2,image=self.photo5)
        #self.imageLabel.place(x=2,y=60)
        self.image5.place(x=330,y=120)
        
        #iced label and entry-----------------------
        icedName=Label(frame2,text='Name:Iced',font=("times new roman",15,'bold'))
        icedName.place(x=487,y=120)
        #price iced
        icedPrice=Label(frame2,text='Price:45',font=("times new roman",15,'bold'))
        icedPrice.place(x=487,y=150)
        #Qty iced
        icedNameQty=Label(frame2,text='Qty:',font=("times new roman",15,'bold'))
        icedNameQty=Label(frame2,text='Qty:',font=("times new roman",15,'bold'))
        icedNameQty.place(x=487,y=180)
        #entry iced
        icedNameEntry=ttk.Entry(frame2,font=("times new roman",15,'bold'),justify='center',textvariable=self.var_Iecd)
        icedNameEntry.place(x=537,y=181,width=55)
        icedNameEntry.insert(0,0)
        
        #----------------------------------------------------
        #image add 1 in frame 1
        image_6=Image.open(r'D:\Cafe Management system\Photos\lattemacchiato.jpg')
        image_6=image_6.resize((150,90))
        self.photo6=ImageTk.PhotoImage(image_6)
        self.image6=Label(frame2,image=self.photo6)
        #self.imageLabel.place(x=2,y=60)
        self.image6.place(x=618,y=120)
        
        #lattemacchiato label and entry-----------------------
        
        LatteName=Label(frame2,text='Name:Latte Macchiato',font=("times new roman",15,'bold'))
        LatteName.place(x=778,y=120)
        #price lattemacchiato
        LatteNamePrice=Label(frame2,text='Price:100',font=("times new roman",15,'bold'))
        LatteNamePrice.place(x=778,y=150)
        #Qty lattemacchiato
        LatteNameQty=Label(frame2,text='Qty:',font=("times new roman",15,'bold'))
        LatteNameQty=Label(frame2,text='Qty:',font=("times new roman",15,'bold'))
        LatteNameQty.place(x=778,y=180)
        #entry lattemacchiato
        LatteNameEntry=ttk.Entry(frame2,font=("times new roman",15,'bold'),justify='center',textvariable=self.var_LatteMa)
        LatteNameEntry.place(x=830,y=181,width=55)
        LatteNameEntry.insert(0,0)
        
        
        #------------------------------frame 3 for cake-------------------------
        
        frame3=LabelFrame(frame1,text='Cake',font=('roboto',15,'bold'),relief=RIDGE,borderwidth=5,background='white')
        frame3.place(x=3,y=273,width=1040,height=270)
        
        #image add 1 in frame 1
        imageChiffon=Image.open(r'D:\Cafe Management system\Photos\Chiffon Cake.jpg')
        imageChiffon=imageChiffon.resize((150,90))
        self.photoChiffon=ImageTk.PhotoImage(imageChiffon)
        self.imageChiffon=Label(frame3,image=self.photoChiffon)
        #self.imageLabel.place(x=2,y=60)
        self.imageChiffon.grid(row=0,column=0,padx=3,pady=5)
        
        
        #Chiffon label and entry-----------------------
        
        ChiffonName=Label(frame3,text='Name:Chiffon',font=("times new roman",15,'bold'))
        ChiffonName.place(x=160,y=5)
        #price Chiffon
        ChiffonPrice=Label(frame3,text='Price:150',font=("times new roman",15,'bold'))
        ChiffonPrice.place(x=160,y=35)
        #Qty Chiffon
        ChiffonName=Label(frame3,text='Qty:',font=("times new roman",15,'bold'))
        ChiffonName.place(x=160,y=65)
        #entry Chiffon
        ChiffonNameEntry=ttk.Entry(frame3,font=("times new roman",15,'bold'),justify='center',textvariable=self.var_Chiifon)
        ChiffonNameEntry.place(x=210,y=65,width=55)
        ChiffonNameEntry.insert(0,0)
        
        #---------------------------------
        
        #image add 1 in frame 1
        imagesponge=Image.open(r'D:\Cafe Management system\Photos\sponge-cake-16.jpg')
        imagesponge=imagesponge.resize((150,90))
        self.photosponge=ImageTk.PhotoImage(imagesponge)
        self.imagesponge=Label(frame3,image=self.photosponge)
        #self.imageLabel.place(x=2,y=60)
        self.imagesponge.place(x=330,y=5)
        
        #sponge label and entry-----------------------
        
        SpongeName=Label(frame3,text='Name:Sponge',font=("times new roman",15,'bold'))
        SpongeName.place(x=487,y=5)
        #price sponge
        SpongePrice=Label(frame3,text='Price:130',font=("times new roman",15,'bold'))
        SpongePrice.place(x=487,y=35)
        #Qty sponge
        SpongeNameQty=Label(frame3,text='Qty:',font=("times new roman",15,'bold'))
        SpongeNameQty=Label(frame3,text='Qty:',font=("times new roman",15,'bold'))
        SpongeNameQty.place(x=487,y=65)
        #entry sponge
        SpongeNameEntry=ttk.Entry(frame3,font=("times new roman",15,'bold'),justify='center',textvariable=self.var_sponge)
        SpongeNameEntry.place(x=537,y=65,width=55)
        SpongeNameEntry.insert(0,0)
        
        #image add 1 in frame 1
        imageVanilla=Image.open(r'D:\Cafe Management system\Photos\vanilla-bundt-cake-2.jpg')
        imageVanilla=imageVanilla.resize((150,90))
        self.photoVanilla=ImageTk.PhotoImage(imageVanilla)
        self.imageVanilla=Label(frame3,image=self.photoVanilla)
        #self.imageLabel.place(x=2,y=60)
        self.imageVanilla.place(x=618,y=5)
        
        #vanilla label and entry-----------------------
        
        VanillaName=Label(frame3,text='Name:Vanilla-Bundt',font=("times new roman",15,'bold'))
        VanillaName.place(x=778,y=5)
        #price vanilla
        VanillaPrice=Label(frame3,text='Price:200',font=("times new roman",15,'bold'))
        VanillaPrice.place(x=778,y=35)
        #Qty vanilla
        VanillaNameQty=Label(frame3,text='Qty:',font=("times new roman",15,'bold'))
        VanillaNameQty=Label(frame3,text='Qty:',font=("times new roman",15,'bold'))
        VanillaNameQty.place(x=778,y=65)
        #entry vanilla
        VanillaNameEntry=ttk.Entry(frame3,font=("times new roman",15,'bold'),justify='center',textvariable=self.var_vanilla)
        VanillaNameEntry.place(x=830,y=65,width=55)
        VanillaNameEntry.insert(0,0)
        
        #---------------second row----------------------
        #coconut label and entry-----------------------
        
        #image add 1 in frame 1
        imagecoconut=Image.open(r'D:\Cafe Management system\Photos\coconut-cake-5.jpg')
        imagecoconut=imagecoconut.resize((150,90))
        self.photococonut=ImageTk.PhotoImage(imagecoconut)
        self.imagecoconut=Label(frame3,image=self.photococonut)
        #self.imageLabel.place(x=2,y=60)
        self.imagecoconut.grid(row=1,column=0,padx=3,pady=15)
        
        
        coconutName=Label(frame3,text='Name:Coconut',font=("times new roman",15,'bold'))
        coconutName.place(x=160,y=120)
        #price coconut
        coconutNamePrice=Label(frame3,text='Price:70',font=("times new roman",15,'bold'))
        coconutNamePrice.place(x=160,y=150)
        #Qty coconut
        coconutName=Label(frame3,text='Qty:',font=("times new roman",15,'bold'))
        coconutName.place(x=160,y=180)
        #entry coconut
        coconutNameEntry=ttk.Entry(frame3,font=("times new roman",15,'bold'),justify='center',textvariable=self.var_coconut)
        coconutNameEntry.place(x=210,y=181,width=55)
        coconutNameEntry.insert(0,0)
        
        #---------------------------------
        
       #---------------------------------
        
        #image add 1 in frame 1
        imageCupcake=Image.open(r'D:\Cafe Management system\Photos\istockphoto-167120918-612x612.jpg')
        imageCupcake=imageCupcake.resize((150,90))
        self.photoCupcake=ImageTk.PhotoImage(imageCupcake)
        self.imageCupcake=Label(frame3,image=self.photoCupcake)
        #self.imageLabel.place(x=2,y=60)
        self.imageCupcake.place(x=330,y=120)
        
        #Cupcake label and entry-----------------------
        
        CupcakeName=Label(frame3,text='Name:Cupcake',font=("times new roman",15,'bold'))
        CupcakeName.place(x=487,y=120)
        #price Cupcake
        CupcakePrice=Label(frame3,text='Price:80',font=("times new roman",15,'bold'))
        CupcakePrice.place(x=487,y=150)
        #Qty Cupcake
        CupcakeNameQty=Label(frame3,text='Qty:',font=("times new roman",15,'bold'))
        CupcakeNameQty=Label(frame3,text='Qty:',font=("times new roman",15,'bold'))
        CupcakeNameQty.place(x=487,y=180)
        #entry Cupcake
        CupcakeNameEntry=ttk.Entry(frame3,font=("times new roman",15,'bold'),justify='center',textvariable=self.var_cupcake)
        CupcakeNameEntry.place(x=537,y=181,width=55)
        CupcakeNameEntry.insert(0,0)
        
        #----------------------------------------------------
        #image add 1 in frame 1
        imageblack=Image.open(r'D:\Cafe Management system\Photos\4577-black-forest-gateau-560.jpg')
        imageblack=imageblack.resize((150,90))
        self.photoblack=ImageTk.PhotoImage(imageblack)
        self.imageblack=Label(frame3,image=self.photoblack)
        #self.imageLabel.place(x=2,y=60)
        self.imageblack.place(x=620,y=120)
        
        #Black-Forest-Gateau label and entry-----------------------
        
        blackName=Label(frame3,text='Name:Black-Forest-Gateau',font=("times new roman",15,'bold'))
        blackName.place(x=778,y=120)
        #price Black-Forest-Gateau
        blackNamePrice=Label(frame3,text='Price:350',font=("times new roman",15,'bold'))
        blackNamePrice.place(x=778,y=150)
        #Qty Black-Forest-Gateau
        blackNameQty=Label(frame3,text='Qty:',font=("times new roman",15,'bold'))
        blackNameQty=Label(frame3,text='Qty:',font=("times new roman",15,'bold'))
        blackNameQty.place(x=778,y=180)
        #entry Black-Forest-Gateau
        blackNameEntry=ttk.Entry(frame3,font=("times new roman",15,'bold'),justify='center',textvariable=self.var_black)
        blackNameEntry.place(x=830,y=181,width=55)
        blackNameEntry.insert(0,0)
        
        
        
        frame4=Frame(frame1,relief=RIDGE,borderwidth=5,background='yellow')
        frame4.place(x=1045,y=3,width=450,height=540)
        
        frame5=Frame(frame4,relief=RIDGE,borderwidth=5,background='white')
        frame5.place(x=3,y=3,width=435,height=50)
        
        nameHeading=Label(frame5,text="Bill Area",font=("robot",25,'bold'))
        nameHeading.pack(pady=5)
        
        #image right
        imageright=Image.open(r'D:\Cafe Management system\Photos\431-4317544_backhand-index-pointing-right-icon-finger-pointing-right.png')
        imageright=imageright.resize((50,35))
        self.photoright=ImageTk.PhotoImage(imageright)
        self.imageright=Label(frame5,image=self.photoright)
        self.imageright.place(x=55)
        
        #image left
        imageleft=Image.open(r'D:\Cafe Management system\Photos\128-1283530_backhand-index-pointing-left-icon-left-hand-emoji-png.png')
        imageleft=imageleft.resize((50,35))
        self.photoleft=ImageTk.PhotoImage(imageleft)
        self.imageleft=Label(frame5,image=self.photoleft)
        #self.imageLabel.place(x=2,y=60)
        self.imageleft.place(x=320)
        
        self.textArea=Text(frame4,font=('times new roman',15,'bold'),state='normal')
        self.textArea.place(x=3,y=58,width=434,height=466)
        
        Buttonframe=Frame(self.root,relief=RIDGE,borderwidth=5,background='#5e4fa2')
        Buttonframe.place(x=3,y=626,width=1510,height=67)
        
        self.Total=Button(Buttonframe,background='#bfff00',text='Total',width=15,height=2,font=('arial',12,'bold'),command=lambda:[self.changeOnHover(),self.total()])
        self.Total.grid(row=0,column=0,padx=150,pady=2)
        
        #entry Totalbill
        self.Totalbill=StringVar()
        self.TotalNameEntry=ttk.Entry(Buttonframe,font=("times new roman",15,'bold'),justify='center',textvariable=self.Totalbill)
        self.TotalNameEntry.place(x=350,y=3,width=150,height=50)
        
        #button for reset
        self.Reset=Button(Buttonframe,background='#bfff00',command=lambda:[self.changeOnHover(),self.resetItem()],text='Reset',width=15,height=2,font=('arial',12,'bold'))
        self.Reset.place(x=545,y=2)
        
        #button for update
        self.Reciept=Button(Buttonframe,background='#bfff00',command=lambda:[self.changeOnHover(),self.billArea()],text='Reciept',width=15,height=2,font=('arial',12,'bold'))
        self.Reciept.place(x=750,y=2)
        
        #button for Print
        self.Print=Button(Buttonframe,background='#bfff00',command=lambda:[self.changeOnHover(),self.printBill()],text='Print',width=15,height=2,font=('arial',12,'bold'))
        self.Print.place(x=950,y=2)
    
    def changeOnHover(self):
        self.Total.bind("<Enter>",func=lambda e:self.Total.config(background='red'))  
        self.Total.bind("<Leave>",func=lambda e:self.Total.config(background='#bfff00')) 
        self.Reset.bind("<Enter>",func=lambda e:self.Reset.config(background='red'))  
        self.Reset.bind("<Leave>",func=lambda e:self.Reset.config(background='#bfff00')) 
        self.Print.bind("<Enter>",func=lambda e:self.Print.config(background='red'))  
        self.Print.bind("<Leave>",func=lambda e:self.Print.config(background='#bfff00')) 
        self.Reciept.bind("<Enter>",func=lambda e:self.Reciept.config(background='red'))  
        self.Reciept.bind("<Leave>",func=lambda e:self.Reciept.config(background='#bfff00'))  
    def printBill(self):
        if self.textArea.get(1.0,END)=='\n':
            messagebox.showerror('Error',"Bill is Empty")
        else:
            file=tempfile.mktemp('.txt')
            open(file,'w').write(self.textArea.get(1.0,END))
            os.startfile(file,'print')
            
    def total(self):
        self.cap=int(self.var_cappuccino.get())*50
        self.mocha=int(self.var_Mocha.get())*30
        self.lrish=int(self.var_Lrish.get())*30
        self.latte=int(self.var_Latte.get())*70
        self.iced=int(self.var_Iecd.get())*45
        self.latteM=int(self.var_LatteMa.get())*100
        self.chiffon=int(self.var_Chiifon.get())*150
        self.sponge=int(self.var_sponge.get())*130
        self.van=int(self.var_vanilla.get())*200
        self.cocount=int(self.var_coconut.get())*70
        self.cupcake=int(self.var_cupcake.get())*80
        self.black=int(self.var_black.get())*350
        self.totalPrice= self.cap+self.mocha+self.lrish+self.latte+self.iced+self.latteM+self.chiffon+self.sponge+self.van+self.cocount+self.cupcake+self.black
        sum=str(self.totalPrice)
        if(sum!='0'):
            self.Totalbill.set(sum)

    def billArea(self):
        self.total()
        self.textArea.delete(1.0,END)
        self.textArea.insert(END,' \t ***Welcome Customer***')
        self.textArea.insert(END,' \n=======================================')
        self.textArea.insert(END,'\nProduct\t\tQuantity\t\tPrice')
        self.textArea.insert(END,' \n=======================================')
        
        if self.var_cappuccino.get()!='0':
            name="Cappuccino"
            self.textArea.insert(END,'\n{}\t\t {}\t\t{}Rs'.format(name,self.var_cappuccino.get(),self.cap))
            
        if self.var_Mocha.get()!='0':
            name="Mocha"
            self.textArea.insert(END,'\n{}\t\t {}\t\t{}Rs'.format(name,self.var_Mocha.get(),self.mocha))    
        
        if self.var_Lrish.get()!='0':
            name="Lrish"
            self.textArea.insert(END,'\n{}\t\t {}\t\t{}Rs'.format(name,self.var_Lrish.get(),self.lrish))
            
        if self.var_Latte.get()!='0':
            name="Latte"
            self.textArea.insert(END,'\n{}\t\t {}\t\t{}Rs'.format(name,self.var_Latte.get(),self.latte))
            
            
        if self.var_Iecd.get()!='0':
            name="Iced"
            self.textArea.insert(END,'\n{}\t\t {}\t\t{}Rs'.format(name,self.var_Iecd.get(),self.iced))    
            
        if self.var_LatteMa.get()!='0':
            name="Latte Macchiato"
            self.textArea.insert(END,'\n{}\t\t {}\t\t{}Rs'.format(name,self.var_LatteMa.get(),self.latteM))
            
        if self.var_Chiifon.get()!='0':
            name="Chiffon"
            self.textArea.insert(END,'\n{}\t\t {}\t\t{}Rs'.format(name,self.var_Chiifon.get(),self.chiffon))
        
        if self.var_sponge.get()!='0':
            name="Sponge"
            self.textArea.insert(END,'\n{}\t\t {}\t\t{}Rs'.format(name,self.var_sponge.get(),self.sponge))
        
        if self.var_vanilla.get()!='0':
            name="Vanilla-Bundt"
            self.textArea.insert(END,'\n{}\t\t {}\t\t{}Rs'.format(name,self.var_vanilla.get(),self.van))
        
        if self.var_coconut.get()!='0':
            name="Coconut"
            self.textArea.insert(END,'\n{}\t\t {}\t\t{}Rs'.format(name,self.var_coconut.get(),self.cocount))
        
        if self.var_cupcake.get()!='0':
            name="Cupcake"
            self.textArea.insert(END,'\n{}\t\t {}\t\t{}Rs'.format(name,self.var_cupcake.get(),self.cupcake))
        
        if self.var_black.get()!='0':
            name="Black-Forest-Gateau"
            self.textArea.insert(END,'\n{}\t\t {}\t\t{}Rs'.format(name,self.var_black.get(),self.black))
        
        self.textArea.insert(END,' \n=======================================')
        self.textArea.insert(END,' \nTotal Price::\t\t\t\t{}Rs'.format(self.totalPrice))
        self.textArea.insert(END,' \n=======================================')   
         
    def resetItem(self):
        self.var_cappuccino.set('0')
        self.var_Mocha.set('0')
        self.var_Lrish.set('0')
        self.var_Latte.set('0')
        self.var_Iecd.set('0')
        self.var_LatteMa.set('0')
        self.var_Chiifon.set('0')
        self.var_sponge.set('0')
        self.var_vanilla.set('0')
        self.var_coconut.set('0')
        self.var_cupcake.set('0')
        self.var_black.set('0')
        self.textArea.delete(1.0,END)
        self.TotalNameEntry.delete(0,END)
   
           
root=Tk()
root.configure(background='blue')
obj=CafeManagement(root)
a=obj.total()
def displayTime():
            time_string=strftime( '%I:%M:%S %p ')
            timeDisplay.config(text=time_string)
            timeDisplay.after(1000,displayTime) 
timeDisplay=Label(root,font=("roboto",25,'bold'),background='yellow')
timeDisplay.place(x=13,y=13)
displayTime()
root.mainloop()    