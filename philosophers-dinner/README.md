#Video de la explicacion;
https://youtu.be/jVyt9GLr3AI

# Documentación del nuesta solución al problema de la cena de los filósofos.

Cinco filósofos se sientan alrededor de una mesa redonda y hay un tenedor entre cada dos filósofos. Los filósofos pasan su tiempo comiendo y pensando. Para comer, necesitan dos tenedores adyacentes, uno a su izquierda y otro a su derecha. Cuando terminan de comer, dejan los tenedores y continúan pensando. Si todos los filósofos intentan comer al mismo tiempo, es posible que se produzca una situación de competencia por los recursos (tenedores) y que se produzca un deadlock.

El programa crea un hilo para cada filósofo y define dos funciones: agarrartenedores() y liberartenedores(). La primera función trata de tomar los tenedores izquierdo y derecho (en ese orden) y devuelve True si ha podido adquirir ambos y False de lo contrario. La segunda función libera los tenedores adyacentes al filósofo.

La función iniciarSimulacion() es la que va a ejecutar cada filósofo (hilo). Esta función contiene un ciclo while que se ejecuta mientras el tiempo que el filósofo ha estado comiendo es menor que el tiempo total que requiere para estar satisfecho. En cada iteración, el filósofo trata de tomar los tenedores y, si lo consigue, come durante un tiempo aleatorio entre 0 y la ráfaga de comer (un valor que se pasa como argumento al programa). Si no puede tomar los tenedores, espera un tiempo aleatorio antes de intentar de nuevo. Si no puede tomar los tenedores durante un número máximo de intentos (un valor que se pasa como argumento al programa), se considera que el filósofo ha muerto por inanición y se termina su ejecución.

```python
import threading

def agarrartenedores(id_filosofo):
    # Trata de tomar los tenedores izquierdo y derecho
    # y devuelve True si ha podido adquirir ambos y False de lo contrario

def liberartenedores(id_filosofo):
    # Libera los tenedores adyacentes al filósofo

def iniciarSimulacion(id_filosofo, tiempo_comer, tiempo_satisfecho, num_intentos):
    while tiempo_comiendo < tiempo_satisfecho:
        # Trata de tomar los tenedores y, si lo consigue, come durante un tiempo aleatorio
        # Si no puede tomar los tenedores, espera un tiempo aleatorio antes de intentar de nuevo
        # Si no puede tomar los tenedores durante un número máximo de intentos, se termina su ejecución

for i in range(num_filosofos):
    threading.Thread(target=iniciarSimulacion, args=(i, tiempo_comer, tiempo_satisfecho, num_intentos)).start()

```
El programa utiliza la librería argparse para leer los argumentos pasados por la línea de comandos. Los argumentos son el número de filósofos, la ráfaga de comer de los filósofos, el tiempo total que requiere comer un filósofo para estar satisfecho y la cantidad de intentos antes de que el filósofo muera de inanición. También se establece el estado inicial de cada filósofo como "F" (filosofando).

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("num_filosofos", type=int, help="Número de filósofos en la mesa")
parser.add_argument("tiempo_comer", type=int, help="Ráfaga de comer de los filósofos")
parser.add_argument("tiempo_satisfecho", type=int, help="Tiempo total que requiere comer un filósofo para estar satisfecho")
parser.add_argument("num_intentos", type=int, help="Cantidad de intentos antes de que el filósofo muera de inanición")
args = parser.parse_args()

```

En la función principal se crean los hilos y se inicia su ejecución. Después, se espera a que terminen todos los hilos.

```python
hilos = []

for i in range(args.num_filosofos):
    hilo = threading.Thread(target=iniciarSimulacion, args=(i, args.tiempo_comer, args.tiempo_satisfecho, args.num_intentos))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

```

*Aclaración: Los trozos de código están descritos de manera resumida, por esto pueden llegar a verse diferentes al programa completo.*

# Investigación:

## Concurrencia:
La concurrencia en informática es un término fundamental para entender cómo funcionan los sistemas informáticos modernos. Se refiere a la habilidad de un sistema para manejar múltiples tareas simultáneamente en lugar de realizarlas de forma secuencial. Esto significa que, en lugar de esperar a que una tarea se complete antes de empezar la siguiente, varias tareas se pueden realizar al mismo tiempo.

La concurrencia se puede lograr a través de diferentes técnicas, como el uso de hilos o procesos en un sistema operativo, el uso de técnicas de programación concurrente y la implementación de algoritmos y estructuras de datos diseñados para manejar múltiples tareas al mismo tiempo.

## Paralelismo vs concurrencia:
El paralelismo se refiere a la ejecución simultánea de varias tareas en diferentes procesadores o núcleos de procesamiento en un sistema informático. Esto implica la división de cada tarea en sub-tareas más pequeñas que se procesan en paralelo en distintos procesadores. El objetivo del paralelismo es aumentar la rapidez y la eficiencia de procesamiento, lo que permite ejecutar más tareas en menos tiempo.

El paralelismo es especialmente útil cuando se deben procesar grandes cantidades de datos o realizar cálculos complejos que consumen muchos recursos de procesamiento. Por ejemplo, la simulación de sistemas complejos, la renderización de gráficos 3D o la minería de datos en grandes conjuntos de datos pueden beneficiarse significativamente del uso del paralelismo.

Por otro lado, la concurrencia se refiere a la habilidad de un sistema para gestionar múltiples tareas en el mismo procesador o núcleo de procesamiento. En este caso, en lugar de dividir una tarea en sub-tareas más pequeñas para ejecutarlas en distintos procesadores, el sistema administra las tareas simultáneamente mediante cambios de contexto. El cambio de contexto es un proceso en el cual el procesador asigna un fragmento de tiempo a una tarea y luego cambia a otra tarea antes de que la primera se complete. El objetivo de la concurrencia es permitir que varias tareas se ejecuten al mismo tiempo, lo cual puede mejorar la eficiencia y la capacidad de respuesta del sistema.

La concurrencia es adecuada para situaciones en las que se deben gestionar múltiples tareas de manera interactiva y con una respuesta rápida, como en aplicaciones de software en tiempo real, sistemas de comunicación, servidores web y videojuegos en línea. En estos casos, la concurrencia permite que el sistema gestione de manera efectiva múltiples solicitudes y eventos que ocurren de manera simultánea.

## Implementación de hilos en Python:

Los hilos en Python se implementan utilizando la biblioteca "threading", que proporciona una interfaz de programación de aplicaciones (API) para trabajar con hilos.

Para crear un hilo en Python, primero debe importar la biblioteca "threading". Luego, debe crear una instancia de la clase Thread y pasarle una función que se ejecutará en el hilo. La función se define como una función independiente que puede tomar argumentos si es necesario.

A continuación, se muestra un ejemplo de creación de un hilo en Python:

```python
import threading

def mi_funcion():
    print("Hola desde el hilo!")

# Crear una instancia de Thread y pasar la función mi_funcion como argumento
mi_hilo = threading.Thread(target=mi_funcion)

# Iniciar el hilo
mi_hilo.start()

```
En el ejemplo anterior, se importa la biblioteca "threading" y se define una función llamada "mi_funcion" que simplemente imprime un mensaje. Luego se crea una instancia de la clase Thread y se pasa la función "mi_funcion" como argumento. Finalmente, se inicia el hilo llamando al método "start()" en la instancia del hilo.

Además de crear hilos simples, la biblioteca "threading" también proporciona funciones para trabajar con múltiples hilos al mismo tiempo. Por ejemplo, puede usar la función "enumerate()" para obtener una lista de todos los hilos activos en un momento dado, o la función "join()" para esperar hasta que un hilo específico haya finalizado su ejecución.

Es importante tener en cuenta que, aunque los hilos en Python pueden ser útiles para mejorar el rendimiento y la capacidad de respuesta de un programa, también pueden presentar desafíos de sincronización y problemas de concurrencia. Por lo tanto, es importante tener en cuenta estos factores al implementar hilos en Python y utilizar estrategias adecuadas para evitar problemas de seguridad y de rendimiento en el programa.


## Deadlock;
Se refiere a una situación en la que dos o más procesos están esperando indefinidamente por recursos que no pueden liberar porque están siendo retenidos por otros procesos. En otras palabras, cada proceso está esperando que el otro proceso libere los recursos que necesita para continuar. Como resultado, los procesos quedan atrapados en un estado de espera infinito y no pueden avanzar.

## Exclusión Mutual;
Se refiere a una técnica utilizada en programación concurrente para garantizar que dos o más procesos no puedan acceder al mismo recurso al mismo tiempo. Esto se logra mediante el uso de mecanismos de bloqueo, como semáforos, mutexes o monitores, que aseguran que solo un proceso pueda acceder al recurso en cualquier momento dado.

## Mantenga y espere;
Es una estrategia utilizada en sistemas operativos para resolver problemas de exclusión mutua y evitar la posibilidad de deadlock. En esta estrategia, un proceso que solicita un recurso lo retiene mientras espera que se le otorgue el recurso solicitado. Esto significa que si otro proceso solicita el mismo recurso, deberá esperar hasta que el primer proceso lo libere. Esto evita la posibilidad de deadlock pero puede dar lugar a una utilización ineficiente de los recursos.

## No preventivo;
El término "preventivo" en programación se refiere a la práctica de tomar medidas para evitar problemas antes de que ocurran. En este sentido, es importante tener en cuenta que la programación es una disciplina que requiere una planificación cuidadosa y una atención constante a los detalles para garantizar un código limpio y funcional. Por lo tanto, no implementar medidas preventivas en la programación podría tener como resultado la aparición de errores y problemas técnicos en el futuro. Es decir, se puede terminar gastando más tiempo y recursos tratando de resolver problemas que podrían haberse evitado si se hubieran tomado medidas preventivas adecuadas en primer lugar. Algunas de las medidas preventivas que se pueden tomar en la programación son: Realizar pruebas unitarias para asegurarse de que cada componente del software funciona correctamente. Implementar controles de calidad de código para garantizar que el código cumpla con los estándares y las mejores prácticas de la industria. Mantener una documentación detallada del código para facilitar su comprensión y el mantenimiento posterior. Utilizar herramientas automatizadas para detectar y corregir errores en el código antes de que se conviertan en problemas mayores.

## Esperar circular;
El término "esperar circular" en programación se refiere a una práctica que consiste en pausar la ejecución de un programa hasta que un evento específico ocurra, generalmente la llegada de ciertos datos o la respuesta de un usuario. Aunque esperar circular puede ser útil en algunos casos, como cuando se espera una entrada de usuario, no es una buena práctica general para la programación. La razón es que detener la ejecución de un programa puede ser ineficiente y puede hacer que el programa se sienta lento y no receptivo para el usuario. En lugar de esperar circular, es mejor diseñar programas que sean asincrónicos y respondan a eventos. Esto significa que el programa continúa ejecutándose mientras espera que ocurra un evento, y en lugar de bloquear la ejecución del programa, se activa una respuesta cuando el evento ocurre. Por ejemplo, en lugar de esperar circular para que lleguen los datos de un servidor, un programa asincrónico enviaría una solicitud de datos al servidor y luego continuaría ejecutándose mientras espera que lleguen los datos. Cuando los datos llegan, se activa una respuesta y se procesan los datos.

## Como manejar el interbloque en sistemas operativos - compara con problema de los filosofos;

El problema de los filósofos se convierte en un problema de interbloque cuando cada filósofo intenta tomar los dos tenedores al mismo tiempo. Si todos los filósofos intentan tomar su tenedor izquierdo al mismo tiempo, entonces nadie puede tomar su tenedor derecho, lo que lleva a un interbloqueo. En sistemas operativos, el interbloqueo ocurre cuando dos o más procesos están bloqueados en una espera circular de recursos que cada uno de ellos necesita para continuar. Esto puede ser causado por una variedad de factores, incluyendo una mala planificación del proceso, una asignación incorrecta de recursos, o una falta de comunicación entre los procesos. Para manejar el interbloque en sistemas operativos, se utilizan diferentes técnicas de prevención y recuperación. Algunas técnicas de prevención incluyen la asignación cuidadosa de recursos, la planificación adecuada del proceso y la coordinación de los procesos para evitar la espera circular. Por otro lado, algunas técnicas de recuperación incluyen la detección y la resolución del interbloqueo mediante la liberación de recursos, la interrupción de los procesos o la reorganización de la planificación del proceso.
