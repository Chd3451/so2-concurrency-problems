# Documentación del nuesta solución al problema de la cena de los filósofos.

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
