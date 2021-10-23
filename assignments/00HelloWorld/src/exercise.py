from matplotlib import pyplot as plt

def graficar():
    #Código de la gráfica
    with open('/workspace/evidencia-integrador-/assignments/00CuentaNumeros/src/grafica evidencia integrador.csv', 'p') as juegos:

        juegos = ["PUBG", "Minecraft", "Pac-man", "Among us", "Tetris", "Fortnite", "League of legends", "Warzone", "World of warcraft"]
        numero_de_usuarios = [1037, 600, 505, 500, 500, 350, 101, 100, 100]

        plt.bar(juegos, numero_de_usuarios, width=0.7)

        plt.ylabel("numero de usuarios (en millones)")
        plt.xlabel("Nivel de fama de los juegos")

        plt.savefig("grafica_barras.jpeg")
        plt.show()

def main():
    
    print("Este es un programa diseñado para aquellos que les gustan los videojuegos.")
    print("Aquí encontraras recomendaciones que te puedan interesar...")
    print('------------------------------------------------------------------------------')
    a=input("<Enter> para continuar: ")
    print('------------------------------------------------------------------------------')

    print('¡Hola usuario!')

    b=input('¿Te gustan los videojuegos? (si/no): ')
    print('\n')

    if b == 'no':
        print('Lamentamos no poder ayudarte. Adiós')
    
    elif b == 'si':
        print('Esta es una tabla de los juegos mas famosos por número de usuarios: ')
        print('numero #1: Pubg con 1037 con millones de usuarios activos')
        print('numero #2: Minecraft con 600 millones usuarios activos')
        print('numero #3: Pac-man con 505 millones de usuarios activos')
        print('numero #4: Among us con 500 millones usuarios activos')
        print('numero #5: Tetris con 500 millones de usuarios activos')
        print('numero #6: Fornite con 350 millones de usuarios activos')
        print('numero #7: League of legends con 101 millones de usuarios activos')
        print('numero #8: Call of duty: Warzone con 100 millones de usuarios activos')
        print('numero #9: World of Warcraft con 100 millones de usuarios activos')
    
        print('\n')
        
        q=(input('¿Quieres conocer mas juegos? (si/no): '))
        if q=='no':
            print('Gracias por tu atención. Adiós :) ')

        elif q=='si':
            print('\n')
            print('¿Que categoria de juegos te gustaria conocer?')
            
            c= int(input('1:accion, 2:deportes, 3:aventura, 4: de rol: '))
        
            if c == 1:
                print('aqui estan unas sugerencias de juegos de accion mas populares hoy: ')
                print('Call of Duty: Warzone')
                print('Fornite')
                print('Counter Strike: Global Offensive')
                print('Apex Legends')
            elif c == 2:
                print('aqui estan unas sugerencias de juegos de deportes mas populares hoy: ')
                print('Fifa 22')
                print('NBA 2k22')
                print('Maddden NFL 18')
            elif c == 3:
                print('aqui estan unas sugerencias de juegos de aventura mas populares hoy: ')
                print('it takes two')
                print('God of War')
                print('Monster Hunter: Rise')
                print('Hitman 3')
            elif c == 4:
                print('aqui unas sugerencias de juegos de rol mas populares hoy: ')
                print('Pilars of Eternity')
                print('Tales of...')
                print('Mas Effect Trilogy')
            

            print('\n')
            d=input("<Enter> para continuar: ")
            print('\n')
            print('Ahora que conoces los mejores videojuegos, te recomendamos las mejores consolas:')
            print('--------------------------------------------------------------------------------')
            d1=input("<Enter> para continuar: ")
            print('--------------------------------------------------------------------------------')

            print('¿Te gustaria conocer cuales son los dispositivos mas utilizados para jugar?(si/no)')
            e=input('')
            #Primer informe con datos numericos
            if e == 'si':
                print('\n')
                print('El primer lugar, sorprendentemente lo ocupan los dispositivos moviles ocupando un 49%.')
                print('\n')
                print('En segundo lugar tenemos a los ordenadores, estos se hn popularizado mas en los ultimos años')
                print('debido a su gran capacidad que tiene, ocupa un 38%.')
                print('\n')
                print('En tercer lugar se encuentran las videoconsolas, estos conforme pasa el tiempo se ha perdido')
                print('la comunidad, lo cual si comparamos con otros dispositivos, es el unico cuya unica funcion es jugar videojuegos,')
                print('estas ocupan tan solo un 30%')
                print('\n')
                print('En cuarto lugar estan las tablets con un 26%')
                print('\n')
                print('En quinto lugar se encuentran las consolas portatiles, que a pesar de su gran popularidad en años')
                print('anteriores, estos conforme pasan los años, se innovan cada vez menos y tienen menor capacidad por lo que')
                print('solamente lo utiliza un 17%.')

            elif e == 'no':
                print('De seguro esto te interesara')

            print('\n')    
            print('¿Te interesa saber sobre las consolas recientes mas vendidas este 2021?(si/no)')
            w=input(' ')
            print('\n')

                
            #Segundo informe con datos numericos
            if w == 'si':
                print('1- Ocupando el 58.6% se encuentra la consola mas reciente desarrollda por ninteno, la nintendo switch')
                print('2- En el segundo puesto se encuentra la playstation 5 desarrollada por sony con un 28.3%')
                print('3- En tercer y ultimo lugar se encuentra la xbox series x/s ocupando un 13.1% en el mercado ')
            elif w == 'no':
                print('Entonces...Adiós')
            else:
                print('Respuesta invalida')
                        
            print('\n')        
            print('¿Te gustaria comprar alguna consola de videojuegos?(si/no)')
            f=input(' ')
            if f == 'si':
                print('¿Cual es tu presupuesto?')
                g=int(input(' '))
                            
                if 2000< g <= 7000 :
                    print('Hoy en dia tu presupuesto es algo bajo considernado los precios existentes, te recomendamos')
                    print('buscar consolas de segunda mano, solo procura probarlo antes de pagar.')
                elif 13000> g >7000:
                    print('Tu presupuesto es bueno, sin embargo, no esperes mucho potencial por lo que te recomiendo')
                    print('la nintendo switch, de seguro te gustara.')
                elif 13000 <= g <20000:
                    print('Tu presupuesto es bastante bueno, con ese dinero podras comprarte una consola de ultimo modelo')
                    print('como la xbox series x, o la playstation 5!')
                elif g>=20000:
                    print('Wow con ese dinero puedes comprarte la consola que tu quieras, hasta mas de una de ultimo modelo!!!.')
                elif g < 0:
                    print('Me parece que lo que necesitas es pagar tus deudas :(')
                elif 0<=g<=2000:
                    print('Es dificil encontrar una consola a tan buen precio')
                else:
                        print('Respuesta invalida')

            elif f == 'no':
                print('Adios!')
            
        else:
            print('Respuesta inválida')
   
    else:
        print('Respuesta inválida')

    print('\n')
    print('Esperamos que te haya sido de utilidad. ¡Nos vemos!')

if __name__=='__main__':
    main()
