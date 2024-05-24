name="asritha"
password="ashi123"
user_name=input("enter your name:")
passwords=input("enter your password:")
s="""
1.CREDIT
2.DEBIT
3.MINI STATEMENT
4.EXIT"""
amount=1000
if name==user_name and password==passwords:
    while True:
        print(s)
        option=int(input("select option:"))
        if option==1:
            credit_amount=float(input("enter the amout:"))
            print("amount after credit:",amount+credit_amount)
        elif option==2:
            debit_amount=float(input("enter the amount:"))
            print("amount after debit:",amount-debit_amount)
        elif option==3:
            print("amount:",amount)
        elif option==4:
            break
else:
    print("incorrect")



