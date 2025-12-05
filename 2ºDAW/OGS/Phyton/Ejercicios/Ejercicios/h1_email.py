def validar_email(email):
    if "@" in email:
        return "Email correcto"
    else:
        return "Email no correcto"

email = input("Introduzca un email: ")
print(validar_email(email))