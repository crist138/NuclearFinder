import webbrowser

while True:
    print("1.- Buscar codigo nuclear")
    print("2.- Salir")
    option = int(input())
    if option == 1:    
        print("Ingresa el codigo nuclear: ")
        nuclear_code = int(input())

        webbrowser.open(
        'https://nhentai.net/g/',nuclear_code
        )
    else:
        break
