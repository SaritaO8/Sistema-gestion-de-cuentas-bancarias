#SISTEMA DE CUENTAS BANCARIAS - MENÚ INTERACTIVO
sistema_bancario = {"clientes": {}}

#Crear cuenta
def crear_cuenta():
    cc = input("CC: ")
    nombre = input("Nombre: ")
    email = input("Email: ")
    edad = input("Edad: ")
    movil = input("Teléfono móvil: ")
    pais = input("País: ")
    depto = input("Departamento: ")
    ciudad = input("Ciudad: ")

    sistema_bancario["clientes"][cc] = {
        "datos_cliente": {
            "cc": cc,
            "nombre": nombre,
            "email": email,
            "edad": edad,
            "contacto": {"movil": movil},
            "ubicacion": {"pais": pais, "depto": depto, "ciudad": ciudad}
        },
        "portafolio": {
            "cta_ahorros": {"saldo": 0, "historial": {}, "estado": "activo"},
            "cta_corriente": {"saldo": 0, "historial": {}, "estado": "activo"},
            "CDT": {"saldo": 0, "historial": {}, "estado": "inactivo"},
            "credito_libre_inv": {"saldo": 0, "historial": {}, "estado": "inactivo"},
            "credito_vivienda": {"saldo": 0, "historial": {}, "estado": "inactivo"},
            "credito_compra_automovil": {"saldo": 0, "historial": {}, "estado": "inactivo"}
        }
    }
    print(f"Cliente {nombre} creado.")

#Depositar dinero
def depositar():
    cc = input("CC cliente: ")
    tipo_cuenta = input("Tipo de cuenta: ")
    monto = float(input("Monto a depositar: "))
    fecha = input("Fecha (YYYY-MM-DD): ")
    hora = input("Hora: ")

    cliente = sistema_bancario["clientes"].get(cc)
    if not cliente:
        print("Cliente no encontrado.")
        return
    cuenta = cliente["portafolio"].get(tipo_cuenta)
    if not cuenta:
        print("Cuenta no encontrada.")
        return

    cuenta["saldo"] += monto
    id_mov = f"MOV{len(cuenta['historial'])+1}"
    cuenta["historial"][id_mov] = {"fecha_mov": fecha, "hora": hora, "valor": monto, "tipo": "depósito"}
    print(f"Depósito de {monto} en {tipo_cuenta}.")

#Solicitar crédito

def solicitar_credito():
    cc = input("CC cliente: ")
    tipo_credito = input("Tipo de crédito: ")
    monto = float(input("Monto solicitado: "))
    fecha = input("Fecha (YYYY-MM-DD): ")
    hora = input("Hora: ")

    cliente = sistema_bancario["clientes"].get(cc)
    if not cliente:
        print("Cliente no encontrado.")
        return
    credito = cliente["portafolio"].get(tipo_credito)
    if not credito:
        print("Crédito no encontrado.")
        return

    credito["saldo"] = monto
    credito["estado"] = "activo"
    id_mov = f"MOV{len(credito['historial'])+1}"
    credito["historial"][id_mov] = {"fecha_mov": fecha, "hora": hora, "valor": monto, "tipo": "crédito otorgado"}
    print(f"🏦 Crédito otorgado: {monto} en {tipo_credito}.")

# ------------------------
# 4. Retirar dinero
# ------------------------
def retirar():
    cc = input("CC cliente: ")
    tipo_cuenta = input("Tipo de cuenta: ")
    monto = float(input("Monto a retirar: "))
    fecha = input("Fecha (YYYY-MM-DD): ")
    hora = input("Hora: ")

    cliente = sistema_bancario["clientes"].get(cc)
    if not cliente:
        print("Cliente no encontrado.")
        return
    cuenta = cliente["portafolio"].get(tipo_cuenta)
    if not cuenta:
        print("Cuenta no encontrada.")
        return
    if cuenta["saldo"] < monto:
        print("Fondos insuficientes.")
        return

    cuenta["saldo"] -= monto
    id_mov = f"MOV{len(cuenta['historial'])+1}"
    cuenta["historial"][id_mov] = {"fecha_mov": fecha, "hora": hora, "valor": -monto, "tipo": "retiro"}
    print(f"Retiro de {monto} en {tipo_cuenta}.")

# Pago de cuota de crédito
def pagar_cuota_credito():
    cc = input("CC cliente: ")
    tipo_credito = input("Tipo de crédito: ")
    monto = float(input("Monto a pagar: "))
    fecha = input("Fecha (YYYY-MM-DD): ")
    hora = input("Hora: ")

    cliente = sistema_bancario["clientes"].get(cc)
    if not cliente:
        print("Cliente no encontrado.")
        return
    credito = cliente["portafolio"].get(tipo_credito)
    if not credito:
        print("Crédito no encontrado.")
        return

    credito["saldo"] -= monto
    if credito["saldo"] <= 0:
        credito["estado"] = "pagado"

    id_mov = f"MOV{len(credito['historial'])+1}"
    credito["historial"][id_mov] = {"fecha_mov": fecha, "hora": hora, "valor": -monto, "tipo": "pago crédito"}
    print(f"Pago de {monto} realizado a {tipo_credito}.")

# 6. Cancelar cuenta
def cancelar_cuenta():
    cc = input("CC cliente: ")
    tipo_cuenta = input("Tipo de cuenta: ")

    cliente = sistema_bancario["clientes"].get(cc)
    if not cliente:
        print("Cliente no encontrado.")
        return
    cuenta = cliente["portafolio"].get(tipo_cuenta)
    if not cuenta:
        print("Cuenta no encontrada.")
        return

    cuenta["estado"] = "cancelado"
    cuenta["saldo"] = 0
    print(f"Cuenta {tipo_cuenta} cancelada.")

# 7. Salir
def salir():
    print("Saliendo del sistema...")
    exit()

# Menú principal
def menu():
    while True:
        print("\n=== SISTEMA DE CUENTAS BANCARIAS ===")
        print("1. Crear Cuenta")
        print("2. Depositar Dinero")
        print("3. Solicitar Crédito")
        print("4. Retirar Dinero")
        print("5. Pago Cuota Crédito")
        print("6. Cancelar Cuenta")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1": crear_cuenta()

        elif opcion == "2": depositar()
        elif opcion == "3": solicitar_credito()
        elif opcion == "4": retirar()
        elif opcion == "5": pagar_cuota_credito()
        elif opcion == "6": cancelar_cuenta()
        elif opcion == "7": salir()

        else:
            print("Opción no válida.")

# Ejecución del menú
menu()

