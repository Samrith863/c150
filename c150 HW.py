from tkinter import *
import random 
root=Tk()
root.title("Lucky Friend Wheel")
root.geometry("400x400")
root.configure(background="blue")
country_label=Label(root)
capital_label=Label(root)
random_country=Label(root)
random_capital=Label(root)
country=Entry(root)
capital=Entry(root)
country_list=[]
capital_list=[]

def displayCC():
    country_name=country.get()
    country_list.append(country_name)
    country_label['text']="Your country List: "+str(country_list)
    capital_name=capital.get()
    capital_list.append(capital_name)
    capital_label['text']="Your capital List: "+str(capital_list)
    
    
    

def rCC():
    length=len(country_list)
    random_num=random.randint(0,length-1)
    random_country_name=country_list[random_num]
    random_country['text']=str(random_country_name)
    length1=len(capital_list)
    random_num1=random.randint(0,length1-1)
    random_capital_name=capital_list[random_num]
    random_capital['text']=str(random_capital_name)
  

btn1=Button(root,text="Display Capital and Country",bg="black",fg="white",command=displayCC)
btn1.place(relx=0.5,rely=0.3,anchor=CENTER)
btn=Button(root,text="Random Capital and Country",bg="black",fg="white",command=rCC)
btn.place(relx=0.5,rely=0.6,anchor=CENTER)
country_label.place(relx=0.5,rely=0.4,anchor=CENTER)
capital_label.place(relx=0.5,rely=0.5,anchor=CENTER)
random_capital.place(relx=0.5,rely=0.7,anchor=CENTER)
random_country.place(relx=0.5,rely=0.8,anchor=CENTER)
country.place(relx=0.5,rely=0.1,anchor=CENTER)
capital.place(relx=0.5,rely=0.2,anchor=CENTER)
root.mainloop()

