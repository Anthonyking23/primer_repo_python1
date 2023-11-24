class CARRO(): 
	ruedas = 4
	puertas = 0
	color = " "
	ventanas = 0
	marca = " " 

toyota = CARRO()
toyota.modelo= "Hylux"
toyota.asientos = 4
toyota.color = "Rojo"
toyota.tipo = "Pickup"
toyota.tipo_de_combustible = "Diesel"
toyota.precio = "$29,900.00"
toyota.garantia = "8 años"
toyota.fecha_ingreso = "23/11/23"
	
	
kia = CARRO()
kia.modelo = "Hylux"
kia.asientos = 4
kia.color = "Blanco"
kia.tipo = "Sedan"
kia.tipo_de_combustible = "Diesel"
kia.precio = "$19,000.00"
kia.garantia = "6 años"
kia.fecha_ingreso = "23/11/22"
	
	
mitsubishi = CARRO()
mitsubishi.modelo = "Hylux"
mitsubishi.asientos = 5
mitsubishi.color = "Negro"
mitsubishi.tipo = "Sedan"
mitsubishi.tipo_de_combustible = "Diesel"
mitsubishi.precio = "$23,500.00"
mitsubishi.garantia = "5 años"
mitsubishi.fecha_ingreso = "23/11/22"
	
	
nissan = CARRO()
nissan.modelo = "Hylux"
nissan.asientos = 4
nissan.color = "Gris"
nissan.tipo = "Sedan"
nissan.tipo_de_combustible = "Diesel"
nissan.precio = "$24,000.00"
nissan.garantia = "10 años"
nissan.fecha_ingreso = "23/11/22"
	
	
hyundai = CARRO()
hyundai.modelo = "Hylux"
hyundai.asientos = 4
hyundai.color = "Plateado"
hyundai.tipo = "Sedan"
hyundai.tipo_de_combustible = "Diesel"
hyundai.precio = "$27,000.00"
hyundai.garantia = "7 años"
hyundai.fecha_ingreso = "23/11/22"

print("Elija la información de dos autos que deseas, luego digite dos de las opciones ")
print("1- Toyota y Kia")
print("2- Mitsubishi y Nissan")
print("3- Hyundai")

opcion1 = 0

opcion1 = int(input("Digite la primero opción deseada: "))

if opcion1 == 1:
	print("----------------------------------------------")
	print("			Toyota					")
	print("Modelo:", toyota.modelo)
	print("Asientos: ", toyota.asientos)
	print("Color: ", toyota.color)
	print("Tipo: ", toyota.tipo )
	print("Tipo de combustible: ", toyota.tipo_de_combustible)
	print("Precio: ", toyota.precio)
	print("Años de garantía: ", toyota.garantia)
	print("Fecha de ingreso: ", toyota.fecha_ingreso)
	print("                       ")
	print("__________________________")
	print("		Kia						")
	print("Modelo:", kia.modelo)
	print("Asientos: ", kia.asientos)
	print("Color: ", kia.color)
	print("Tipo: ", kia.tipo )
	print("Tipo de combustible: ", kia.tipo_de_combustible)
	print("Precio: ", kia.precio)
	print("Años de garantía: ", kia.garantia)
	print("Fecha de ingreso: ", kia.fecha_ingreso)
	print("__________________________")
elif opcion1 == 2:
	print("----------------------------------------------")
	print("			Mitsubishi					")
	print("Modelo:", mitsubishi.modelo)
	print("Asientos: ", mitsubishi.asientos)
	print("Color: ", mitsubishi.color)
	print("Tipo: ", mitsubishi.tipo )
	print("Tipo de combustible: ", mitsubishi.tipo_de_combustible)
	print("Precio: ", mitsubishi.precio)
	print("Años de garantía: ", mitsubishi.garantia)
	print("Fecha de ingreso: ", mitsubishi.fecha_ingreso)
	print("            ")
	print("__________________________")
	print("			Nissan					")
	print("Modelo:", nissan.modelo)
	print("Asientos: ", nissan.asientos)
	print("Color: ", nissan.color)
	print("Tipo: ", nissan.tipo )
	print("Tipo de combustible: ", nissan.tipo_de_combustible)
	print("Precio: ", nissan.precio)
	print("Años de garantía: ", nissan.garantia)
	print("Fecha de ingreso: ", nissan.fecha_ingreso)
	print("__________________________")
elif opcion1 == 3:
	print("__________________________")
	print("			Hyundai					")
	print("Modelo:", hyundai.modelo)
	print("Asientos: ", hyundai.asientos)
	print("Color: ", hyundai.color)
	print("Tipo: ", hyundai.tipo )
	print("Tipo de combustible: ", hyundai.tipo_de_combustible)
	print("Precio: ", hyundai.precio)
	print("Años de garantía: ", hyundai.garantia)
	print("Fecha de ingreso: ", hyundai.fecha_ingreso)
	print("__________________________")
	