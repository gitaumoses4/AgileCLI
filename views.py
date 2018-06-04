from models import User, Moderator, Admin
print("Agile Group Project")
print("********************")

#User can signup or login
print("Choose one of the options below by entering 1 or 2")
print("1. Login")
print("2. Signup")
choice = input("I want to: ")
if choice == '1':
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = User.login(username=username, password=password)
elif choice == '2':
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = User.login(username=username, password=password)
else:
    print("Please enter a valid choice")

#User can view and edit own comments if login successful
if user.role is user:
    print("Do you want to view your comments or edit your comment")
    print("[[A or a]. Add comment]")
    print("[[E or e]. Edit comment]")
    print("[V or v]. View comment")
    print("2. Edit comment")

    if user_choice == 'a' or user_choice == 'd':
        new_comment = input("Enter new comment: ")
    elif user_choice == 'E' or user_choice == 'e':
        #Show all comments
        comm_choice =input("Choose comment you want to edit")
        new_comment = input("Enter new comment: ")
        #Edit comment where comment_id == comm_choice
    elif user_choice == 'v' or user_choice == 'v':
        #Show all comments
        pass
    else:
        print("Enter a valid choice")

#Moderator can edit own comment and delete any comment
if user.role is moderator:
    print("Do you want to view all comments, edit your comment or delete a comment")
    print("[[A or a]. Add comment]")
    print("[V or v]. View comments")
    print("[E or e]. Edit your comment")
    print("[D or d]. Delete a comment")
    if user_choice == 'a' or user_choice == 'd':
        new_comment = input("Enter new comment: ")
    elif mod_choice == 'V' or mod_choice == 'v':
        #Show all comments
        
    elif mod_choice == 'E' or mod_choice == 'e':
        if comment_created_by == moderator_username:
            #view list of own comments
            mod_choice = input("Enter comment you want to edit: ")
            comment = input("Enter new comment: ")
            #update comment on table where comment id == mod_choice
    elif mod_choice == 'D' or mod_choice == 'd':
        #view all comments
        mod_choice = input("Enter comment you want to delete: ")
        #delete comment
    else:
        print("Enter a valid choice")
     


if user.role is admin:
    #view all comments
    print("Do you want to edit or delete a comment")
    print("[E or e]. Edit your comment")
    print("[D or d]. Delete a comment")
    adm_choice = input("Enter choice: ")
    if adm_choice == 'D' or adm_choice == "d":
        comm_choice = input("Enter comment you wish to delete: ")
        #Delete comment where comm_choice == comment_id
    elif adm_choice == 'E' or adm_choice == 'e':
        comm_choice = input("Enter comment you want to edit: ")
        new_message = input("Enter new comment: ")
    else:
        print("Enter a valid choice")