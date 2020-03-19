while True:
    try:
        var_1 = float(input("Introduceti prima variabila si apasati <enter>: "))
        break
    except ValueError:
        print("Caracterul(ele) introdus(e) nu este(sunt) un numar! Reintroduceti prima varialbila! ")
# def sterge():
#     if input() == "c":
#      var_1.replace(var_1[:-1], "")

while True:
    try:
        var_2 = str(input("Introduceti operatia, apoi apasati <enter>: "))
        var_2_list = ("+", "-", "/", "*", "**")
        if var_2 in var_2_list:
            break
    except ValueError:
        print("")

while True:
    try:
        var_3 = float(input("Introduceti a doua variabila si apasati <enter>: "))
        break
    except ValueError:
        print("Caracterul(ele) introdus(e) nu este(sunt) un numar! Reintroduceti a doua variabila: ")

while var_2 == "+":
    print(float(var_1) + float(var_3))
    break

while var_2 == "-":
    print(float(var_1) - float(var_3))
    break

while var_2 == "*":
    print(float(var_1) * float(var_3))
    break

while var_2 == "/":
    print(float(var_1) / float(var_3))
    break

while var_2 == "**":
    print(int(var_1) ** int(var_3))
    break

quit = input("Apasa tasta <enter> pentru a iesi! ")