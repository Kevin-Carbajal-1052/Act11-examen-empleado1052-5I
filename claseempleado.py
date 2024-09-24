class empleado1052:
    #Zona de atributos
    id=0
    nombre=""
    direccion=""
    correo=""
    horario=""
    sueldo=0
    curp=""

    #Zona de funciones
    def mostrardatos(self):
        print("--Mostra datos--\n")
        print(f"El id del usuario es: {self.id}")
        print(f"El nombre es: {self.nombre}")
        print(f"Su direccion es: {self.direccion}")
        print(f"Su correo es: {self.correo}")
        print(f"Su horario es: {self.horario}")
        print(f"Su sueldo es: {self.sueldo}")
        print(f"Su curp es: {self.curp}\n")

    def listar_empleado(self):
        print("--Lista de empleados--\n")
        listaempleado=["Kevin", "Roberto", "Cristian","Karen","Casandra\n"]
        for x in listaempleado:
            print(x)
    def tupla_empleado(slef):
        print("--Tupla de empleados--\n")
        tuplaempleado=("Kevin", "Roberto", "Cristian","Karen","Casandra\n")
        for x in tuplaempleado:
            print(x)
    def dic_empleado(self):
        print("--Diccionario--\n")
        dicempleado={"adriel":"no",
                     "Roberto":"si",
                     "Melany":"no",
                     "isac":"si",
                     "carlos":"no\n"}
        for x,y in dicempleado.items():
            print(x,y)

    def altas(self):
        print("Operacion realizada para la clase empleado con exito\n")
    
    def bajas(self):
        print("Datos borrados con exito\n")

#Zona de creacion de objetos
obj=empleado1052()
obj.id=1
obj.nombre="Roberto"
obj.direccion="Colonia aeropuerto"
obj.correo="Robertote@gmail.com"
obj.horario="3:00 pm 8:00 pm"
obj.sueldo=15000
obj.curp="CEGR070108HCHRRBA9"

#Llamar a las funciones
obj.mostrardatos()
obj.listar_empleado()
obj.tupla_empleado()
obj.dic_empleado()
obj.altas()
obj.bajas()