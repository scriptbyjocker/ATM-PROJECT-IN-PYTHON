import mysql.connector,datetime
def data_insert(name,password):
            amount=int(input("\nEnter Your Amount : "))
            user_acc =mysql.connector.connect(
            host="localhost",
            user="root",
            password="vijaykavi",
            database="atm"
           )
            mycursor=user_acc.cursor()
            current_time = datetime.datetime.now()
            print (current_time)
            data_insert="insert into user_acc(Name,Password,deposit_amount,register_date) value(%s,%s,%s,%s)"
            data=(name,password,amount,current_time)
            mycursor.execute(data_insert,data)
            user_acc.commit()
            print("Account Create Successful!")
def data_view(name,password):
            user_acc =mysql.connector.connect(
            host="localhost",
            user="root",
            password="vijaykavi",
            database="atm"
           )
            mycursor=user_acc.cursor()
            mycursor.execute(f"select * from user_acc where name='{name}' and password='{password}'")
            show=mycursor.fetchall()

            if show !=[]:
                u_n=show[0]
                user_name=u_n[0]
                old=u_n[2]
                old_withdraw=u_n[3]
                print("\n Login SuccessFul!")
                select=int(input("\n 1. show Balance  \n 2. Deposit \n 3. withdraw   \n"))
                if select == 1:
                    print(f"current Balance is {old}")
                elif select == 2:
                   how=int(input("\n How much You Want to Deposit : "))
                   new=how+old
                   deposit(new,old,name)
                elif select == 3:
                    how=int(input("\n How much You Want to Withdraw : "))
                    new=old-how
                    old_with=old_withdraw+how
                    if how > old:
                        print(f"Available balance is {old}")

                        
                    else:
                        withdraw(new,name,old_with)
            else:
                print(" \n User Not Present")
def deposit(new,old,name):
            user_acc=mysql.connector.connect(
            host="localhost",
            user="root",
            password="vijaykavi",
            database="atm"
           )
            mycursor=user_acc.cursor()
            mycursor.execute(f"update user_acc set deposit_amount='{new}' where name='{name}'")
            user_acc.commit()
            show=mycursor.fetchall()
def withdraw(new,name,old_with):
            user_acc=mysql.connector.connect(
            host="localhost",
            user="root",
            password="vijaykavi",
            database="atm"
           )
            mycursor=user_acc.cursor()
            update_deposit=f"update user_acc set deposit_amount='{new}' where name='{name}'"
            update_withdraw=f"update user_acc set withdraw='{old_with}' where name='{name}'"
            mycursor.execute(update_deposit)
            user_acc.commit()
            mycursor=user_acc.cursor()
            mycursor.execute(update_withdraw)
            user_acc.commit()
            show=mycursor.fetchall()
           
def data_search():
            name=input("\n Enter Your Name: ")
            password=input("\n Enter Your Password: ")
            user_acc=mysql.connector.connect(
            host="localhost",
            user="root",
            password="vijaykavi",
            database="atm"
           )
            mycursor=user_acc.cursor()
            mycursor.execute(f"select * from user_acc where name='{name}' and password='{password}'")
            show=mycursor.fetchall()
            if show !=[]:
                u_n=show[0]
                user_name=u_n[0]
                user_pass=u_n[1]
                user_deposit=u_n[2]
                user_withdraw=u_n[3]
                print(f" \nName = {user_name} \n Balance = {user_deposit} \nWithdraw = {user_withdraw}")
            else:
                print("User NOt Present\n ")

def out():
    print("\nHello Welcome To KVB Bank")
    admin=int(input("\n 1.Create Account  \n 2.Login Your Account  \n " ))
    if admin == 1:
        name=input("\nEnter Your Name: ")
        password=input("\nEnter Your Password: ")
        data_insert(name,password)

    elif admin ==2:
       name=input("\nEnter Your Name: ")
       password=input("\nEnter Your Password: ")
       data_view(name,password)


out()




