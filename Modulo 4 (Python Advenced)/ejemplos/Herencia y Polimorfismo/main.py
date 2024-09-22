from persona import Persona, Supervisor, Cliente

#Herencia

persona1 = Persona('Juan', 'Perez','123456')
persona2 = Persona('José', 'Sanchez','456789')
persona1.imprimir_datos()
print(persona1)
persona2.imprimir_datos()
print(persona2)

###############################################################

supervisor1 = Supervisor('Juan', 'Perez','123456', 'Sur')
print("******")
supervisor1.imprimir_datos()
print("******")
supervisor1.imprimir_supervisor()
print("******")
print(supervisor1)

################################################################

cliente1 = Cliente('Juan', 'Perez','123456', 20)
print("******")
cliente1.imprimir_datos()
print("******")
cliente1.imprimir_cliente()
print("******")
print(cliente1)

#################################################################

#Polimorfismo

print("******")
persona1 = Persona('Juan', 'Perez','123456')
persona1.get_tipo()
print("******")
supervisor1 = Supervisor('Juan', 'Perez','123456', 'Sur')
supervisor1.get_tipo()
print("******")
cliente1 = Cliente('Juan', 'Perez','123456', 20)
cliente1.get_tipo()
