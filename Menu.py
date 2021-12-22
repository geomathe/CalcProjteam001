import add.py
import sub.py
import mul.py
import div.py   
print("Calculator")
while True:
    print("MENU")
    print("Press 1.Addition")
    print("Press 2.Subtraction")
    print("Press 3.Multiplication")
    print("Press 4.Division")
    print("Press 5.Exit")
    choice=int(input("Enter your choice"))
    if choice==1:
          x=int(input("Enter Number 1"))
          y=int(input("Enter Number 2"))
          add.add(x,y)
    elif choice==2:
          x=int(input("Enter Number 1"))
          y=int(input("Enter Number 2"))
          sub.subtract(x,y)
    elif choice==3:   
          x=int(input("Enter Number 1"))
          y=int(input("Enter Number 2"))
          mul.mul(x,y)
    elif choice==4:    
          x=int(input("Enter Number 1"))
          y=int(input("Enter Number 2"))
          div.div(x,y)
    elif choice==5:
          break
    else:
        print("Wrong choice")
