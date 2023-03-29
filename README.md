# so2-concurrency-problems
Repositorio creado por: Miguel Anibal (), Jefferson Hidalgo (2021-1203) y Charlie Delgado (2021-1092)

Clase de Sistemas operativos II P2 2023.


# Investigación: Problema de la concurrencia.

## Concepto básico de semáforo en los sistemas operativos:

Un semáforo en un sistema operativo es una variable que se utiliza para controlar el acceso a un recurso compartido. Es similar a un semáforo de tráfico que permite o deniega el acceso a un recurso. Cuando un proceso desea acceder al recurso, primero debe tomar el semáforo. Si el semáforo está en verde, el proceso puede acceder al recurso, y si está en rojo, debe esperar. Una vez que el proceso ha terminado de usar el recurso, libera el semáforo. De esta manera, el semáforo ayuda a evitar problemas como la corrupción de datos o bloqueos del sistema al garantizar que varios procesos no accedan al mismo recurso simultáneamente.

## Semaforos Binarios y Enteros:

Los semáforos son un mecanismo de sincronización utilizado en la programación concurrente para controlar el acceso a recursos compartidos. Los semáforos binarios y enteros son dos tipos comunes de semáforos utilizados en este contexto.

Un semáforo binario es un semáforo que sólo puede tener dos valores posibles: 0 y 1. Se utiliza para controlar el acceso a un recurso compartido de forma que sólo un proceso pueda acceder a él en un momento determinado. Cuando un proceso quiere acceder al recurso, intenta adquirir el semáforo. Si el semáforo está en 0, el proceso adquiere el semáforo y accede al recurso. Si el semáforo está en 1, el proceso debe esperar hasta que el semáforo vuelva a estar en 0 antes de poder acceder al recurso.

Por otro lado, un semáforo entero es un semáforo que puede tomar cualquier valor entero positivo. Se utiliza para controlar el acceso a un recurso compartido de forma que varios procesos puedan acceder a él simultáneamente, pero sólo un número limitado de procesos puedan acceder al mismo tiempo. Cada proceso intenta adquirir el semáforo. Si el valor del semáforo es mayor que cero, el proceso adquiere el semáforo y accede al recurso. Si el valor del semáforo es cero, el proceso debe esperar hasta que algún otro proceso libere el recurso y aumente el valor del semáforo antes de que pueda adquirir el semáforo y acceder al recurso.

En resumen, los semáforos binarios se utilizan para controlar el acceso a un recurso compartido de forma que sólo un proceso pueda acceder al mismo tiempo, mientras que los semáforos enteros se utilizan para controlar el acceso a un recurso compartido de forma que varios procesos puedan acceder al mismo tiempo, pero sólo un número limitado de procesos puedan acceder al mismo tiempo.

##Explica la relación entre los semáforos y la sincronización

Los semáforos son una herramienta utilizada en programación para la sincronización de procesos o hilos en un sistema computacional.Un semáforo es una variable que se utiliza para indicar el estado de un recurso compartido en un sistema. Cuando un proceso necesita acceder a ese recurso, debe tomar el semáforo para indicar que está en uso. Si otro proceso intenta acceder al recurso mientras está siendo utilizado por otro proceso, el semáforo le impedirá el acceso y lo colocará en espera hasta que se libere el recurso.En este sentido, los semáforos son útiles para la sincronización de procesos, ya que permiten que los procesos compartan recursos de manera ordenada y evitan que se produzcan condiciones de carrera, donde varios procesos intentan acceder al mismo recurso simultáneamente, lo que puede llevar a errores y resultados inesperados.Por ejemplo, en un sistema operativo, los semáforos se utilizan comúnmente para sincronizar el acceso a recursos compartidos, como archivos o dispositivos de entrada/salida. De esta manera, el sistema operativo puede garantizar que solo un proceso acceda a un recurso compartido en un momento dado, evitando errores y conflictos.
