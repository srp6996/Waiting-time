'''
Application Created for predicting the waitng time in the bank
using Queuing Theory 
It is Prototype 
Queueing theory is the mathematical study of waiting lines, or queues.
 A queueing model is constructed so that queue lengths and waiting time can be predicted.
 Queueing theory is generally considered a branch of operations research
 because the results are often used when making business decisions about the resources needed to provide a service.

 
'''

from twilio.rest import Client
from tkinter import *
import os
import time
#import Authen
account_sid=('*****************************')
auth_token=(***************************)

client = Client(Authen.account_sid, Authen.auth_token)


mobile_number_deposit=[]
mobile_number_debit=[]
time =[]

def show_entry_fields():

    mobile_number_deposit=(e1.get())
    mobile_number_debit=(e2.get())
    try:
        if len(mobile_number_deposit) ==10:
            master.deposit +=1
            L['text'] = 'Token Number: ' + str(master.deposit)
            Length_Queue = master.deposit
            if Length_Queue < 5:
                if Length_Queue == 1:

                    T['text'] =  'Dear Customer Inital Waiting time is 3 mins at Counter no. 1'

                    message = client.messages \
                            .create(body="Dear Customer The  Initial Waiting time is 3 mins at Counter No. 1",from_='+12053786107',to='+91'+str(mobile_number_deposit))
                    print(message.sid)
                    
                elif Length_Queue > 1:
                    Inital_Time = 4 
                    #Ld = 1 / Inital_Time ##lambda is 1/4 
                    Waiting_Time = (Length_Queue) * (Inital_Time)
                    wait = "Dear Customer the waiting time is  " 
                    T['text'] = str(wait) + str(Waiting_Time) + 'mins at Counter no. 1'
                    message = client.messages \
                            .create(body=str(wait)+str(Waiting_Time)+"mins at Counter No. 1",from_='+12053786107',to='+91'+str(mobile_number_deposit))
                    print(message.sid)
                    #print (wait)
                    #message = client.messages.create(body=wait+str(Waiting_Time),from_='+12053786107 ',to='+91' + str(mobile_number_debit))
                else:
                    wait = "Time Over"

                
            else:
                wait="Time is over today "
                T['text'] = str(wait)
                message = client.messages \
                        .create(body=str(wait),from_='+12053786107',to='+91'+str(mobile_number_deposit))
                print(message.sid)
                #message = client.messages.create(body=wait,from_='+12053786107',to='+91' + str(mobile_number_deposit))

                #print (wait)
            

        elif len(mobile_number_debit)==10:
            master.debit += 1
            L['text'] = 'Token Number: ' + str(master.debit)
            Length_Queue = master.debit
            if Length_Queue < 5:
                if Length_Queue == 1:
                    T['text'] =  'Dear Customer Inital Waiting time is 5 mins at Counter No. 2'

                    message = client.messages \
                            .create(body="Dear Customer The Initial Waiting time is 5 mins at Counter No. 2",from_='+12053786107',to='+91'+str(mobile_number_debit))
                    print(message.sid)

                
                elif Length_Queue > 1:
                    Inital_Time = 7 
                    #Ld = 1 / Inital_Time ##lambda is 1/7 
                    Waiting_Time = (Length_Queue) * (Inital_Time)
                    wait = "Dear Customer the waiting time is  "
                    T['text'] = str(wait) + str(Waiting_Time) + 'mins at Counter no. 2' 
                    message = client.messages \
                            .create(body=str(wait)+str(Waiting_Time)+"mins at Counter No. 2",from_='+12053786107',to= '+91'+str(mobile_number_debit))
                    print(message.sid)
                    #print (wait)
                    #message = client.messages.create(body=wait+str(Waiting_Time),from_='+12053786107 ',to='+91' + str(mobile_number_debit))
                else:
                    wait = "Time Over"
                            
            
            else:
                wait="Time is over today "
                T['text'] = str(wait)
                message = client.messages \
                    .create(body=str(wait),from_='+12053786107',to= '+91'+str(mobile_number_debit))
                print(message.sid)
                
                # message = client.messages.create(body=wait,from_='+12053786107',to='+91' + str(mobile_number_deposit))
                #print (wait)

            

        elif len(mobile_number_debit) < 10 and len(mobile_number_deposit) < 10:
            T['text'] = 'Enter the Mobile Number correctly'
        

        else:
            L['text'] = 'Enter the Mobile Number For Token'
        
           
    except:
        pass


def earse():
    e1.delete(0,END)
    e2.delete(0,END)




if __name__ == "__main__":
    master = Tk()
    master.title("Tokens")
    master.geometry("900x650")
    master.configure(background ="lightgray")

    master.deposit = 0
    master.debit = 0
    Button(master, text="Next",width=50,height=2,command=earse).grid(row=7, column=1, sticky=W,padx=20, pady = 20)

    Label(master, text="Mobile num without +91 For Deposit:",width=30,height=1,font=("", 10)).grid(row=0,padx=20, pady = 20)
    e1 = Entry(master,width=30,font=("", 15))
    e1.grid(row=0, column=1,padx=20, pady = 20)
    Label(master, text="Mobile num without +91 For Debit:",width=30,height=1,font=("", 10)).grid(row=1,padx=20, pady = 20)
    e2 = Entry(master,width=30,font=("", 15))
    e2.grid(row=1, column=1,padx=20, pady = 20)


    

    Button(master, text="Press",width=50,height=2,command=show_entry_fields).grid(row=2, column=1, sticky=W,padx=20, pady = 20)
    B = Label(master, text="  Bank of India      ",width=50,height=2,bg="gray",fg="black")
    B.grid(row=3, column=1,padx=20, pady = 20)
    W = Label(master, text="    Welcomes You    ",width=50,height=2,bg="gray",fg="black")
    W.grid(row=4, column=1,padx=20, pady = 20)

    L = Label(master, text="         ",width=50,bg="lightgray",fg="red")
    L.grid(row=5, column=1,padx=20, pady = 20)
    T = Label(master,text="         ",width=50,bg="lightgray",fg="brown")
    T.grid(row=6, column=1,padx=20, pady = 20)
        
    master.mainloop( )


