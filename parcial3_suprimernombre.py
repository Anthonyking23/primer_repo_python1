class agenda():
    def __init__(self):
        self.contacts = []

    def menu(self):
        while True:
            print("                ")
            print("                           ¡Bienvenido!")
            print("A continuación se te presentan las opciones de agenda, elige la opción de tu agrado.")
            print("             ")
            print("1. Agregar contacto a la agenda")
            print("2. Mostrar lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")
            print("-----‐-----------------------------------------------------------")

            opcion = input("Digita la opción deseada: ")

            if opcion == "1":
                self.agregar_contacto()
            elif opcion == "2":
                self.lista_contactos()
            elif opcion == "3":
                self.buscar_contacto()
            elif opcion == "4":
                self.editar_contacto()
            elif opcion == "5":
                print("Agenda cerrada. ")
                break
            else:
                print("Opción no válida. ¡Por favor inténtelo de nuevo!")

    def agregar_contacto(self):
        name = input("Ingrese el nombre del contacto: ")
        phone = input("Ingrese el teléfono del contacto: ")
        email = input("Ingrese el email del contacto: ")

        contact = {"Nombre": name, "Teléfono": phone, "Email": email}
        self.contacts.append(contact)
        print("El contacto fue añadido sin problema.")

    def lista_contactos(self):
        print("\nLista de contactos:")
        for i, contact in enumerate(self.contacts, 1):
            print(f"{i}. Nombre: {contact['Nombre']}, Teléfono: {contact['Teléfono']}, Email: {contact['Email']}")

    def buscar_contacto(self):
        name_to_search = input("Digite el nombre del contacto que deses buscar: ")
        for contact in self.contacts:
            if contact['Nombre'].lower() == name_to_search.lower():
                print(f"Nombre: {contact['Nombre']}, Teléfono: {contact['Teléfono']}, Email: {contact['Email']}")
                return
        print("El contacto escrito no ha sido encontrado.")

    def editar_contacto(self):
        name_to_edit = input("Ingrese el nombre del contacto a editar: ")
        for contact in self.contacts:
            if contact['Nombre'].lower() == name_to_edit.lower():
                new_name = input("Ingrese el nuevo nombre del contacto: ")
                new_phone = input("Ingrese el nuevo teléfono del contacto: ")
                new_email = input("Ingrese el nuevo email del contacto: ")

                contact['Nombre'] = new_name
                contact['Teléfono'] = new_phone
                contact['Email'] = new_email

                print("El contacto ha sido editado correctamente.")
                return

        print("El contacto no fue encontrado.")

personal_agenda = agenda()
personal_agenda.menu()