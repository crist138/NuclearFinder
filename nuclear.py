import webbrowser
from colorama import init, Fore, Back, Style
from urllib.parse import urlparse
import os



import random

nuclear_codes = [20667,6929,5275,18507,52262]


while True:
    print("2.- Salir")
    option = int(input())
   
  
    init()
    print(Fore.RED+"""
          
        ███╗░░██╗██╗░░░██╗░█████╗░██╗░░░░░███████╗░█████╗░██████╗░███████╗██╗███╗░░██╗██████╗░███████╗██████╗░
        ████╗░██║██║░░░██║██╔══██╗██║░░░░░██╔════╝██╔══██╗██╔══██╗██╔════╝██║████╗░██║██╔══██╗██╔════╝██╔══██╗
        ██╔██╗██║██║░░░██║██║░░╚═╝██║░░░░░█████╗░░███████║██████╔╝█████╗░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝
        ██║╚████║██║░░░██║██║░░██╗██║░░░░░██╔══╝░░██╔══██║██╔══██╗██╔══╝░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗
        ██║░╚███║╚██████╔╝╚█████╔╝███████╗███████╗██║░░██║██║░░██║██║░░░░░██║██║░╚███║██████╔╝███████╗██║░░██║
        ╚═╝░░╚══╝░╚═════╝░░╚════╝░╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝
          """)
    
    print(Fore.GREEN+"1.- Buscar codigo nuclear")
    print(Fore.BLUE+"2.- Busqueda random")
    print(Fore.GREEN+"3.- Salir")
    option = int(input(":"))
    if option == 1:    
        print("Ingresa el codigo nuclear: ")
        nuclear_code = int(input())
       
      
        webbrowser.open("https://nhentai.net/g/"+str(nuclear_code))
        os.system("cls")
        
    elif option == 2:
        random.shuffle(nuclear_codes)
        
        webbrowser.open('https://nhentai.net/g/'+str(nuclear_codes[0]))
        os.system("cls")
        1
    elif option == 3:
        break
