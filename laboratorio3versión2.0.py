class carro():
	ruedas = 4
	puertas = 0
	color = " "
	ventanas = 0
	marca = " " 

def _init_(self,modelo,asientos,color,tipo,combustible,precio,garantia,fecha_ingreso):
	self.modelo = modelo
	self.asientos = asientos
	self.color =  color
	self.tipo = tipo
	self.combustible = combustible
	self.precio = precio
	self.garantia = garantia
	self.fecha_ingreso = fecha_ingreso
	
toyota = carro(modelo="Hylux",asientos="5",color="Rojo",tipo="Pickup",combustible="Diesel",precio="$28,500.00",garantia="8",fecha_ingreso="23/11/2023")

kia = carro(modelo="K 20700",asientos="2",color="Escarlata",tipo="Pickup",combustible="Diesel",precio="$19,500.00",garantia="6",fecha_ingreso="20/11/2023")

mitsubishi = carro(modelo="Lancer",asientos="4",color="Negro",tipo="Sedan",combustible="Diesel",precio="$21,400.00",garantia="5",fecha_ingreso="22/11/2023")

nissan = carro(modelo="Frontier",asientos="5",color="Gris",tipo="Pickup",combustible="Diesel",precio="$23,000.00",garantia="6",fecha_ingreso="20/11/2023")

hyundai = carro(modelo="H 100",asientos="4",color="Plateado",tipo="Pickup",combustible="Diesel",precio="$20,200.00",garantia="4",fecha_ingreso="23/11/2023")

opcion1 = 0
print("La información de los autos aparecerá del auto más cómodo al más caro. Todos los precios ya incluyen IVA.")
print("1- Kia y Hyundai.")
print("2- Mitsubishi y Nissan.")
print("3- Toyota.")

opcion1 = int(input("Digite una de las tres opciones presentadas anteriormente: "))

if opcion1 == 1:
	print("----------------------------------------------")
	print("				Kia					")
	print(f"Modelo: {kia.modelo}")
	print(f"Asientos: {kia.asientos}")
	print(f"Color: {kia.color}")
	print(f"Tipo: {kia.tipo}")
	print(f"Tipo de combustible: {kia.combustible}")
	print(f"Precio: {kia.precio}")
	print(f"Años de garantía: {kia.garantia}")
	print(f"Fecha de ingreso: {kia.fecha_ingreso}")
	print("                       ")
	print("----------------------------------------------")
	print("				Hyundai					")
	print(f"Modelo: {hyundai.modelo}")
	print(f"Asientos: {hyundai.asientos}")
	print(f"Color: {hyundai.color}")
	print(f"Tipo: {hyundai.tipo}")
	print(f"Tipo de combustible: {hyundai.combustible}")
	print(f"Precio: {hyundai.precio}")
	print(f"Años de garantía: {hyundai.garantia}")
	print(f"Fecha de ingreso: {hyundai.fecha_ingreso}")
elif opcion1 ==2:
	print("----------------------------------------------")
	print("				Mitsubishi					")
	print(f"Modelo: {mitsubishi.modelo}")
	print(f"Asientos: {mitsubishi.asientos}")
	print(f"Color: {mitsubishi.color}")
	print(f"Tipo: {mitsubishi.tipo}")
	print(f"Tipo de combustible: {mitsubishi.combustible}")
	print(f"Precio: {mitsubishi.precio}")
	print(f"Años de garantía: {mitsubishi.garantia}")
	print(f"Fecha de ingreso: {mitsubishi.fecha_ingreso}")
	print("                       ")
	print("----------------------------------------------")
	print("				Nissan					")
	print(f"Modelo: {nissan.modelo}")
	print(f"Asientos: {nissan.asientos}")
	print(f"Color: {nissan.color}")
	print(f"Tipo: {nissan.tipo}")
	print(f"Tipo de combustible: {nissan.combustible}")
	print(f"Precio: {nissan.precio}")
	print(f"Años de garantía: {nissan.garantia}")
	print(f"Fecha de ingreso: {nissan.fecha_ingreso}")
elif opcion1 == 3:
	print("----------------------------------------------")
	print("				Toyota					")
	print(f"Modelo: {toyota.modelo}")
	print(f"Asientos: {toyota.asientos}")
	print(f"Color: {toyota.color}")
	print(f"Tipo: {toyota.tipo}")
	print(f"Tipo de combustible: {toyota.combustible}")
	print(f"Precio: {toyota.precio}")
	print(f"Años de garantía: {toyota.garantia}")
	print(f"Fecha de ingreso: {toyota.fecha_ingreso}")