import os
usuario = "Sbleit"

colores = {
    "1": "\033[91m",
    "2": "\033[92m",
    "3": "\033[93m",
    "4": "\033[94m",
    "5": "\033[95m",
    "6": "\033[96m",
    "reset": "\033[0m"
}
# 30 negro
def cambiar_color(indice,texto):
    print(colores[indice] + texto + colores["reset"])

while True:
    # \033[42m Tu usuario\033[0m"
    # Directorio de Trabajo Actual | Current Working Directory
    # "\033[42m\033[30m Tu usuario \033[0m")
    # "\033[96m{usuario}\033[95m on 📁 {os.getcwd()}\033[0m\033[96m\n>> \033[0m\033[0m"
    comando = input(f"\033[42m\033[30m{usuario} >>\033[0m").lower().strip()

    if( comando.startswith("color") and len(comando.split(" ")) >= 3):
        # hola me llamo rodrigo palacios
        _,indice,texto = comando.split(" ",2)
        cambiar_color(indice,texto)
        continue
    if(comando == "clear"):
        os.system('cls')
        continue
    if(comando == "help"):
        print("Lista de comandos.")
        print("  - color <indice> <texto> : Comando que permite modificar el color del texto mostrado por consola")
        print("  - clear : Limpia la consola.")
        continue
    if(comando == "cls" or comando.startswith("cle") or comando == "klear"):
        print("¿Quisiste usar el comando 'clear' ?")
    if(comando.startswith("hel") or comando.startswith("he") or comando.startswith("jelp")):
        print("¿Quisiste usar el comando 'help' ?")
    # "col", "kolor" o "colo"
    if( comando.startswith("col") or comando.startswith("kolor") or comando.endswith("lor")):
        print("¿Quisiste usar el comando 'color <indice> <texto>'  ?")
    if(comando not in ["color","clear","help"]):
        print("Comando desconocido.")
