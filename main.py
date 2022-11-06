import tkinter as tk

window = tk.Tk() 

def main():
  global window
  window.destroy()
  window = tk.Tk()
  window.title("LogIn")
  window.geometry("300x300")
  nama = tk.Label(text="Username: ")
  nama.grid(row = 0, column = 0)
  global BoxNama
  BoxNama = tk.Entry()
  BoxNama.grid(row = 0, column = 1)
  passw = tk.Label(text="Password: ")
  passw.grid(row = 1, column =0)
  global BoxPassw
  BoxPassw = tk.Entry()
  BoxPassw.grid(row = 1, column = 1 )
  L_Check = tk.Button(text = "Log In", command = LogIn)
  L_Check.grid (row = 3, column = 0 )
  B_sign = tk.Button(text = "Click here to Sign Up", command = PSignUp)
  B_sign.grid (row = 4, column = 0 )

def PSignUp(): 
  global window
  window.destroy()
  window = tk.Tk()
  window.title("Sign Up New Account")
  window.geometry("300x300")
  nama = tk.Label(text="Username: ")
  nama.grid(row = 0, column = 0)
  global BoxNama
  BoxNama = tk.Entry()
  BoxNama.grid(row = 0, column = 1)
  global BoxPassw
  passw = tk.Label(text="Password: ")
  passw.grid(row = 1, column =0)
  BoxPassw = tk.Entry()
  BoxPassw.grid(row = 1, column = 1 )
  L_Check = tk.Button(text = "Sign Up", command = signin)
  L_Check.grid(row = 2, column = 0)

def P_Success(): 
  global window
  window.destroy()
  window = tk.Tk()
  window.title("success")
  window.geometry ("400x400")
  LogInOk= tk.Label(text="Log In Successful ")
  LogInOk.grid(row = 0, column = 0)
  L_Check = tk.Button(text = "Back to Home", command =  main)
  L_Check.grid(row = 1,column = 0)

def P_SignInSuccess(): 
  global window
  window.destroy()
  window = tk.Tk()
  window.title("success")
  window.geometry ("400x400")
  LogInOk= tk.Label(text="Sign Up Successful ")
  LogInOk.grid(row = 0, column = 0)
  L_Check = tk.Button(text = "Back to Home", command = main)
  L_Check.grid(row = 1,column = 0)

def LogIn(): 
  try:
    uname = BoxNama.get()
    passwo = BoxPassw.get()
    f = open(uname,'r')
    passw = f.read()
    passw = passw.split("\n")   
    if passw[0] == passwo: 
      P_Success()
    else: 
      Salah= tk.Label(text="Incorrect Password")
      Salah.grid(row = 5, column = 0)
    f.close()
  except FileNotFoundError: 
    SU = tk.Label(text="Please Sign Up")
    SU.grid(row = 5, column = 0)

def check(uname): 
  try: 
    f = open(uname,'x')
    f.close()
    return True
  except FileExistsError:
    return "Username taken"

def signin(): 
  uname = BoxNama.get()
  passwo = BoxPassw.get()
  if check(uname) == True:
    f = open(uname,'a')
    content = passwo+"\n"
    f.write(content)
    f.close()
    P_SignInSuccess()
  else:
    SU = tk.Label(text="Username taken, please change username")
    SU.place(x = 0,y = 70)

main()