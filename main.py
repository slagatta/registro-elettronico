print("\n░█▀▄░█▀▀░█▀▀░▀█▀░█▀▀░▀█▀░█▀▄░█▀█░░░█▀▀░█░░░█▀▀░▀█▀░▀█▀░█▀▄░█▀█░█▀█░▀█▀░█▀▀░█▀█\n"
      "░█▀▄░█▀▀░█░█░░█░░▀▀█░░█░░█▀▄░█░█░░░█▀▀░█░░░█▀▀░░█░░░█░░█▀▄░█░█░█░█░░█░░█░░░█░█\n"
      "░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░░▀░░▀░▀░▀▀▀░░░▀▀▀░▀▀▀░▀▀▀░░▀░░░▀░░▀░▀░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀▀\n")

registro = {} #dovrà contenere come chiave i nomi e come valori i voti per ciascun nome
print("- premi 1 per inserire nomi al registro: ")
print("- premi 2 per inserire i voti: ")
print("- premi 3 per stampare il registro: ")
print("- premi 4 per uscire: ")

while True:
    scelta = input("\nInserisci scelta: ")
    if scelta == "4":
        print("mi mancherai")
        break
    elif scelta == "1":
        nome = input("Inserisci il nome: ")
        registro.update({nome: []})
    elif scelta == "2":
        nome = input("Inserisci nome dell'alunno: ")
        if nome not in registro:
            print("Nome non presente\n")
            continue
        else:
            voto = eval(input("Inserisci il voto: "))
            registro[nome].append(voto)
    elif scelta == "3":
        print(registro)
