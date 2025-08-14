SISTEMA DE CUENTAS BANCARIAS
RESUMEN DE LO QUE SE UTILIZA EN EL CODIGO

1. Estructura de datos principal

* Se usa un **diccionario** llamado `sistema_bancario` con una clave `"clientes"`.
* Cada cliente tiene:

  * **datos\_cliente** (información personal, contacto, ubicación).
  * **portafolio** (cuentas de ahorro, corriente, créditos, etc.), cada uno con:

    * saldo
    * historial de movimientos
    * estado (activo/inactivo/cancelado).

2. Funciones principales

* **`crear_cuenta()`** → Registra un nuevo cliente con sus datos y crea todas las cuentas iniciales.
* **`depositar()`** → Aumenta el saldo de una cuenta y registra el movimiento.
* **`solicitar_credito()`** → Activa un crédito, asigna monto y guarda historial.
* **`retirar()`** → Resta dinero de una cuenta si hay fondos.
* **`pagar_cuota_credito()`** → Disminuye el saldo de un crédito y lo marca como pagado si llega a 0.
* **`cancelar_cuenta()`** → Cambia el estado de una cuenta a cancelado y pone saldo en 0.
* **`salir()`** → Finaliza el programa.

3. Menú interactivo

* Un **bucle `while True`** que muestra opciones del sistema.
* Usa **condiciones `if-elif`** para ejecutar la función correspondiente.
* Solo se rompe el ciclo cuando el usuario elige salir.

4. Conceptos de Python usados

* **Diccionarios anidados** (estructura jerárquica de datos).
* **Funciones** para modularizar acciones.
* **Entradas de usuario (`input`)** para interactuar.
* **Condicionales (`if-elif-else`)** para el flujo lógico.
* **Bucles (`while True`)** para mantener el programa en ejecución.

