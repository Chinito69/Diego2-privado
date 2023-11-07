# Función para validar un Rut en formato ########-#
print("ESTA ECHO PARA 6 RUT SI SE QUIERE CAMBIAR SE TIENE QUE CAMBIAR DE LAS LINEAS DE CODIGO, EXACTAMENTE EN LA LINEA 12")
def validar_rut(rut):
    if len(rut)!=10:
        return False
    if not rut[:8].isdigit() or rut[8]!='-' or not rut[9].isdigit(): 
        return False
    return True
# Función para leer Ruts y guardarlos en el archivo Cedulas.txt
def guardar_rut():
    try:
        n_ruts=6  
        with open("Cedulas.txt", "w") as file:
            for i in range(n_ruts):
                rut=input(f"Ingrese el Rut Numero. {i + 1} (formato ########-#): ")
                while not validar_rut(rut):
                    print("Rut incorrecto. Ingrese un Rut válido.")
                    rut=input(f"Ingrese el Rut Numero. {i + 1} (formato ########-#): ")
                file.write(rut+"\n")
        print("Rut guardados en el archivo Cedulas.txt")
    except Exception as e:
        print(f"Error al guardar los Ruts: {e}")
# Función para reemplazar el 2do Rut con "12345678-9"
def reemplazar_rut():
    try:
        with open("Cedulas.txt","r") as file:
            lines=file.readlines()
        if len(lines)>=2:
            lines[1]="12345678-9\n"
        with open("Cedulas.txt", "w") as file:
            file.writelines(lines)
        print("El 2do Rut ha sido reemplazado con '12345678-9'")
    except Exception as e:
        print(f"Error al reemplazar el Rut: {e}")
# Función para cargar Ruts
def cargar_rut():
    try:
        with open("Cedulas.txt","r") as file:
            rut_lista=[line.strip() for line in file]
        return rut_lista
    except Exception as e:
        print(f"Error al cargar los Ruts desde el archivo: {e}")
# Función para imprimir los Ruts con formato específico
def imprimir_rut(rut_lista):
    if not rut_lista:
        print("La lista de Ruts está vacía.")
        return
    for i, rut in enumerate(rut_lista):
        print(f"Rut Nro. {i + 1}: {rut}")
if __name__ == "__main__":
    guardar_rut()
    reemplazar_rut()
    lista_rut = cargar_rut()
    imprimir_rut(lista_rut)