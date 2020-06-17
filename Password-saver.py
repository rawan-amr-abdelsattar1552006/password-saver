from tkinter import *
import os

root = Tk()
root.title("Password saver")
root.iconbitmap("my icon.ico")

# Some kind of function

def submit():
    global username
    global myPassword
    global myAccount
    username = nameEnt.get()
    myPassword = passEnt.get()
    myAccount = accountEnt.get()
    if username == '' or myPassword == '' or myAccount == '' :
        warning = Label(myFrame , text = "You can't leave any EMPTY fields !!" , fg = 'red')
        warning.grid(row = 7 , column = 0, pady = 10)

    else:
        myFile = open("passwords.txt" , "a")
        myFile.write( 'Account site : \n'+ myAccount +'\nUsername or email : \n'+ username + '\nPassword : \n'+ myPassword + '\n' + '\n')
        nameEnt.delete(0 , END)
        passEnt.delete(0 , END)
        accountEnt.delete(0 , END)
        myFile.close()

    
def SP_btn():
    os.startfile("passwords.txt") 
    

# Creating widgets 
myFrame = LabelFrame(root , padx = 20 , pady = 20)

nameLabel = Label(myFrame , text = "Username or email", padx = 10 , pady = 10 )
passLabel = Label(myFrame , text = "Password" , padx = 10 , pady = 10 )
accountLabel = Label(myFrame , text = "Account site" , padx = 10 , pady = 10 )
nameEnt = Entry(myFrame , width = 80 )
passEnt = Entry(myFrame, width = 80)
accountEnt = Entry(myFrame , width = 80)
S_btn = Button(myFrame, text = "Submit" , padx = 10 , pady = 10 , command = submit )
S_pass_btn = Button(myFrame, text = "Saved passwords" , padx = 10 , pady = 10 , command = SP_btn)





                     
# Showing things on the screen
myFrame.pack(padx = 15 , pady = 15)

nameLabel.grid(row = 1 , column = 0 , columnspan = 2)
nameEnt.grid(row = 2 , column = 0  ,columnspan = 2)
passLabel.grid(row = 3 , column = 0, columnspan = 2)
passEnt.grid(row = 4 , column = 0, columnspan = 2)
S_btn.grid(row = 8 , column = 0 , padx = 10 , pady = 10)
accountLabel.grid(row = 5 , column = 0, columnspan = 2)
accountEnt.grid(row = 6 , column = 0)
S_pass_btn.grid(row = 9 , column = 0 , padx = 10 , pady = 10)


root.mainloop()




                     


