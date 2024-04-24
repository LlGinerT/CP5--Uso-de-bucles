import timeit

"""  
Vamos a hacer un experimento, como en este ejercicio,
sabemos lo que buscamos, los números pares entre el 1 y el 20,
podemos hacer una "trampa" saltando los números de 2 en 2,
de esta forma iterando solo sobre los números que buscamos(los pares)
y optimizando el código.
Como soy sincero, reconozco que esto lo vi en una de tus tutorías,
asi que, lo que me he propuesto es experimentar si se nota realmente la optimización.
"""

# Empezamos con el bucle 'for' comprobando numero por numero si es par.

# Decoramos un poco
titulo_for_1 = "FOR NUMERO POR NUMERO"
print(
    f"-------------------------\n{titulo_for_1.center(25)}\n-------------------------"
)

# Como son tiempos muy pequeños, los resultados eran inconsistentes,
# Asi que, usaremos la librería timeit, que nos permite ejecutar el código 100000 veces
# y dará tiempos mas consistentes.
# ¡¡¡TRANQUILO!!!
# No vamos a imprimir la serie de números 10.000 veces, para ello, primero haremos que el bucle imprima los números
# y luego haremos una función que imite el bucle original, pero sin imprimir los números.

for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# Ya están impresos por pantalla, siguiendo las instrucciones del ejercicio.
# Ahora, vamos a medir el tiempo, para ello definiremos una función por bucle a comparar.
def forNxN():
    """
    Función que imita el comportamiento del bucle for
    que comprueba numero por numero si es par, pero sin imprimirlo,
    en su lugar usaremos suma para que "haga algo" el bucle pero sin imprimir
    una cantidad inmensa de números.
    """
    suma = 0
    for i in range(1, 21):
        if i % 2 == 0:
            suma += i
    return suma


# Si tu ordenador tarda demasiado, cancela la ejecución y baja el parámetro 'number' un poco, ya que este determina el numero de repeticiones.
# Tampoco demasiado, porque podría dar resultados inconsistentes de nuevo, con bajarlo a 10000 debería ser suficiente,
# o al contrario, si tu ordenador va muy rápido y dan resultados muy bajos e inconsistentes, puedes aumentarlo.
cronometro_for_1 = timeit.timeit(forNxN, number=100000)
print(f"Tiempo: {cronometro_for_1}")
# En mi PC, da un resultado aproximado de 0.16s, después de ejecutarlo varia veces.

# Ahora vamos a comprobar la version "optimizada" y compararemos los resultados.
# La mecánica será la misma, primero imprimiremos la serie, y luego mediremos el tiempo con una "simulación".
titulo_for_2 = "FOR DE 2 EN 2"
print(
    f"-------------------------\n{titulo_for_2.center(25)}\n-------------------------"
)

# Aquí en el bucle, usaremos el parámetro 'step' de la clase range, que irá sumando a 'i' un 2,
# así solo iteraremos por los números que nos interesan y los imprimiremos directamente.
for i in range(2, 21, 2):
    print(i)


def for2en2():
    suma = 0
    for i in range(2, 21, 2):
        suma += i
    return suma


cronometro_for_2 = timeit.timeit(for2en2, number=100000)
print(f"Tiempo: {cronometro_for_2}")
# En este caso, me da una media de 0.06s


# Ahora vamos a repetir el mismo proceso con el bucle 'while',
# esperamos resultados similares.
titulo = "WHILE NUMERO POR NUMERO"
print(
    f"------------------------------\n{titulo.center(30)}\n------------------------------"
)

x = 1
while x <= 20:
    if x % 2 == 0:
        print(x)
    x += 1


def whileNxN():
    x = 1
    suma = 0
    while x <= 20:
        if x % 2 == 0:
            suma += x

        x += 1
    return suma


cronometro_while_1 = timeit.timeit(whileNxN, number=100000)
print(f"Tiempo: {cronometro_while_1}")


titulo = "WHILE 2 EN 2"
print(
    f"------------------------------\n{titulo.center(30)}\n------------------------------"
)

x = 0
while x < 20:
    x += 2
    print(x)


def while2n2():
    x = 0
    suma = 0
    while x < 20:
        x += 2
        suma += x
    return suma


cronometro_while_2 = timeit.timeit(while2n2, number=100000)
print(f"Tiempo: {cronometro_while_2}")

# Una vez hemos obtenido todos los tiempos, vamos a compararlos


def calcular_diferencia(tiempo_1: float, tiempo_2: float):
    """
    Definimos una función para comparar los resultados

    Args:
    - tiempo_1(float): resultado de la primera medición de tiempo a comparar
    - tiempo_2(float): resultado de la segunda medición de tiempo a comparar

    Returns:
    - diferencia(float): diferencia redondeada a 4 decimales entre los dos tiempos
    - Nombre del algoritmo con menor tiempo de resultado.
    """
    if tiempo_1 < tiempo_2:
        diferencia = tiempo_2 - tiempo_1
        return round(diferencia, 4), "N x N gana"
    else:
        diferencia = tiempo_1 - tiempo_2
        return round(diferencia, 4), "2 n 2 gana"


# Vamos a elaborar una tabla, donde compararemos los resultados.
titulo_resultados_for = "RESULTADOS 'FOR'"
titulo_resultados_while = "RESULTADOS 'WHILE'"
subtitulo_for_1 = "FOR N x N"
subtitulo_for_2 = "FOR 2 n 2"
resultado_for_1 = f"Tiempo aprox: {round(cronometro_for_1, 3)}"
resultado_for_2 = f"Tiempo aprox: {round(cronometro_for_2, 3)}"
subtitulo_while_1 = "WHILE N x N"
subtitulo_while_2 = "WHILE 2 n 2"
resultado_while_1 = f"Tiempo aprox: {round(cronometro_while_1, 3)}"
resultado_while_2 = f"Tiempo aprox: {round(cronometro_while_2, 3)}"
subtitulo_diff = "DIFERENCIA"
tiempo_for_diff, ganador_for = calcular_diferencia(cronometro_for_1, cronometro_for_2)
tiempo_while_diff, ganador_while = calcular_diferencia(
    cronometro_while_1, cronometro_while_2
)
print(f"---------------------------------------------------------------------")
print(
    f"| {titulo_resultados_for.center(30)}  |{titulo_resultados_while.center(30)}   |"
)
print(f"|---------------------------------|---------------------------------|")
print(
    f"|{subtitulo_for_1.center(12)}|{resultado_for_1.ljust(20)}|{subtitulo_while_1.center(13)}|{resultado_while_1.ljust(19)}|"
)
print(
    f"|{subtitulo_for_2.center(12)}|{resultado_for_2.ljust(20)}|{subtitulo_while_2.center(13)}|{resultado_while_2.ljust(19)}|"
)
print("|---------------------------------|---------------------------------|")
print(
    f"|{subtitulo_diff.center(12)}|{str(tiempo_for_diff).ljust(7)}|{ganador_for.ljust(11)}"
    + " |"
    + f" {subtitulo_diff.ljust(12)}|{str(tiempo_while_diff).ljust(7)}|{ganador_while.ljust(11)}|"
)
print(f"---------------------------------------------------------------------")

# Los resultados en mi ordenador dan una diferencia media de 0.1 en el 'for' y de 0.15 en el 'while',
# a favor del bucle que itera menos veces(2 n 2), como era de esperar.
# Los resultados, no son tiempos significativo en este caso,
# pero vemos que estas micro optimizaciones pueden llegar a ser significativas cuando tratamos
# con una cantidad importante de datos.
# Así que, en conclusión, siempre que se pueda,
# deberíamos ahorrar el mayor numero de "pasos" en el código, siempre que el requerimiento lo permita.
