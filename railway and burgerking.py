# #RAILWAY TICKET BOOKING SYSTEM
# print("Welcome to coderail railway booking system")
# final_ticket_price=0
# a=input("Enter your name:")
# print("Choose travel class:  1.First_class=1500 or 2.Second_class=1000 or 3.Sleepers_class=500")
# travel_class=int(input("Enter your choice(1/2/3):"))
# if travel_class==1:
#     final_ticket_price=1500
# elif travel_class==2:
#     final_ticket_price=1000
# elif travel_class==3:
#      final_ticket_price=500
# else:
#     print("Invalid Input")

# b=int(input("Enter your age:"))
# if b<5:
#     final_ticket_price=0
# elif b>60:
#     final_ticket_price= final_ticket_price*0.8
# else:
#     print(final_ticket_price)

# c=input("Do you want to add a meal?(Yes/No):")
# if c=="Yes":
#     final_ticket_price+=200

# print("Total price:",final_ticket_price)
       
#BURGER KING ORDER SYSTEM
print("Welcome to Burger King")
price=0
print('Menu: 1. Whopper Burger - ₹150, 2. Crispy Veg - ₹100, 3. Chicken Wings - ₹120')
a=int(input('Enter the item number(1/2/3):'))
if a==1:
    price=150
elif a==2:
    price=100
elif a==3:
    price=120
else:
    print("Invalid Input")

b=int(input("Enter the quantity:"))
price=price*b

c=input("Do you have a coupon code?(yes/no):")
if c=='yes':
    d=input('Enter your coupon code:')
    if d=='KING50':
        price=price*0.5
    elif d=='BK20':
        price-=20
    else:
        print("No discount")

else:
    print('No discount')

print('Final price:',price)
print('Thanks for ordering at Burger King')