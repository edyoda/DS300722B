from login_register import register,login



def get_prompt():
    user_or_admin = """1. Users\n2. Admin\n"""
    print(user_or_admin)
    choice = int(input())
    if choice==1:
        # User part
        display = """1.Register\n2.Login\n"""
        print(display)
        choice = int(input())
        if choice==1:
            output = register(True) 
            if output:
                print("registered successfully")
        elif choice==2:
            output = login(True)
            if output:
                display = """1.Show Menu\n2.Order Food\n3.Order History"""
                print(display)
                user_input = int(input())
                print(user_input)
            else:
                print("login failure")




    elif choice==2:
        display = """1.Register\n2.Login\n"""
        print(display)

        choice = int(input())
        if choice==1:
            output = register(False)
            if output:
                print("registered successully")
            else:
                print("registration failure")
        elif choice==2:
            output = login(False)
            if output:
                display = """1.Add Menu Items\n2.User Details"""
                print(display)
                admin_input= int(input())  
                print(admin_input)  
            else:
                print("Login failure")
    else:
        print("Invalid choice")

    


if __name__=="__main__":
    get_prompt()




