import json

def register(is_user):
    print("please enter username")
    username = input()
    print("please enter password")
    password = input()

    if is_user:
        file_name = 'json_files/user_registration_details.json'
    else:
        file_name = 'json_files/admin_registration_details.json'

    with open(file_name,'r+') as file_handler:
        user_details_dict = json.load(file_handler)
        if user_details_dict.get(username):
            print("choose different username")
        user_details_dict[username]=password
        file_handler.seek(0)
        json.dump(user_details_dict,file_handler)


def login(is_user):
    print("please enter username")
    username = input()
    print("please enter password")
    password = input()

    if is_user:
        file_name = 'json_files/user_registration_details.json'
    else:
        file_name = 'json_files/admin_registration_details.json'

    
    with open(file_name,'r') as file_handler:
        details_dict = json.load(file_handler)
        file_password = details_dict.get(username)

        if file_password==password:
            return True
        else:
            return False