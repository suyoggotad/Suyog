import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.font as font
import os
import dbconnect
from tkinter import messagebox as msg 
win=tk.Tk()
win.title('Income tax calculator')
win.configure(bg='#ffdab3')
# *****************************************personal********************************************************
# frames
# main
personalframe=ttk.LabelFrame(win,text='Personal information and the date of electronics transmission')
personalframe.grid(row=1,rowspan=10,column=0,padx=15,pady=10)
# bank frame
bank_frame=ttk.LabelFrame(win, text='Enter your bank details below ')
bank_frame.grid(row=11, column=0, padx=10, pady=10)
# address
addressframe=ttk.LabelFrame(personalframe,text='Fill your address details ')
addressframe.grid(row=3,columnspan=4,padx=30,pady=30)
# income frame
incomeframe=ttk.LabelFrame(win, text='Income details')
incomeframe.grid(row=1,rowspan=8,column=1,columnspan=12,padx=10,pady=10)
# income rate frame
irateframe=ttk.LabelFrame(win, text =' Income sources with tax deduction')
irateframe.grid(row=10,column=1,columnspan=12,padx=1,pady=1,sticky=tk.W)
# 
# # bank labels 

acc_no=ttk.Label(bank_frame, text='Enter your account number: ', font=('arial', 14, 'bold'))
acc_no.grid(row=0, column=0, padx=10, sticky=tk.W)

ifsc=ttk.Label(bank_frame, text='Enter your bank ifsc code: ', font=('arial', 14, 'bold'))
ifsc.grid(row=1, column=0, padx=10, sticky=tk.W)

branch=ttk.Label(bank_frame, text='Enter your bank brank name/id: ', font=('arial', 14, 'bold'))
branch.grid(row=2, column=0, padx=10, sticky=tk.W)

ac=tk.StringVar()

ac_Entry=ttk.Entry(bank_frame, width=19, textvariable=ac)
ac_Entry.grid(row=0, column=1, padx=10, pady=10)
ac_Entry.focus()

ifs=tk.StringVar()

ifsc_entry=ttk.Entry(bank_frame, width=19, textvariable=ifs)
ifsc_entry.grid(row=1, column=1, padx=10, pady=10)
br=tk.StringVar()
bra_entry=ttk.Entry(bank_frame, width=19, textvariable=br)
bra_entry.grid(row=2, column=1, padx=10, pady=10)

# label____________________________________________________________--------

name=ttk.Label(personalframe, text='Enter your full name: ',font=('Helvetica',14,'bold'))
name.grid(row=0,column=0,padx=5,pady=2,sticky=tk.W)

gender=ttk.Label(personalframe, text='Select your gender: ',font=('Helvetica',14,'bold'))
gender.grid(row=1,column=0, padx=5, pady=2, sticky=tk.W)

type_var=tk.StringVar()
gender_radio=ttk.Radiobutton(personalframe, text='Male',value='Male', variable=type_var)
gender_radio.grid(row=1, column=1,sticky=tk.W)

gender_radio=ttk.Radiobutton(personalframe, text='Female',value='Female', variable=type_var)
gender_radio.grid(row=1, column=2, sticky=tk.W)

gender_radio=ttk.Radiobutton(personalframe, text='Other',value='Other', variable=type_var)
gender_radio.grid(row=1 ,column=3, sticky=tk.W)



pan=ttk.Label(personalframe,text='Enter your pan id: ',font=('Helvetica',14,'bold'))
pan.grid(row=2,column=0,padx=5, pady=2,sticky=tk.W)

addresslabel=['Flat/House No.: ','Name of house/flat:', 'Area/Locality:','Town/City/District:','State:','Pin:']

for i in range(len(addresslabel)):
    alabel = 'label' + str(1)
    alabel=ttk.Label(addressframe,text=addresslabel[i],font=('Helvetica',14,'bold'))
    alabel.grid(row=i,column=0,sticky=tk.W,padx=30,pady=2)

# entry personal ________________________________________________________-----
name_var=tk.StringVar()
nameEntry=ttk.Entry(personalframe, width=30, textvariable=name_var)
nameEntry.grid(row=0,column=1,columnspan=3)
nameEntry.focus()

pan_var=tk.StringVar()
panEntry=ttk.Entry(personalframe, width =30 , textvariable=pan_var)
panEntry.grid(row=2 ,column=1,columnspan=3)

EntryBox={
    'fl':tk.StringVar(),
    'name': tk.StringVar(),
    'area': tk.StringVar(),
    'city': tk.StringVar(),
    'state': tk.StringVar(),
    'pin':tk.StringVar()
}
counter=0
for i in EntryBox:
    entry='entry' + i
    entry=ttk.Entry(addressframe, width=16,textvariable=EntryBox[i])
    entry.grid(row=counter,column=1)
    counter+=1

def add_db():
    addd=''
    for i in EntryBox:
        get='get' + i
        get=EntryBox[i].get()
        if get=='':
            pass
        else:
            addd+=get + ', '
    print(addd)
    insert='insert into addresss (address) values (%s)'
    data=(addd,)
    dbconnect.insert_data(insert,data)


# ############################################### bank details ##################

def bank():
    acc=ac.get()
    iff=ifs.get()
    branch_d=br.get()
    insert='insert into bank_info (Account_Number, IFSC_Code, Branch) values (%s,%s,%s)'
    data=(acc,iff,branch_d)
    dbconnect.insert_data(insert,data)
    
    

# bank_detail=ttk.Button(win, width=16, text='Bank details',command=bank)
# bank_detail.grid(row=17, column=0, padx=10, pady=10, sticky=tk.W)

# *************************************************** Income ***********************************
# year label
year=ttk.Label(win,text='Assessment year: ',font=('Helvetica',14,'bold'),background='#ffdab3')
year.grid(row=0,column=1,sticky=tk.W)

year_var=tk.StringVar()
y=ttk.Combobox(win,width=14,textvariable=year_var , state='readonly')
y['values']=('2019-20','2018-19','2017-18','2016-17','2015-16','2016-17')
y.current(0)
y.grid(row=0,column=3,padx=10,sticky=tk.W)

# income label
IncomeLabel=['Salary: ','House Property: ','Income from other sources: ','Profit from bussiness(enter profit only): ',
'Agricultural income: ']

for i in range(len(IncomeLabel)):
    label='label' + str(1)
    label=ttk.Label(incomeframe,text=IncomeLabel[i],font=('Helvetic',14,'bold'))
    label.grid(row=i, column=0,columnspan=3,sticky=tk.W,pady=2)

IncomeEntry={
    'salary': tk.StringVar(),
    'house': tk.StringVar(),
    'other': tk.StringVar(),
    'profit':tk.StringVar(),
    'agri':tk.StringVar()
}
counter=0
for i in IncomeEntry:
    Entry='entry' + i
    Entry=ttk.Entry(incomeframe,width=16,textvariable=IncomeEntry[i])
    Entry.grid(row=counter,column=4,pady=2)
    counter+=1

# --------------------------------- Total income ----------------------------------
   
res=Text(incomeframe,width=16,height='1',background='light grey')
res.grid(row=6,column=2)
# ***********************************income with rates **************************************

source=['Gain from rental property(30%): ','winnigs from lottery(20%): ', 'Capital gain(10%):']
for i in range(len(source)):
    s='s' + str(i)
    s=ttk.Label(irateframe,text=source[i],font=('Helvetica',14,'bold'))
    s.grid(row=i,column=0,padx=8,pady=2,sticky=tk.W)

# ****************sourceEntry  (****************)

rental=StringVar()
r=ttk.Entry(irateframe, width=16, textvariable=rental)
r.grid(row=0, column=1,padx=8, pady=2)

winnings=StringVar()
w=ttk.Entry(irateframe, width=16, textvariable=winnings)
w.grid(row=1, column=1, padx=8, pady=2)

capital=StringVar()
c=ttk.Entry(irateframe, width=16, textvariable=capital)
c.grid(row=2,column=1, padx=8,pady=2)
# ************************ text box ***************
p=Text(irateframe,width=14,height=1,background='light grey')
p.grid(row=0,column=2)

q=Text(irateframe,width=14,height=1,background='light grey')
q.grid(row=1,column=2)

r=Text(irateframe,width=14,height=1,background='light grey')
r.grid(row=2,column=2)
   
labell=ttk.Label(irateframe, text='Total')
labell.grid(row=3, column=0, sticky=tk.E)
inc=Text(irateframe, width=12, height=1, background='light pink')
inc.grid(row=3, column=1)
ii=Text(irateframe, width=14, height=1, background='light pink')
ii.grid(row=3, column=2)

totain=Text(win, width=16, height=1)
totain.grid(row=1, column=17)

netin_text=Text(win, width=16, height=1)
netin_text.grid(row=2, column=17)

total__Tax=Text(win, width=16, height=1)
total__Tax.grid(row=3, column=17)



def check():
    rent=rental.get()
    win=winnings.get()
    cap=capital.get()
    p.delete(0.0,'end')
    q.delete(0.0,'end')
    r.delete(0.0, 'end')
    inc.delete(0.0, 'end')
    ii.delete(0.0, 'end')
    totain.delete(0.0,'end')
    netin_text.delete(0.0,'end')
    total__Tax.delete(0.0,'end')
    total_tax=0.0
    total_income=0.0
    if rent=='':
        pass
    else:
        p_rate=float(rent)*0.3
        total_income+=float(rent)
        total_tax+=p_rate
        p.insert(END,p_rate)
    
    if win=='':
        pass
    else:
        q_rate= float(win)*0.2 
        total_tax+= q_rate
        total_income+=float(win)
        q.insert(END,q_rate)
        
    if cap=='':
        pass
    else:
        r_rate= float(cap)*0.1
        total_tax+= r_rate
        total_income+=float(cap)
        r.insert(END,r_rate)

   
    inc.insert(END, total_income)
    ii.insert(END, total_tax)

    
    result=0
    for i in IncomeEntry:
        Get='get' + i
        Get=IncomeEntry[i].get()
        if Get=='':
            pass
        else:
            result+=int(Get)

    res.delete(0.0,'end')   
    res.insert(END,result)

    final_Income=total_income+ result
    totain.insert(END, final_Income)

    netINc=final_Income- total_tax
    netin_text.insert(END, netINc)

    total__Tax.insert(END, total_tax)
    year_db=year_var.get()
    
    
    return year_db,final_Income,netINc, total_tax
    
def income_data():
    year_db,final_Income, netINc, total_tax=check()
    insert='insert into income_details (Year,Total_income, Net_income, Total_tax) values (%s,%s,%s,%s)'
    data=(year_db,final_Income,netINc, total_tax)
    dbconnect.insert_data(insert,data)

    


def personal():
  
    name_db=name_var.get()
    pan_db=pan_var.get()
    gender_db=type_var.get()
    # ****************************    personal  ***************
    insert_personal='insert into personal_info (name,pan,gender) values(%s,%s,%s)'
    data_personal=(name_db,pan_db, gender_db)
    dbconnect.insert_data(insert_personal,data_personal)
    # *****************************  address  ****************
    
def save():
    income_data()
    add_db()
    personal()
    bank()




##############################################################save$$$$$$$$$$$$$$$$$$$$$

myFont = font.Font(family='Courier', size=12, weight='bold')

save_button=Button(win, width=17, text='save',bg='#0052cc', fg='#ffffff', command=save)
save_button.grid(row=12, column=15, columnspan=3)
save_button['font']=myFont


# &&&&&&&&&&&&&&&&&&&&&&77  exit   (((((((((((((((((((((((()))))))))))))))))))))))) 


totalInc=ttk.Label(win, text='Total income: ',font=('arial',14,'bold'),background='#ffdab3')
totalInc.grid(row=1,column=16,sticky=tk.W)    

netIN=ttk.Label(win, text='Net income: ',font=('arial',14,'bold'),background='#ffdab3')
netIN.grid(row=2,column=16,sticky=tk.W) 

totalta=ttk.Label(win, text='Total tax: ',font=('arial',14,'bold'),background='#ffdab3')
totalta.grid(row=3,column=16,sticky=tk.W)    

final=Button(win, width=16, text='Calculate',bg='#59b300', fg='#ffffff', command=check)
final.grid(row=6,column=16)   
final['font']=myFont

# ************************************            display  ************************

def p_info():
    db_win=tk.Tk()
    db_win.title('personal information')
    get=code_var.get()
    disp_sql=f'select * from personal_info where client_id={get}'
    row=dbconnect.search_in_table(disp_sql)
    if row==False:
        msg.showinfo('info','No data found')
    else:
        lbl1 = Label(db_win, text=f"Client_ID: {row[0]}", font=('Arial', 14))
        lbl1.grid(row=0, column=1,sticky=tk.W)
        lbl2 = Label(db_win, text=f"Name: {row[1]}", font=('Arial', 14))
        lbl2.grid(row=1, column=1,sticky=tk.W)
        lbl3 = Label(db_win, text=f"Pan: {row[2]}", font=('Arial', 14))
        lbl3.grid(row=2, column=1,sticky=tk.W)
        lbl3 = Label(db_win, text=f"Gender: {row[3]}", font=('Arial', 14))
        lbl3.grid(row=3, column=1,sticky=tk.W)
        
    db_win.geometry('300x300')
    db_win.mainloop()

def ad_info():
    db_win=tk.Tk()
    db_win.title('personal information')
    get=code_var.get()
    disp_sql=f'select * from addresss where client_id={get}'
    row=dbconnect.search_in_table(disp_sql)
    if row==False:
        msg.showinfo('info','No data found')
        db_win.destroy()
    else:
        lbl1 = Label(db_win, text=f"Client_ID: {row[0]}", font=('Arial', 14))
        lbl1.grid(row=0, column=1,sticky=tk.W)
        lbl2 = Label(db_win, text=f"Address: {row[1]}", font=('Arial', 14))
        lbl2.grid(row=1, column=1,sticky=tk.W)

    db_win.geometry('700x200')
    db_win.mainloop()


def in_info():
    db_win=tk.Tk()
    db_win.title('personal information')
    get=code_var.get()
    disp_sql=f'select * from income_details where client_id={get}'
    row=dbconnect.search_in_table(disp_sql)
    if row==False:
        msg.showinfo('info','No data found')
        db_win.destroy()
    else:
        lbl1 = Label(db_win, text=f"Client_ID: {row[0]}", font=('Arial', 14))
        lbl1.grid(row=0, column=1,sticky=tk.W)
        lbl2 = Label(db_win, text=f"Year: {row[1]}", font=('Arial', 14))
        lbl2.grid(row=2, column=1,sticky=tk.W)
        lbl2 = Label(db_win, text=f"Total income : {row[2]}", font=('Arial', 14))
        lbl2.grid(row=4, column=1,sticky=tk.W)
        lbl2 = Label(db_win, text=f"Net income: {row[3]}", font=('Arial', 14))
        lbl2.grid(row=6, column=1,sticky=tk.W)
        lbl2 = Label(db_win, text=f"Total tax: {row[4]}", font=('Arial', 14))
        lbl2.grid(row=8, column=1,sticky=tk.W)
     
    db_win.geometry('300x300')
    db_win.mainloop()

def bn_info():
    db_win=tk.Tk()
    db_win.title('personal information')
    get=code_var.get()
    disp_sql=f'select * from bank_info where client_id={get}'
    row=dbconnect.search_in_table(disp_sql)
    if row==False:
        msg.showinfo('info','No data found')
        db_win.destroy()
    else:
        lbl1 = Label(db_win, text=f"Client_ID: {row[0]}", font=('Arial', 14))
        lbl1.grid(row=0, column=1,sticky=tk.W)
        lbl2 = Label(db_win, text=f"Account Number : {row[1]}", font=('Arial', 14))
        lbl2.grid(row=2, column=1,sticky=tk.W)
        lbl2 = Label(db_win, text=f"IFSC Code : {row[2]}", font=('Arial', 14))
        lbl2.grid(row=4, column=1,sticky=tk.W)
        lbl2 = Label(db_win, text=f"Branch : {row[3]}", font=('Arial', 14))
        lbl2.grid(row=6, column=1,sticky=tk.W)
       
    db_win.mainloop()

def view_clients():
    db_win=tk.Tk()
    db_win.title('personal information')
    get=code_var.get()
    sql_query=f'select client_id,name,gender from personal_info'
    row=dbconnect.view_all(sql_query)
    if row==False:
        msg.showinfo('info','No data found')
        db_win.destroy()
    else:
        # lbl1 = Label(db_win, text=f"{row[0]}", font=('Arial', 14))
        # lbl1.grid(row=0, column=1,sticky=tk.W,padx=5, pady=5)
        for i in range(len(dbconnect.view_all(sql_query))):
            lbl1 = Label(db_win, text=f"{row[i]}", font=('Arial', 14))
            lbl1.grid(row=i, column=1,sticky=tk.W,padx=5, pady=5)

        
    db_win.mainloop()


def exit():
    win.destroy()
    

clin_l=tk.Label(win, text='Enter the client code: ',font=('Helvetica',14,'bold'),background='#ffdab3')
clin_l.grid(row=11, column=10, sticky=tk.W)

code_var=StringVar()
code_entry=tk.Entry(win, width=16, textvariable=code_var)
code_entry.grid(row=11, column=11)

view_data=Button(win, text='View client',bg='#009999', fg='#ffffff', command=p_info)
view_data.grid(row=12,column=11)
view_data['font']=myFont

view_data=Button(win,width=12, text='View address',bg='#009999', fg='#ffffff', command=ad_info)
view_data.grid(row=12,column=10,padx=4)
view_data['font']=myFont

view_data=Button(win,width=12, text='View income',bg='#009999', fg='#ffffff', command=in_info)
view_data.grid(row=13,column=11,padx=4,pady=7)
view_data['font']=myFont

view_data=Button(win,width=12, text='View bank',bg='#009999', fg='#ffffff', command=bn_info)
view_data.grid(row=13,column=10,padx=4,pady=7)
view_data['font']=myFont

view_data=Button(win, text='View all clients',bg='#009999', fg='#ffffff', command=view_clients)
view_data.grid(row=15,column=10,pady=7)
view_data['font']=myFont

view_data=Button(win,width=12, text='exit',bg='#ff0000', fg='#ffffff', command=exit)
view_data.grid(row=18,column=15,columnspan=3)
view_data['font']=myFont


# ******************************************************** END **********************************************
dbconnect.create_tables()
win.geometry('1500x1500')
win.mainloop()