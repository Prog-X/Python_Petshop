from perros import pitbull

perro = pitbull()


preg = raw_input("\n Que raza es? \n")

if preg == "pitbull":
    nomb = raw_input("Ingrese el nombre\n")
    perro.nombre(nomb)
    pes = raw_input("Ingrese el peso\n")
    perro.peso(pes)



resp = raw_input("desea guardar los datos? (si o no)\n")

if resp == "si":
    archi=open('Miperro.txt','w')
    archi=open('Miperro.txt','a')
    archi.write("BIENVENIDO A LOS DATOS DE SU PERRO\n\n\nLos datos son: "+"\n\traza: "+preg+"\n\tEl nombre es:"+perro.n+" \n\t pesa: "+perro.p+"kg"+"\nGracias por utilizar nuestros servicios!")
    archi.close()




salir = input("enter para salir")
