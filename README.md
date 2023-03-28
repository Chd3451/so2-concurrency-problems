# so2-concurrency-problems
Repositorio creado por: Miguel Anibal (), Jefferson Hidalgo () y Charlie Delgado (2021-1092)

Clase de Sistemas operativos II P2 2023.


# Investigación: Problema de la concurrencia.

## Concepto básico de semáforo en los sistemas operativos:

Un semáforo en un sistema operativo es una variable que se utiliza para controlar el acceso a un recurso compartido. Es similar a un semáforo de tráfico que permite o deniega el acceso a un recurso. Cuando un proceso desea acceder al recurso, primero debe tomar el semáforo. Si el semáforo está en verde, el proceso puede acceder al recurso, y si está en rojo, debe esperar. Una vez que el proceso ha terminado de usar el recurso, libera el semáforo. De esta manera, el semáforo ayuda a evitar problemas como la corrupción de datos o bloqueos del sistema al garantizar que varios procesos no accedan al mismo recurso simultáneamente.
