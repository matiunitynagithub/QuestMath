accounts = {}
while True:
    option = input("Wpisz 'Sign in' lub 'Log in' ")
    login = input("Login: ")
    password = input("Hasło: ")
    if option == "Sign in":
        accounts[login] = password
    elif option == "Log in":
        if accounts[login] == password:
            print("Zalogowany!")
            break
    else:
        print("Błąd, sprubój ponownie")
        continue

print("Pora na pytania:")
# pytanie pierwsze
pytaniea = input("Ile to 2*2? 'a' : 22 'b' : 4  ")
if pytaniea == "a":
    print("Źle odpowiedziałeś!!")
if pytaniea == "b":
    print("Dobrze odpowiedziałeś!!!")
# pytanie drugie
pytanieb = input("ile to 8*8? 'a' : 64 'b' : 88 ")
if pytanieb == "a":
    print("Dobrze odpowiedziałeś!!")
if pytanieb == "b":
    print("Źle odpowiedziałeś!!")
# pytanie ostatnie
pytaniec = input("ile to 20*2? 'a' : 202 'b' : 40 ")
if pytaniec == "a":
    print("Źle odpowiedziałeś!!")
if pytaniec == "b":
    print("Dobrze odpowiedziałeś!!")
