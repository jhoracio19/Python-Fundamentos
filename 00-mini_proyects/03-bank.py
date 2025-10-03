
class CuentaBancaria:
    
    def __init__ (self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, monto):
        self.saldo += monto
        print(f"Depósito realizado. Saldo actual ${self.saldo}")
    
    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro realizado. Saldo actual ${self.saldo}")
        else:
            print("Saldo insuficiente")
    
    def info(self):
        print(f"Titular: {self.titular}, saldo: ${self.saldo}")
    
    def transferir(self, monto, otra_cuenta):
        if monto <= self.saldo:
            self.saldo -= monto
            otra_cuenta.saldo += monto
            print(f"Transferencia realizada de {monto} a {otra_cuenta.titular}")
        else:
            print("Fondos insuficientes para transferir")


print("---------------------------------------------------")
cuenta = CuentaBancaria("Horacio", 0)

cuenta.depositar(50)
cuenta.retirar(500)
cuenta.info()

cuenta1 = CuentaBancaria("Horacio", 1000)
cuenta2 = CuentaBancaria("Naomi", 300)

print("---------------------------------------------------")
cuenta1.transferir(200, cuenta2)
cuenta1.info()
print("---------------------------------------------------")
cuenta2.info()

cuenta = CuentaBancaria("Horacio", 1000)

while True:
    print("\n--- Cajero Automático ---")
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        cuenta.info()
    elif opcion == "2":
        monto = float(input("Monto a depositar: "))
        cuenta.depositar(monto)
    elif opcion == "3":
        monto = float(input("Monto a retirar: "))
        cuenta.retirar(monto)
    elif opcion == "4":
        print("Gracias por usar el cajero. ¡Adiós!")
        break
    else:
        print("Opción no válida, intenta de nuevo.")
