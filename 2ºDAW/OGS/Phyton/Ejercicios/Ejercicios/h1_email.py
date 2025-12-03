def email():
    email = input("Introduzca un email: ")
    if "@" in email:
        print("Email correcto")
    else:
        print("Email no correcto")
        