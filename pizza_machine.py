#AHHYEE this one is my fav from my old projects.Imagine craving pizza and ordering it through a machine! This project is a code for a pizza machine where you can select your favorite pizza, choose toppings, and place your order. It's like having your own pizza vending machine

Bill = 0
print("Thank you for choosing Python Pizza Deliveries!")
size = str(input("enter size S, M ,L")) # What size pizza do you want? S, M, or L
if size == "s":
  print("you choose small size pizza")
  Bill=15
elif size == "m":
    print("you choose medium size pizza")
    Bill=20
else:
 print("you choose large size pizza")
 Bill=25

add_pepperoni = str(input("Do you want pepperoni? y or n"))
if add_pepperoni == "y":
 sizeof = input("which size of pizza do you have? type s for small and l for large and medium")
 if sizeof == "s":
   print("You choose yess and small pizza")
   Bill=Bill+2
 else:
    print("you choose yes and your pizza is large or medium")
    Bill=Bill+3
else:
  print("thank you next")
extra_cheese = str(input("Do you want extra cheese? y or n"))
if extra_cheese == "y":
  Bill=Bill+1
else:
    print("end")
print(f"your total bill is {Bill}")
